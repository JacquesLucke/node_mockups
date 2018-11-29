from .. base import MockupNode

ArrayNode = MockupNode.create_simple(
    "mn_ArrayNode", "Array",
    inputs = [
        ("Geometry", "Geometry"),
        ("Integer", "Count"),
        ("Vector", "Offset"),
    ],
    outputs = [
        ("Geometry", "Geometry")
    ]
)
