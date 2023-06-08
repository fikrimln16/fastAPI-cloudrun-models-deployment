# Deploy FastAPI dengan menggunakan Cloud Run
Deploy FastAPI Machine Learning model dengan menggunakan CloudRun


## Kebutuhan
* Pyenv (optional)
* Virtualenv (optional)
* Python 3.9
* Google Cloud Platform Account
* Google Cloud Platform - API Cloud Build


## Jalankan secara lokal
```
$ virtualenv -p python3.8.2 .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ uvicorn main:app --reload
```

## Cara deploy ke cloud-run menggunakan cloud SDK
```
$ gcloud init
$ gcloud services enable run.googleapis.com
$ gcloud builds submit --tag gcr.io/[project-id-kalian]/fastapi-model-deployment
$ gcloud run deploy --image gcr.io/[project-id-kalian]/fastapi-model-deployment --platform managed --region asia-southeast2 --allow-unauthenticated fastapi-model-ml
```
