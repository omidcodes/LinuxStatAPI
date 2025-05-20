# 🚀 FastAPI Project

A modern and scalable backend API built with [FastAPI](https://fastapi.tiangolo.com/), featuring clean architecture, automatic docs, and ready-to-test endpoints.

---

## 📁 Project Structure

```
fastapi_project/
├── app/
│   ├── main.py                # App entry point
│   ├── api/
│   │   └── v1/
│   │       └── endpoints/
│   │           └── user.py    # Sample user endpoint
│   ├── core/
│   │   └── config.py          # App settings
│   ├── models/                # Pydantic schemas (future)
│   ├── services/              # Business logic (future)
│   └── __init__.py
├── tests/
│   └── test_user.py           # Example test
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Run

### 1. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the server
```bash
uvicorn app.main:app --reload
```

Visit: [http://localhost:8000/docs](http://localhost:8000/docs) for Swagger UI.

---

## 🧪 Run Tests

### Make sure you're in the project root:
```bash
pytest -v
```

If necessary, run with:
```bash
PYTHONPATH=./ pytest -v
```

---

## 📦 Dependencies

- `fastapi`
- `uvicorn[standard]`
- `pydantic`
- `pytest`
- `httpx`

(See `requirements.txt` for full list)

---

## 📌 Features

- Modular structure for easy scaling
- Swagger & ReDoc auto-generated docs
- Sample API with versioning (`/api/v1/users/`)
- Unit test integration with `pytest`


---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
