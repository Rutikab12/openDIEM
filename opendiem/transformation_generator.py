from opendiem.transformation_engine import (
    TransformationEngine
)


class TransformationGenerator:

    def __init__(self):

        self.engine = TransformationEngine()

    def build(self, transformations):

        code_blocks = []

        for transformation in transformations:

            code = self.engine.get_transformation_code(
                transformation
            )

            code_blocks.append(code)

        return "\n\n".join(code_blocks)