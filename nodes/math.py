import bpy
from .. base import MockupNode

class FloatMathNode(MockupNode, bpy.types.Node):
    bl_idname = "mn_FloatMathNode"
    bl_label = "Float Math"

    input_sockets = [
        ("mn_FloatSocket", "A"),
        ("mn_FloatSocket", "B"),
    ]

    output_sockets = [
        ("mn_FloatSocket", "Result"),
    ]
