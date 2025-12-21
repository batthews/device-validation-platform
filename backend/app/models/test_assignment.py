from pydantic import BaseModel, Field
from datetime import datetime
from typing import Dict, Optional, Any
from enum import Enum


class AssignmentStatus(str, Enum):
    QUEUED = "queued"
    ASSIGNED = "assigned"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


class TestAssignment(BaseModel):
    assignment_id: str
    test_id: str
    device_id: str
    parameters: Dict[str, Any]
    status: AssignmentStatus
    assigned_at: datetime
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
