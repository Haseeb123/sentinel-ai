# Installation

## Clone

```bash
git clone https://github.com/YOUR_USERNAME/sentinel-ai.git
```

## Create Environment

```bash
python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

Linux/macOS

```bash
source .venv/bin/activate
```

## Install

```bash
pip install -r requirements.txt
```

## Run

```bash
uvicorn backend.app:app --reload
```

Swagger

```
http://127.0.0.1:8000/docs
```