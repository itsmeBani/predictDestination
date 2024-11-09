# app.py
from fastapi import FastAPI

from PredictDestination import predictnextdestination
from Utils import read_driver_trips
from suggestedPlace import suggest_cluster_centers

app = FastAPI() 
@app.get("/predict/{docID}")
async def predict(docID:str):
    data=read_driver_trips(docID)
    prediction = predictnextdestination(data)
    return prediction


@app.get("/suggestedPlace/{docID}")
async  def getSuggestedPlace(docID:str):
    data=read_driver_trips(docID)
    if len(data) >= 3:
      suggestedplace=suggest_cluster_centers(data,3)
      return suggestedplace
    else:
        return False