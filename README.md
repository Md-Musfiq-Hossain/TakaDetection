# 🇧🇩 Bangladeshi Taka Detection API

---

## 📁 Folder Structure

```bash
TakaDetection/
├── app/
│   ├── main.py
│   └── schemas.py
├── model/
│   ├── model.py
│   └── weights/
│       └── (your YOLO weights)
├── requirements.txt
├── Dockerfile
└── README.md
```

---

This repository contains a high-performance REST API for detecting Bangladeshi Taka notes and coins. The project leverages a fine-tuned YOLOv8 model integrated with FastAPI and is fully containerized for portability.

🛠️ Installation & Setup  
1. Prerequisites  
Docker Desktop: Ensure it is installed and the engine is running.

Git: Required for cloning the repository and version control.

2. Building and Running (The Easy Way)  
Using Docker Compose is the recommended method as it handles networking, volume mounting, and port mapping automatically.

Bash  
# Navigate to the project root and run:  
docker compose up --build  
3. Alternative (Manual Build)  
If you prefer using standard Docker CLI commands, follow these two steps:

Build the image:  
Bash  
docker build -t taka-detection-app .  
Run the container:  
Bash  
docker run -p 8000:8000 taka-detection-app  
🚀 How to Use the API  
Once the container is active, the API is accessible at http://localhost:8000.

1. Interactive Documentation (Swagger UI)  
FastAPI provides a built-in interface to test your endpoints without needing Postman. Visit http://localhost:8000/docs in your browser:

Locate and expand the POST /predict endpoint.

Click the "Try it out" button.

Upload a supported image (JPG/PNG) of Bangladeshi currency.

Click Execute to see the real-time detection results.

2. API Endpoint Details  
Endpoint: /predict

Method: POST

Request Type: multipart/form-data (Binary Image File)

Example Success Response:  
JSON  
{
  "status": "success",
  "count": 1,
  "detections": [
    {
      "denomination": "5 taka coin",
      "confidence": 0.92,
      "bbox": [120.5, 45.2, 300.1, 250.8]
    }
  ]
}  
📝 Troubleshooting  
Port Conflicts: If you get a "Port already in use" error, ensure no other instance of Uvicorn or another web server is running on port 8000.

Path Errors: The application is configured to use Linux-style forward slashes (/) for compatibility inside the Docker container. Ensure your local main.py matches this configuration.

Memory Issues: YOLO models require sufficient RAM. Ensure Docker Desktop is allocated at least 2GB of memory for optimal performance.
