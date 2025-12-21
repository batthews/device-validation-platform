from pydantic import BaseModel
from datetime import datetime
from typing import Dict, Optional


class TestResult(BaseModel):
    assignment_id: str
    success: bool
    metrics: Dict[str, float]
    logs: Optional[str] = None
    error_message: Optional[str] = None
    reported_at: datetime
