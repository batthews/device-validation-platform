from app.models.device import Device, DeviceRegistration

from fastapi import FastAPI, HTTPException
from datetime import datetime
import uuid

from app.models import TestAssignment, AssignmentStatus
from app.schemas.test_assignment import (
    TestAssignmentRequest,
    TestAssignmentResponse,
)
from app.state import DEVICES, TEST_DEFINITIONS, TEST_ASSIGNMENTS


app = FastAPI(title="Device Validation Platform API")

@app.get("/")
def read_root():
    return {"message": "Hello, Device Validation Platform!"}

@app.post("/api/v1/devices/register")
def register_device(device: DeviceRegistration):
    # Save device info in memory
    device_token = str(uuid.uuid4())

    registered_device = Device(
        device_id=device.device_id,
        manufacturer=device.manufacturer,
        model=device.model,
        android_version=device.android_version,
        agent_version=device.agent_version,
        capabilities=device.capabilities,
        device_token=device_token,
        registered_at=datetime.utcnow(),
        last_seen_at=datetime.utcnow(),
    )

    DEVICES[device.device_id] = registered_device
    
    return {
        "device_token": device_token,
        "poll_interval_sec": 300,
        "message": "Device registered successfully"
    }


@app.post("/api/v1/tests/assign", response_model=TestAssignmentResponse)
def assign_test(req: TestAssignmentRequest):

    # 1. Find device by token
    device = next(
        (d for d in DEVICES.values() if d.device_token == req.device_token),
        None,
    )

    if not device:
        raise HTTPException(status_code=401, detail="Invalid device token")

    # 2. Check if device already has an active assignment
    for assignment in TEST_ASSIGNMENTS.values():
        if assignment.device_id == device.device_id and assignment.status in {
            AssignmentStatus.ASSIGNED,
            AssignmentStatus.RUNNING,
        }:
            return TestAssignmentResponse(assigned=False)

    # 3. Find first enabled test
    test_def = next(
        (t for t in TEST_DEFINITIONS.values() if t.enabled),
        None,
    )

    if not test_def:
        return TestAssignmentResponse(assigned=False)

    # 4. Create assignment
    assignment_id = str(uuid.uuid4())

    assignment = TestAssignment(
        assignment_id=assignment_id,
        test_id=test_def.test_id,
        device_id=device.device_id,
        parameters={
            "duration_sec": 300,
            "band": "LTE",
            "load": "high",
        },
        status=AssignmentStatus.ASSIGNED,
        assigned_at=datetime.utcnow(),
    )

    TEST_ASSIGNMENTS[assignment_id] = assignment

    return TestAssignmentResponse(
        assigned=True,
        assignment_id=assignment.assignment_id,
        test_id=test_def.test_id,
        test_type=test_def.test_type,
        parameters=assignment.parameters,
    )
