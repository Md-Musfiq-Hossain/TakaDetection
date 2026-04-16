# 🇧🇩 Bangladeshi Taka Detection API
This repository contains a containerized REST API designed to detect Bangladeshi Taka notes and coins. The project utilizes a fine-tuned YOLOv8 model integrated with FastAPI for high-performance inference and Docker for standardized deployment.

# 📂 Project Hierarchy
The project is structured to maintain a clean separation between the API logic and the machine learning model:
```bash
TakaDetection/
├── app/
│   ├── main.py          # FastAPI application routes and logic
│   └── schemas.py       # Pydantic models for API request/response
├── model/
│   ├── model.py         # YOLOv8 inference pipeline class
│   └── weights/
│       └── best.pt          # Trained YOLOv8 model weights from Phase-1
├── Dockerfile           # Instructions for building the Docker image
├── docker-compose.yml   # Orchestration for the containerized service
├── requirements.txt     # Python dependency list
└── README.md            # Project documentation
```
# 🛠️ Installation & Setup
## 1. Prerequisites
* Docker Desktop: Must be installed and running on your host machine.
* Git: Used for repository management.

## 2. Building the Docker Image

To build the image manually from the Dockerfile, open your terminal in the project root and run:
```bash
docker compose up --build
```

### 3. Alternative (Manual Build)

If you prefer using standard Docker CLI commands, follow these two steps:

**Build the image:**

```bash
docker build -t taka-detection-app .
```

**Run the container:**

```bash
docker run -p 8000:8000 taka-detection-app
```

## 🚀 How to Use the API

Once the container is active, the API is accessible at `http://localhost:8000`.

### 1. Interactive Documentation (Swagger UI)

FastAPI provides a built-in interface to test your endpoints without needing Postman. Visit `http://localhost:8000/docs` in your browser:

- Locate and expand the `POST /predict` endpoint.
- Click the "Try it out" button.
- Upload a supported image (JPG/PNG) of Bangladeshi currency.
- Click Execute to see the real-time detection results.

### 2. API Endpoint Details

**Endpoint:** `/predict`

**Method:** `POST`

**Request Type:** `multipart/form-data` (Binary Image File)

**Example Success Response:**

```json
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
```
# 📝 Troubleshooting & Notes
* Path Compatibility: The application uses Linux-style paths (weights/best.pt) to ensure it functions correctly within the Docker environment.

* Port Conflict: If port 8000 is already in use by another application on your host machine, you can change the mapping (e.g., -p 8080:8000).

* Hardware: Inference is performed on the CPU by default within the container to ensure compatibility across different host machines.

