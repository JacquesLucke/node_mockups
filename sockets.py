import bpy
from bpy.props import *
from . base import MockupSocket

class FloatSocket(MockupSocket, bpy.types.NodeSocket):
    bl_idname = "mn_FloatSocket"
    bl_label = "Float Socket"
    color = (1, 1, 1, 1)
    data_type = "Float"

    value: FloatProperty()

    def draw_property(self, layout, node, text):
        layout.prop(self, "value", text=text)
