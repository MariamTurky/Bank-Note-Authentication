from fastapi import FastAPI
import uvicorn
import app.model.model as model_module


app = FastAPI(title="BankNote Authentication API", version="1.0.0", description="Predicts whether a banknote is authentic (1) or fake (0).")

@app.get("/", tags=["health"])

def root():
    return {"status": "ok", "message": "BankNote Authentication API is running."}


@app.post("/predict", tags=["inference"])
def predict(data: model_module.BankNoteAuthenticator):
    data = data.dict()
    varsiance = data['varsiance']
    skewness = data['skewness']
    curtosis = data['curtosis']
    entropy = data['entropy']
    note = model_module.BankNoteAuthenticator(varsiance=varsiance, skewness=skewness, curtosis=curtosis, entropy=entropy)
    prediction = note.predict()
    
    if(prediction > 0.5):
        prediction="Fake note"
    else:
        prediction="Its a Bank note"
    return {
        'prediction': prediction
    }
