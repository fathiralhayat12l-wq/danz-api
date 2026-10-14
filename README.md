# Danz API

A small Flask API scaffold prepared for deployment.

## Endpoints

- `GET /` — API info
- `GET /health` — health check
- `GET /generate?count=5&pattern=random` — generate synthetic numeric IDs
- Supported patterns: `random`, `pretty`, `1555`
- `count` must be between 1 and 100.

Example response:

```json
{
  "status": "success",
  "creator": "Danz",
  "pattern": "random",
  "count": 2,
  "results": ["12345678", "87654321"],
  "verified": false
}
```

Important: generated numbers are synthetic. This API does not access Garena/Free Fire systems, verify account existence, or return real account data.

## Run locally

```bash
pip install -r requirements.txt
python app.py
```

Then open `http://127.0.0.1:5000/generate?count=5&pattern=pretty`.

## Deploy on Render

1. Upload these files to a GitHub repository.
2. In Render, choose **New + → Web Service** and connect the repository.
3. Build command: `pip install -r requirements.txt`
4. Start command: `gunicorn app:app --bind 0.0.0.0:$PORT`
5. Deploy. Render will provide the public URL if the deployment succeeds.

This package is deployment-ready, but it is not online until you deploy it through your own hosting account.
