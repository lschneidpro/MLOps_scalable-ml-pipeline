# Put the code for your API here.

from joblib import load
from typing import Dict

from fastapi import FastAPI, Request
import pandas as pd

from api.schemas import PredictPayload
from src.ml.data import process_data
from src.ml.model import inference

cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]


app = FastAPI(debug=True)

@app.on_event("startup")
def load_artifacts():
    global model
    global encoder
    global lb
    model = load('./model/model.joblib')
    encoder = load('./model/encoder.joblib')
    lb = load('./model/lb.joblib')

@app.get("/")
async def say_hello():
    return {"greeting": "Hello World!"}

@app.post("/predict")
async def predict(payload: PredictPayload) -> Dict:
      
    data = pd.DataFrame(
        {
            'workclass':payload.workclass.value,
            'education':payload.education.value,
            'marital-status':payload.marital_status.value,
            'occupation':payload.occupation.value,
            'relationship':payload.relationship.value,
            'race':payload.race.value,
            'sex':payload.sex.value,
            'native-country':payload.native_country.value,
        },
        index=[0]
        )
    X, _, _, _ = process_data(
        data, categorical_features=cat_features, label=None, training=False,
        encoder = encoder, lb=lb
        )
    preds = inference(model, X)
    label = lb.inverse_transform(preds)[0]
    
    response = {"prediction": 
                {"salary":label
                 }
                }
    return response