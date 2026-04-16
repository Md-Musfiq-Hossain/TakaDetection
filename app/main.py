from fastapi import FastAPI, UploadFile, File, HTTPException
from model.model import TakaDetector
from app.schemas import PredictionOutput
import io

app = FastAPI(title="Bangladeshi Taka Detection API")

# Initialize detector using relative path to weights folder
detector = TakaDetector("model/weights/best.pt")

@app.get("/")
def read_root():
    return {"message": "Bangladeshi Taka Detection API is live! Use /docs to test."}

@app.post("/predict", response_model=PredictionOutput)
async def predict(file: UploadFile = File(...)):
    # Validate file type
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Only JPEG and PNG are supported")

    try:
        image_content = await file.read()
        predictions = detector.predict(image_content)
        
        return {
            "status": "success",
            "count": len(predictions),
            "detections": predictions
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))