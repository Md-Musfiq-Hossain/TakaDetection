from ultralytics import YOLO
import cv2
import numpy as np

class TakaDetector:
    def __init__(self, model_path):
        # Loads the trained weights from Phase-1
        self.model = YOLO(model_path)

    def predict(self, image_bytes):
        # Decode the uploaded image bytes
        nparr = np.frombuffer(image_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        # Perform detection
        results = self.model.predict(img, conf=0.25)[0]
        
        detections = []
        for box in results.boxes:
            detections.append({
                "denomination": self.model.names[int(box.cls)],
                "confidence": float(box.conf),
                "bbox": box.xyxy.tolist()[0]
            })
        return detections