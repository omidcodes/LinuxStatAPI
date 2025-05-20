from fastapi import APIRouter
from app.utils.run_command import run_command

router = APIRouter()

@router.get("/network/ip")
def get_ip():
    return {"output": run_command("ip a")}

@router.get("/network/route")
def get_route():
    return {"output": run_command("ip route")}

@router.get("/network/ss")
def get_ss():
    return {"output": run_command("ss -tuln")}

@router.get("/network/ping")
def get_ping():
    return {"output": run_command("ping -c 4 8.8.8.8")}

@router.get("/network/traceroute")
def get_traceroute():
    return {"output": run_command("traceroute google.com")}

@router.get("/network/dig")
def get_dig():
    return {"output": run_command("dig example.com")}

@router.get("/network/nmcli")
def get_nmcli():
    return {"output": run_command("nmcli dev show")}