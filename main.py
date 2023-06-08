from fastapi import FastAPI
import tensorflow as tf
from pydantic import BaseModel

app = FastAPI()

#buat basemodel untuk post
class DataInput(BaseModel):
    data: int

#import model h5 disini, sebagai contoh inputan model linear
model = tf.keras.models.load_model('./linear.h5')

@app.get("/")
def hello():
    return {"message": "fastAPI CloudRun Tensorflow Deployment"}

#contoh untuk get model predict
@app.get("/predict")
def predict():
    predict = model.predict([[10.0]])
    res = predict.item()
    return {"res" : res}

#contoh untuk post model predict
@app.post("/predict")
def predict(data: DataInput):
    predict = model.predict([[data.data]])
    res = predict.item()
    return {"res" : res}




