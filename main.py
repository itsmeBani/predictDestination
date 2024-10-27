# app.py
from fastapi import FastAPI

from PredictDestination import predictnextdestination
from Utils import read_driver_trips

app = FastAPI() 
@app.get("/predict/{docID}")
async def predict(docID:str):
    data=read_driver_trips(docID)
    prediction = predictnextdestination(data)
    return prediction


@app.get("/suggestedPlace/{docID}")
async  def suggestedPlace(docID:str):
    return docID