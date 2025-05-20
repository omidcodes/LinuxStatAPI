import platform
import sys
from fastapi.responses import RedirectResponse
from app.api.v1.endpoints import (
    system,
    cpu_memory,
    disk,
    network,
    processes,
    logs,
    hardware,
)
from fastapi import FastAPI


app = FastAPI(title="Linux Monitor API")

# Block non-Linux OS
if platform.system() != "Linux":
    print("❌ This API project only runs on Linux systems.")
    sys.exit(1)


# Redirect root (/) to /docs
@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")


app.include_router(system.router, prefix="/api")
app.include_router(cpu_memory.router, prefix="/api")
app.include_router(disk.router, prefix="/api")
app.include_router(network.router, prefix="/api")
app.include_router(processes.router, prefix="/api")
app.include_router(logs.router, prefix="/api")
app.include_router(hardware.router, prefix="/api")
