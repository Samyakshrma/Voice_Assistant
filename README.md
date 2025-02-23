


### **README.md**
```markdown
# Azure Speech API FastAPI Service

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
git clone <your-repo-url>
cd <your-project-folder>
```

### 2️⃣ **Create a `.env` File**
Before running the application, create a `.env` file in the root directory and add your Azure credentials:
```
SPEECH_KEY=your-azure-speech-key
SPEECH_REGION=your-azure-region
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
docker build -t my_speech_app .
```

2️⃣ **Run the container**
```sh
docker run --env-file .env -p 8000:8000 my_speech_app
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

---

### **What This README Covers**
✅ **Project Overview**  
✅ **Setup Instructions**  
✅ **Local & Docker Run Commands**  
✅ **API Endpoints & Example Requests**  
✅ **Troubleshooting Guide**  

Let me know if you need any modifications! 🚀
