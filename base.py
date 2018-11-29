import bpy

class MockupNodeTree(bpy.types.NodeTree):
    bl_idname = "mn_MockupNodeTree"
    bl_label = "Mockup Nodes"
    bl_icon = 'NODETREE'

class MockupNode:
    def init(self, context):
        for idname, name in self.input_sockets:
            self.inputs.new(idname, name)
        for idname, name in self.output_sockets:
            self.outputs.new(idname, name)

class MockupSocket:
    def draw(self, context, layout, node, text):
        if self.is_output or self.is_linked:
            layout.label(text=text)
        else:
            self.draw_property(layout, node, text)

    def draw_color(self, context, node):
        return self.color
