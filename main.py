from fastapi import FastAPI, HTTPException
from adbutils import adb, AdbTimeout
from functools import wraps

app = FastAPI()

def handle_adb_errors(func):
    """Decorator to catch common ADB exceptions and return HTTP errors."""
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except AdbTimeout as e:
            raise HTTPException(status_code=500, detail=f"ADB timeout: {e}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {e}")
    return wrapper

@app.get("/")
async def read_root():
    return {"message": "Welcome to ADB server!"}

@app.get("/devices")
@handle_adb_errors
async def get_adb_devices():
    """Returns a list of connected ADB devices."""
    return {"devices": adb.device_list()}

@app.post("/connect/{addr}")
@handle_adb_errors
async def connect(addr: str):
    """Connect to a device via its IP address and port."""
    return {"result": adb.connect(addr=addr)}

@app.post("/device/{serial}/volume_up")
@handle_adb_errors
async def volume_up(serial: str):
    """Send volume up command to a specified device."""
    device = adb.device(serial)
    device.volume_up()
    return {"message": f"Sent volume up command to device {serial}."}

@app.post("/device/{serial}/volume_down")
@handle_adb_errors
async def volume_down(serial: str):
    """Send volume down command to a specified device."""
    device = adb.device(serial)
    device.volume_down()
    return {"message": f"Sent volume down command to device {serial}."}