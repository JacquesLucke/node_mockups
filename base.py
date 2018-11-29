import bpy

class MockupNodeTree(bpy.types.NodeTree):
    bl_idname = "mn_MockupNodeTree"
    bl_label = "Mockup Nodes"
    bl_icon = 'NODETREE'

class MockupNode:
    def init(self, context):
        self.refresh()

    input_sockets = []
    output_sockets = []

    def refresh(self):
        from . sockets import get_idname_by_data_type

        self.inputs.clear()
        self.outputs.clear()

        for data_type, name in self.input_sockets:
            self.inputs.new(get_idname_by_data_type(data_type), name)
        for data_type, name in self.output_sockets:
            self.outputs.new(get_idname_by_data_type(data_type), name)

    @classmethod
    def create_simple(cls, identifier, label, *, inputs=[], outputs=[]):
        NodeCls = type(identifier, (cls, bpy.types.Node), {
            "bl_idname" : identifier,
            "bl_label" : label,
            "input_sockets" : inputs,
            "output_sockets" : outputs,
        })

        return NodeCls

class MockupSocket:
    def draw(self, context, layout, node, text):
        if self.is_output or self.is_linked:
            layout.label(text=text)
        else:
            self.draw_property(layout, node, text)

    def draw_color(self, context, node):
        return self.color

    def get_property(self):
        return None

    def set_property(self, value):
        pass
