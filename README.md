# NFLStatsApp-Backend
fast api backend for NFLStatsApp 

## Setup
### 1. Set up Virtual Environment

```bash
python3 -m venv .venv
```

### 2. Activate Virtual Environment

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r api/requirements.txt
```

### 4. Set certificate path

```bash
export SSL_CERT_FILE=$(python -m certifi)
```

### 5. Create .env file
set API_KEY in .env file

## Instructions
### 1. Run the server

```bash
uvicorn main:app --reload
```

### 2. View interactive API docs

http://127.0.0.1:8000/docs
