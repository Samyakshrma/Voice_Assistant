


### **README.md**

# AI Assistant based on Azure & FastAPI Service

This is a FastAPI-based service that integrates with **Azure Cognitive Services Speech API** for speech-to-text and text-to-speech functionalities.

## 🚀 Features
- Speech-to-Text (STT) using Azure Speech API
- Text-to-Speech (TTS) conversion
- FastAPI backend for handling API requests
- Docker support for easy deployment

---

## 🛠 Setup Instructions

### 1️⃣ **Clone the Repository**
```sh
git clone <https://github.com/Samyakshrma/Voice_Assistant.git>
cd <assistant>
```

### 2️⃣ **Create a `.env` File**
Before running the application, create a `.env` file in the root directory and add your Azure credentials:
```
AZURE_OPENAI_KEY=<YOUR_KEY>
AZURE_OPENAI_ENDPOINT=<YOUR_ENDPOINT>
AZURE_SPEECH_KEY=<YOUR_KEY>
AZURE_SPEECH_REGION=<DEPLOYMENT_REGION>
AZURE_OPENAI_DEPLOYMENT=gpt-4
AZURE_OPENAI_MODEL=gpt-4

```


## 🔧 Running Locally

### **With Python (Without Docker)**
1️⃣ **Create a virtual environment (optional but recommended)**
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2️⃣ **Install dependencies**
```sh
pip install -r requirements.txt
```

3️⃣ **Run the FastAPI server**
```sh
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

4️⃣ Open your browser and go to:
```
http://localhost:8000/docs
```
to access the interactive API documentation.

---

## 🐳 Running with Docker

1️⃣ **Build the Docker image**
```sh
docker-compose up --build 
```


---

## 📡 API Endpoints

| Method | Endpoint         | Description |
|--------|----------------|-------------|
| `POST` | `/speech-to-text` | Convert speech to text |
| `POST` | `/text-to-speech` | Convert text to speech |

### **Example Request (Speech-to-Text)**
```sh
curl -X POST "http://localhost:8000/speech-to-text" -F "file=@audio.wav"
```

---

## ✅ Troubleshooting
- **SpeechConfig Error?** → Ensure `.env` is properly configured.
- **Audio Library Missing?** → If running manually, install `libasound2`:
  ```sh
  sudo apt-get install libasound2
  ```

---

## 📜 License
This project is licensed under the MIT License.

---

### 💡 Need Help?
Feel free to open an issue or reach out! 🚀
```


