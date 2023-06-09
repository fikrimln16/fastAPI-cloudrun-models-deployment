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

## Cara deploy ke cloud-run menggunakan Google Cloud Platform 
```
$ Pastikan Anda memiliki akun Google Cloud Platform (GCP) yang aktif. Jika belum, daftar dan buat proyek baru di https://console.cloud.google.com.
$ Pastikan Anda telah menginstal Google Cloud SDK (https://cloud.google.com/sdk) dan menginisialisasi dengan menjalankan perintah berikut di terminal atau command prompt:
  `gcloud init`
$ gcloud builds submit --tag gcr.io/[project-id-kalian]/fastapi-model-deployment
$ gcloud run deploy --image gcr.io/[project-id-kalian]/fastapi-model-deployment --platform managed --region asia-southeast2 --allow-unauthenticated fastapi-model-ml
```
