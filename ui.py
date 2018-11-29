import bpy
from . base import MockupNode

class MockupsPanel(bpy.types.Panel):
    bl_idname = "mn.mockups"
    bl_label = "Mockups"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'TOOLS'

    def draw(self, context):
        layout = self.layout
        for cls in MockupNode.__subclasses__():
            props = layout.operator("node.add_node", text=cls.bl_label)
            props.type = cls.bl_idname
            props.use_transform = True
