from pydantic import BaseModel
from typing import Dict, Any, Optional


class TestAssignmentRequest(BaseModel):
    device_token: str


class TestAssignmentResponse(BaseModel):
    assigned: bool
    assignment_id: Optional[str] = None
    test_id: Optional[str] = None
    test_type: Optional[str] = None
    parameters: Optional[Dict[str, Any]] = None
