from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Dict


# ---------- API SCHEMAS ----------

class DeviceRegistrationRequest(BaseModel):
    device_id: str
    manufacturer: str
    model: str
    android_version: str
    capabilities: Dict[str, bool] = Field(default_factory=dict)


class DeviceRegistrationResponse(BaseModel):
    device_token: str
    poll_interval_sec: int = 30


class DeviceRegistration(BaseModel):
    device_id: str
    agent_version: str
    manufacturer: str
    model: str
    soc: Optional[str] = None
    android_version: str
    build_fingerprint: Optional[str] = None
    capabilities: Optional[Dict[str, bool]] = {}

class Device(BaseModel):
    device_id: str = Field(..., description="Stable logical device ID")
    device_token: str = Field(..., description="Auth token for device")
    manufacturer: str
    model: str
    android_version: str
    capabilities: Dict[str, bool] = Field(
        default_factory=dict,
        description="Device capabilities (cellular, wifi, gps, etc)"
    )
    registered_at: datetime
    last_seen_at: datetime