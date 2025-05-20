# 🖥️ Linux Monitor API

A **FastAPI** project to expose various Linux system statistics as RESTful APIs using common Linux commands.

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

## 📌 License

This project is licensed under the MIT License.