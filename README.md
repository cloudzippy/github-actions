# github-actions

Sample Python Flask application with a Dockerfile.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open <http://localhost:5000>.

## Build and run with Docker

```bash
docker build -t sample-flask-app .
docker run --rm -p 5000:5000 sample-flask-app
```

Then visit:
- <http://localhost:5000>
- <http://localhost:5000/health>
