import bpy
from bpy.props import *
from . base import MockupSocket

def get_idname_by_data_type(data_type):
    for socket_cls in MockupSocket.__subclasses__():
        if socket_cls.data_type == data_type:
            return socket_cls.bl_idname
    raise Exception("data type not found: " +  data_type)

def to_list_color(color):
    return (*color[:3], 0.5)

class SimpleValueSocket:
    def get_property(self):
        return self.value

    def set_property(self, value):
        self.value = value

    def draw_property(self, layout, node, text):
        layout.prop(self, "value", text=text)

class FloatSocket(MockupSocket, SimpleValueSocket, bpy.types.NodeSocket):
    bl_idname = "mn_FloatSocket"
    bl_label = "Float Socket"
    data_type = "Float"
    color = (0.5, 0.5, 0.9, 1)

    value: FloatProperty()

class IntegerSocket(MockupSocket, SimpleValueSocket, bpy.types.NodeSocket):
    bl_idname = "mn_IntegerSocket"
    bl_label = "Integer Socket"
    data_type = "Integer"
    color = (0.3, 0.7, 0.9, 1)

    value: IntProperty()

class TextSocket(MockupSocket, SimpleValueSocket, bpy.types.NodeSocket):
    bl_idname = "mn_TextSocket"
    bl_label = "Text Socket"
    data_type = "Text"
    color = (0.9, 0.9, 0.9, 1)

    value: StringProperty()

class VectorSocket(MockupSocket, bpy.types.NodeSocket):
    bl_idname = "mn_VectorSocket"
    bl_label = "Vector Socket"
    data_type = "Vector"
    color = (0.2, 0.2, 0.7, 1)

    value: FloatVectorProperty(size=3)

    def draw_property(self, layout, node, text):
        return layout.column().prop(self, "value", text=text)

    def get_property(self):
        return tuple(self.value)

    def set_property(self, value):
        self.value = value

class FloatListSocket(MockupSocket, bpy.types.NodeSocket):
    bl_idname = "mn_FloatListSocket"
    bl_label = "Float List"
    data_type = "Float List"
    color = to_list_color(FloatSocket.color)

class VectorListSocket(MockupSocket, bpy.types.NodeSocket):
    bl_idname = "mn_VectorListSocket"
    bl_label = "Vector List"
    data_type = "Vector List"
    color = to_list_color(VectorSocket.color)

class GeometrySocket(MockupSocket, bpy.types.NodeSocket):
    bl_idname = "mn_GeometrySocket"
    bl_label = "Geometry Socket"
    color = (0.8, 0.4, 0.4, 1)
    data_type = "Geometry"

    def draw_property(self, layout, node, text):
        layout.label(text=text)



