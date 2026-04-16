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
'. Docker Desktop: Must be installed and running on your host machine.'
'.Git: Used for repository management.'

## 2. Building the Docker Image
To build the image manually from the Dockerfile, open your terminal in the project root and run:


