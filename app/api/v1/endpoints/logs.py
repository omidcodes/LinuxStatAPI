from fastapi import APIRouter
from app.utils.run_command import run_command

router = APIRouter()

@router.get("/logs/syslog")
def get_syslog():
    return {"output": run_command("tail -n 100 /var/log/syslog")}

@router.get("/logs/auth")
def get_auth_log():
    return {"output": run_command("less /var/log/auth.log")}

@router.get("/logs/dmesg")
def get_dmesg():
    return {"output": run_command("dmesg")}