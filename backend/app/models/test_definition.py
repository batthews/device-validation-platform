from pydantic import BaseModel, Field
from datetime import datetime
from typing import Dict, Any


class TestDefinition(BaseModel):
    test_id: str = Field(..., description="Stable test identifier")
    name: str
    test_type: str = Field(..., description="radio, thermal, performance, etc")
    description: str
    parameters_schema: Dict[str, Any] = Field(
        ..., description="Expected parameters and types"
    )
    compatible_devices: Dict[str, Any] = Field(
        default_factory=dict,
        description="Constraints like model, soc, capabilities"
    )
    enabled: bool = True
    created_at: datetime
