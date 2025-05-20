from fastapi import APIRouter
from app.utils.run_command import run_command

router = APIRouter()


@router.get("/cpu/top")
def get_top():
    return {"output": run_command("top -bn1")}


@router.get("/cpu/vmstat")
def get_vmstat():
    return {"output": run_command("vmstat 1 1")}


@router.get("/cpu/lscpu")
def get_lscpu():
    return {"output": run_command("lscpu")}


@router.get("/memory/free")
def get_free():
    return {"output": run_command("free -h")}


@router.get("/memory/meminfo")
def get_meminfo():
    return {"output": run_command("cat /proc/meminfo")}
