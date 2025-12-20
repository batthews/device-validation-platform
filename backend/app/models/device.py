from pydantic import BaseModel
from typing import Optional, Dict

class DeviceRegistration(BaseModel):
    device_id: str
    agent_version: str
    manufacturer: str
    model: str
    soc: Optional[str] = None
    android_version: str
    build_fingerprint: Optional[str] = None
    capabilities: Optional[Dict[str, bool]] = {}
