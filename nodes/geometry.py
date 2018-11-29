from .. base import MockupNode

GetVectorAttribute = MockupNode.create_simple(
    "mn_GetVectorAttributeNode", "Get Geometry Attribute",
    inputs = [
        ("Geometry", "Geometry"),
        ("Text", "Name")
    ],
    outputs = [
        ("Vector List", "Values")
    ]
)
