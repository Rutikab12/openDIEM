from opendiem.quality_engine import (
    QualityEngine
)


class QualityGenerator:

    def __init__(self):

        self.engine = QualityEngine()

    def build(self, quality_rules):

        code_blocks = []

        for rule in quality_rules:

            code = self.engine.get_quality_code(
                rule
            )

            code_blocks.append(code)

        return "\n\n".join(code_blocks)