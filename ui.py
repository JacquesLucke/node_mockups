import bpy

class MockupsPanel(bpy.types.Panel):
    bl_idname = "mn.mockups"
    bl_label = "Mockups"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'TOOLS'

    def draw(self, context):
        layout = self.layout
        props = layout.operator("node.add_node", text="Float Math")
        props.type = "mn_FloatMathNode"
        props.use_transform = True
