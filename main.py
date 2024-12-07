from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from PredictDestination import predictnextdestination
from Utils import read_driver_trips


app = FastAPI()


# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (or specify allowed origins)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all HTTP headers
)



@app.get("/predict/{docID}")
async def predict(docID:str):
    data=read_driver_trips(docID)
    prediction = predictnextdestination(data)
    return prediction





