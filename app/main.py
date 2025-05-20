from fastapi import FastAPI
from app.api.v1.endpoints import cpu_memory, disk, hardware, logs, network, processes, system 

app = FastAPI(title="Linux Monitor API")

app.include_router(system.router, prefix="/api")
app.include_router(cpu_memory.router, prefix="/api")
app.include_router(disk.router, prefix="/api")
app.include_router(network.router, prefix="/api")
app.include_router(processes.router, prefix="/api")
app.include_router(logs.router, prefix="/api")
app.include_router(hardware.router, prefix="/api")