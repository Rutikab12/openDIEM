from pathlib import Path

from jinja2 import (
    Environment,
    FileSystemLoader
)

from opendiem.transformation_generator import (
    TransformationGenerator
)

from opendiem.quality_generator import (
    QualityGenerator
)


class SparkPipelineGenerator:

    def __init__(self):

        template_dir = (
            Path(__file__).parent / "templates"
        )

        self.env = Environment(
            loader=FileSystemLoader(template_dir)
        )

        self.transformation_generator = (
            TransformationGenerator()
        )

        self.quality_generator = (
    QualityGenerator()
    )

    def generate(self, config):

        transformation_code = (
            self.transformation_generator.build(
                config.transformations
            )
        )

        template = self.env.get_template(
            "spark_pipeline.j2"
        )

        quality_code = (
    self.quality_generator.build(
        config.quality_rules
    )
)

        rendered_code = template.render(
            pipeline_name=config.pipeline_name,
            source_type=config.source.type,
            source_path=config.source.path,
            target_type=config.target.type,
            target_path=config.target.path,
            load_type=config.load_type,
            transformation_code=transformation_code,
            quality_code=quality_code
)

        output_dir = Path("generated")

        output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        output_file = (
            output_dir /
            f"{config.pipeline_name}.py"
        )

        with open(
            output_file,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(rendered_code)

        return output_file