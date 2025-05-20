from fastapi import APIRouter
from app.utils.run_command import run_command

router = APIRouter()

@router.get("/disk/df")
def get_df():
    return {"output": run_command("df -h")}

@router.get("/disk/du")
def get_du():
    return {"output": run_command("du -sh *")}

@router.get("/disk/lsblk")
def get_lsblk():
    return {"output": run_command("lsblk")}

@router.get("/disk/mount")
def get_mount():
    return {"output": run_command("mount")}

@router.get("/disk/fdisk")
def get_fdisk():
    return {"output": run_command("fdisk -l")}

@router.get("/disk/findmnt")
def get_findmnt():
    return {"output": run_command("findmnt")}