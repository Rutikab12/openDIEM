import yaml
from opendiem.models import PipelineConfig


def load_pipeline_config(file_path):
    with open(file_path, "r") as f:
        data = yaml.safe_load(f)

    return PipelineConfig(**data)