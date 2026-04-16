import cv2
import torch
from model.model import TakaDetector

# 1. Initialize the Pipeline
# This loads the YOLOv26 weights from Phase-1
weights_path = "model\\weights\\best.pt"
detector = TakaDetector(weights_path)

def run_sample_inference(image_path):
    print(f"--- Processing Image: {image_path} ---")
    
    # Read image as bytes to simulate the API behavior
    with open(image_path, "rb") as f:
        image_bytes = f.read()

    # 2. Perform Object Detection
    # Returns detected classes, confidence scores, and bounding box coordinates
    detections = detector.predict(image_bytes)

    # 3. Print Results
    if not detections:
        print("No Bangladeshi Taka notes or coins detected.")
    else:
        print(f"{'Denomination':<15} | {'Confidence':<10} | {'Bounding Box'}")
        print("-" * 50)
        for det in detections:
            bbox_str = [round(c, 1) for c in det['bbox']]
            print(f"{det['denomination']:<15} | {det['confidence']:<10.2f} | {bbox_str}")

# --- Execution ---
test_image_path = "test_images\\20_16_jpg.rf.c585e30f37f423ac3789ff931aeef680.jpg" 
try:
    run_sample_inference(test_image_path)
except FileNotFoundError:
    print("Please provide a valid path to a test image.")