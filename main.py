from opendiem.parser import load_pipeline_config
from opendiem.generator import SparkPipelineGenerator


def main():

    config_path = "configs/sample_pipeline.yml"

    print("Loading pipeline configuration...")
    config = load_pipeline_config(config_path)

    print(f"Pipeline Name : {config.pipeline_name}")
    print(f"Source Type   : {config.source.type}")
    print(f"Source Path   : {config.source.path}")
    print(f"Target Type   : {config.target.type}")
    print(f"Target Path   : {config.target.path}")
    print()

    print("Generating Spark Pipeline...")

    generator = SparkPipelineGenerator()

    output_file = generator.generate(config)

    print(f"Pipeline generated successfully!")
    print(f"Location: {output_file}")


if __name__ == "__main__":
    main()