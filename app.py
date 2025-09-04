from fastapi import FastAPI, HTTPException
from model.data import Features

from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from pickle import load
import numpy as np

app = FastAPI()
fake_db = {}

item_id_counter = 0

@app.post("/items/", status_code=201)
async def create_item(features: Features):

    global item_id_counter
    pca = load(open('utils/PCA_2025-09-04.pkl', 'rb'))
    logreg = load(open('utils/LogisticRegression_2025-09-04.pkl', 'rb'))

    features_dict = features.dict()
    
    data = list(features_dict.values())
    data = np.array(data)\
             .reshape(1, -1)
    data = pca.transform(data)
    prediction = logreg.predict(data)

    features_dict['prediction'] = prediction

    item_id = str(item_id_counter)
    fake_db[item_id] = features_dict
    item_id_counter += 1

    return {"message": "Item created successfully", 
            "item_id": item_id, 
            "features": features}

@app.get("/items/{item_id}")
async def read_item(item_id: str):

    if item_id not in fake_db:
        raise HTTPException(status_code=404, 
                            detail="Item not found.")
    
    return fake_db[item_id]