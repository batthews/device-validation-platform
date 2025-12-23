from datetime import datetime
from typing import Dict
from app.models import Device, TestDefinition, TestAssignment, AssignmentStatus

DEVICES: Dict[str, Device] = {}
TEST_DEFINITIONS: Dict[str, TestDefinition] = {}
TEST_ASSIGNMENTS: Dict[str, TestAssignment] = {}


TEST_DEFINITIONS["radio_lte_stress"] = TestDefinition(
    test_id="radio_lte_stress",
    name="LTE Radio Stress Test",
    test_type="radio",
    description="Stress LTE radio for signal stability",
    parameters_schema={
        "duration_sec": int,
        "band": str,
        "load": str
    },
    compatible_devices={
        "model": ["Pixel 6"]
    },
    enabled=True,
    created_at=datetime.utcnow()
)
