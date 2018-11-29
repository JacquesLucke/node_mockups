from .. base import MockupNode

ModifierInputNode = MockupNode.create_simple(
    "mn_ModifierInputNode", "Modifier Input",
    outputs = [
        ("Geometry", "Source"),
    ]
)

ModifierOutputNode = MockupNode.create_simple(
    "mn_ModifierOutputNode", "Modifier Output",
    inputs = [
        ("Geometry", "Source"),
    ]
)
