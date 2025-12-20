from fastapi import FastAPI
from .models.device import DeviceRegistration

app = FastAPI(title="Device Validation Platform API")

# Temporary in-memory “database”
registered_devices = {}

@app.get("/")
def read_root():
    return {"message": "Hello, Device Validation Platform!"}

@app.post("/api/v1/devices/register")
def register_device(device: DeviceRegistration):
    # Save device info in memory
    registered_devices[device.device_id] = device.dict()
    
    # Generate a mock device token
    device_token = f"token_{device.device_id}"
    
    return {
        "device_token": device_token,
        "poll_interval_sec": 300,
        "message": "Device registered successfully"
    }
