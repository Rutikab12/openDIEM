from pydantic import BaseModel
from typing import List, Optional, Dict


class SourceConfig(BaseModel):
    type: str
    path: str


class TargetConfig(BaseModel):
    type: str
    path: str


class TransformationConfig(BaseModel):
    type: str

    mappings: Optional[Dict[str, str]] = None

    condition: Optional[str] = None


class QualityRuleConfig(BaseModel):

    type: str

    column: Optional[str] = None

    min_rows: Optional[int] = None


class PipelineConfig(BaseModel):

    pipeline_name: str

    source: SourceConfig

    target: TargetConfig

    load_type: str

    transformations: List[TransformationConfig] = []

    quality_rules: List[QualityRuleConfig] = []