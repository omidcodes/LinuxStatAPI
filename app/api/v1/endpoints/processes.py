from fastapi import APIRouter
from app.utils.run_command import run_command

router = APIRouter()


@router.get("/processes/ps")
def get_ps():
    return {"output": run_command("ps aux")}


@router.get("/processes/systemctl_status")
def get_systemctl_status():
    return {"output": run_command("systemctl status")}


@router.get("/processes/systemctl_services")
def get_systemctl_services():
    return {"output": run_command("systemctl list-units --type=service")}


@router.get("/processes/journalctl")
def get_journalctl():
    return {"output": run_command("journalctl -xe")}
