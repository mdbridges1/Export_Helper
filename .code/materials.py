# SPDX-License-Identifier: MIT
# Export Helper Pro - Material conversion functions


def material_has_principled_bsdf(material):
    """Check if material has a Principled BSDF node."""
    if not material or not material.use_nodes:
        return False
    for node in material.node_tree.nodes:
        if node.type == 'BSDF_PRINCIPLED':
            return True
    return False


def prepare_materials_for_export(objects, convert_viewport=True):
    """Convert Viewport Display colours to Principled BSDF materials.

    Returns a list of material info dicts for restoration after export.
    """
    if not convert_viewport:
        return []

    modified_materials = []

    for obj in objects:
        if obj.type != 'MESH':
            continue

        for slot in obj.material_slots:
            mat = slot.material
            if not mat:
                continue

            if material_has_principled_bsdf(mat):
                continue

            original_use_nodes = mat.use_nodes
            viewport_color = mat.diffuse_color[:3]

            if not mat.use_nodes:
                mat.use_nodes = True
                nodes = mat.node_tree.nodes
                links = mat.node_tree.links
                nodes.clear()

                bsdf = nodes.new('ShaderNodeBsdfPrincipled')
                bsdf.location = (0, 0)
                bsdf.inputs['Base Color'].default_value = (*viewport_color, 1.0)

                output = nodes.new('ShaderNodeOutputMaterial')
                output.location = (300, 0)

                links.new(bsdf.outputs['BSDF'], output.inputs['Surface'])

                modified_materials.append({
                    'material': mat,
                    'original_use_nodes': original_use_nodes,
                    'was_converted': True,
                })
            else:
                nodes = mat.node_tree.nodes
                links = mat.node_tree.links

                output_node = None
                for node in nodes:
                    if node.type == 'OUTPUT_MATERIAL':
                        output_node = node
                        break

                if output_node:
                    bsdf = nodes.new('ShaderNodeBsdfPrincipled')
                    bsdf.name = "_TempPrincipledBSDF"
                    bsdf.location = (output_node.location.x - 300, output_node.location.y)
                    bsdf.inputs['Base Color'].default_value = (*viewport_color, 1.0)

                    old_link = None
                    if output_node.inputs['Surface'].is_linked:
                        old_link = output_node.inputs['Surface'].links[0].from_socket

                    links.new(bsdf.outputs['BSDF'], output_node.inputs['Surface'])

                    modified_materials.append({
                        'material': mat,
                        'original_use_nodes': original_use_nodes,
                        'was_converted': False,
                        'temp_node_name': "_TempPrincipledBSDF",
                        'old_link_socket': old_link,
                    })

    return modified_materials


def cleanup_materials_after_export(modified_materials):
    """Restore materials to their original state after export."""
    for info in modified_materials:
        mat = info['material']

        if info.get('was_converted'):
            mat.use_nodes = info['original_use_nodes']
            if not info['original_use_nodes']:
                mat.node_tree.nodes.clear()
        else:
            temp_node_name = info.get('temp_node_name')
            if temp_node_name and temp_node_name in mat.node_tree.nodes:
                temp_node = mat.node_tree.nodes[temp_node_name]

                old_socket = info.get('old_link_socket')
                if old_socket:
                    output_node = None
                    for node in mat.node_tree.nodes:
                        if node.type == 'OUTPUT_MATERIAL':
                            output_node = node
                            break
                    if output_node:
                        mat.node_tree.links.new(old_socket, output_node.inputs['Surface'])

                mat.node_tree.nodes.remove(temp_node)
