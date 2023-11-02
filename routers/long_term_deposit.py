import joblib
from fastapi import APIRouter
from models.telemarketing import Telemarketing
from utils.helper import preproces_data

router = APIRouter()

@router.post("/predict")
def predict_long_term_deposit(data: Telemarketing):
    # Preprocess the data
    processed_data = preproces_data(data)

    # Load the model
    model = joblib.load("artifacts/model.pkl")

    # Make the prediction
    prediction = model.predict(processed_data)

    # Return the prediction
    return {"prediction": prediction[0].item()}
