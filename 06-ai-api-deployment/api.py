from fastapi import FastAPI
import pickle

app = FastAPI()

# Load model at startup
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def home():
    return {"message": "API is working!"}

@app.get("/predict")
def predict(text: str):
    # This is where your real prediction logic will go
    response = f"Model received: {text}"
    return {"result": response}
