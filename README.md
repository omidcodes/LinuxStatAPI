# 🖥️ Linux Monitor API

A **FastAPI** project to expose various Linux system statistics as RESTful APIs using common Linux commands.

> ⚠️ **Important**: This project only works on **Linux** systems.  
> It uses native Linux shell commands (e.g. `lshw`, `df`, `ps`, etc.)  
> ❌ It will not run correctly on Windows or macOS.

---

## 🚀 Features

- ✅ System Information (kernel, hostname, uptime, user)
- ✅ CPU & Memory Usage (top, free, lscpu)
- ✅ Disk & Filesystem Info (df, du, mount)
- ✅ Network Status (IP, routes, ping, traceroute)
- ✅ Processes & Services (ps, systemctl)
- ✅ Logs (syslog, dmesg, auth.log)
- ✅ Hardware Details (lshw, lspci, sensors)

---

## 📁 Project Structure

```
linux_monitor_api/
├── app/
│   ├── main.py
│   ├── routes/
│   │   ├── system.py
│   │   ├── cpu_memory.py
│   │   ├── disk.py
│   │   ├── network.py
│   │   ├── processes.py
│   │   ├── logs.py
│   │   └── hardware.py
│   └── utils/
│       └── run_command.py
├── tests/
│   ├── test_system.py
│   ├── test_cpu_memory.py
│   ├── test_disk.py
│   ├── test_network.py
│   ├── test_processes.py
│   ├── test_logs.py
│   └── test_hardware.py
├── requirements.txt
└── README.md
```

---

## ▶️ Run the API

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Start the server
```bash
uvicorn app.main:app --reload
```

---

## 🧪 Run Tests

```bash
pytest tests/
```

---

## 🛡️ Notes

- Some commands may require elevated privileges (e.g., `dmidecode`, `lshw`).
- Make sure required tools like `traceroute`, `dig`, or `lm-sensors` are installed if needed.

---

## 📬 Example API Calls

| Endpoint                      | Description                  |
|------------------------------|------------------------------|
| `/api/system/uname`          | Kernel info (`uname -a`)     |
| `/api/cpu/lscpu`             | CPU info (`lscpu`)           |
| `/api/disk/df`               | Disk usage (`df -h`)         |
| `/api/network/ip`            | IP addresses (`ip a`)        |
| `/api/processes/ps`          | Running processes (`ps aux`) |
| `/api/logs/syslog`           | Syslog tail (`tail /syslog`) |
| `/api/hardware/lshw`         | Hardware info (`lshw`)       |

---


## 📡 Command to API Endpoint Mapping

| 🔧 Command | 🛣️ API Endpoint | 📝 Description | 🗂️ Scope |
|-----------|------------------|----------------|--------|
| `uname -a` | `/api/system/uname` | Kernel name, version, architecture | 🔧 System Information |
| `hostnamectl` | `/api/system/hostname` | Show hostname and system information | 🔧 System Information |
| `lsb_release -a` | `/api/system/release` | Ubuntu release information | 🔧 System Information |
| `uptime` | `/api/system/uptime` | System uptime and load average | 🔧 System Information |
| `whoami` | `/api/system/user` | Current logged-in user | 🔧 System Information |
| `id` | `/api/system/id` | User ID and group info | 🔧 System Information |
| `uname -m` | `/api/system/architecture` | System architecture | 🔧 System Information |
| `top` | `/api/cpu/top` | Real-time CPU, memory, processes snapshot | 🧠 CPU & Memory Usage |
| `vmstat 1` | `/api/cpu/vmstat` | CPU/memory system performance | 🧠 CPU & Memory Usage |
| `lscpu` | `/api/cpu/lscpu` | Detailed CPU information | 🧠 CPU & Memory Usage |
| `free -h` | `/api/memory/free` | Memory usage summary | 🧠 CPU & Memory Usage |
| `cat /proc/meminfo` | `/api/memory/meminfo` | Live memory usage details | 🧠 CPU & Memory Usage |
| `df -h` | `/api/disk/df` | Disk space usage | 💾 Disk & Filesystem |
| `du -sh *` | `/api/disk/du` | Disk usage per directory | 💾 Disk & Filesystem |
| `lsblk` | `/api/disk/lsblk` | Block devices overview | 💾 Disk & Filesystem |
| `mount` | `/api/disk/mount` | Mounted filesystems | 💾 Disk & Filesystem |
| `fdisk -l` | `/api/disk/fdisk` | Partition table info | 💾 Disk & Filesystem |
| `findmnt` | `/api/disk/findmnt` | Hierarchical view of mount points | 💾 Disk & Filesystem |
| `ip a` | `/api/network/ip` | Show IP addresses | 🌐 Network |
| `ip route` | `/api/network/route` | Routing table | 🌐 Network |
| `ss -tuln` | `/api/network/ss` | Listening ports (TCP/UDP) | 🌐 Network |
| `ping 8.8.8.8` | `/api/network/ping` | Test network connectivity | 🌐 Network |
| `traceroute google.com` | `/api/network/traceroute` | Trace network route | 🌐 Network |
| `dig example.com` | `/api/network/dig` | DNS lookup | 🌐 Network |
| `nmcli dev show` | `/api/network/nmcli` | Network manager details | 🌐 Network |
| `ps aux` | `/api/processes/ps` | List running processes | 🔋 Processes & Services |
| `systemctl status` | `/api/processes/systemctl_status` | Service manager status | 🔋 Processes & Services |
| `systemctl list-units` | `/api/processes/systemctl_services` | List active services | 🔋 Processes & Services |
| `journalctl -xe` | `/api/processes/journalctl` | View systemd logs | 🔋 Processes & Services |
| `tail -n 100 /var/log/syslog` | `/api/logs/syslog` | Follow system logs | 🔍 Logs |
| `less /var/log/auth.log` | `/api/logs/auth` | Authentication logs | 🔍 Logs |
| `dmesg` | `/api/logs/dmesg` | Kernel ring buffer | 🔍 Logs |
| `lshw -short` | `/api/hardware/lshw` | Detailed hardware info | 🧰 Hardware Info |
| `lspci` | `/api/hardware/lspci` | PCI bus devices | 🧰 Hardware Info |
| `lsusb` | `/api/hardware/lsusb` | USB devices | 🧰 Hardware Info |
| `dmidecode` | `/api/hardware/dmidecode` | BIOS, motherboard, RAM details | 🧰 Hardware Info |
| `sensors` | `/api/hardware/sensors` | CPU temperature sensors | 🧰 Hardware Info |

## 📌 License

This project is licensed under the MIT License.
