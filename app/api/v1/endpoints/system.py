from fastapi import APIRouter
from app.utils.run_command import run_command

router = APIRouter()


@router.get("/system/uname")
def get_uname():
    return {"output": run_command("uname -a")}


@router.get("/system/hostname")
def get_hostname():
    return {"output": run_command("hostnamectl")}


@router.get("/system/release")
def get_release():
    return {"output": run_command("lsb_release -a")}


@router.get("/system/uptime")
def get_uptime():
    return {"output": run_command("uptime")}


@router.get("/system/user")
def get_user():
    return {"output": run_command("whoami")}


@router.get("/system/id")
def get_user_id():
    return {"output": run_command("id")}


@router.get("/system/architecture")
def get_arch():
    return {"output": run_command("uname -m")}
