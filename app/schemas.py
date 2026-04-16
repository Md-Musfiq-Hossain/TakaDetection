from pydantic import BaseModel
from typing import List

# Data for one detected note/coin
class DetectionResult(BaseModel):
    denomination: str
    confidence: float
    bbox: List[float]

# Main API response
class PredictionOutput(BaseModel):
    status: str
    count: int
    detections: List[DetectionResult]