from fastapi import APIRouter
from app.utils.run_command import run_command

router = APIRouter()

@router.get("/hardware/lshw")
def get_lshw():
    return {"output": run_command("lshw -short")}

@router.get("/hardware/lspci")
def get_lspci():
    return {"output": run_command("lspci")}

@router.get("/hardware/lsusb")
def get_lsusb():
    return {"output": run_command("lsusb")}

@router.get("/hardware/dmidecode")
def get_dmidecode():
    return {"output": run_command("dmidecode")}

@router.get("/hardware/sensors")
def get_sensors():
    return {"output": run_command("sensors")}