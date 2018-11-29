from .. base import MockupNode

FloatMathNode = MockupNode.create_simple(
    "mn_FloatMathNode", "Float Math",
    inputs = [
        ("Float", "A"),
        ("Float", "B")
    ],
    outputs = [
        ("Float", "Result")
    ]
)
