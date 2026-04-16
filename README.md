# Bangladeshi Taka Detection API

## Project Structure
The following is the structure of the project:

```plaintext
TakaDetection/
├── src/
│   ├── app.py
│   ├── utils.py
│   └── models/
│       └── model.h5
├── requirements.txt
└── README.md
```

## Installation Instructions
To set up the Bangladeshi Taka Detection API, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Md-Musfiq-Hossain/TakaDetection.git
   cd TakaDetection
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## API Usage
To use the API, follow the steps below:

1. Start the server:
   ```bash
   python src/app.py
   ```
2. Send a POST request to the API endpoint with the image of the Taka:
   ```http
   POST /detect
   Content-Type: multipart/form-data
   ```
3. The response will include:
   - `status`: indicates success or failure
   - `message`: additional information
   - `result`: detected denomination if successful

Example of a successful response:
```json
{
  "status": "success",
  "message": "Denomination detected.",
  "result": "100 Taka"
}
```

## Troubleshooting Information
- If you encounter any issues, please check the following:
  - Ensure the required libraries are installed as listed in `requirements.txt`.
  - Check if the server is running on the correct port.
  - Verify that the image provided is valid and clear.

For further assistance, you can raise an issue in the GitHub repository or contact support.