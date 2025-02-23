from fastapi import FastAPI, HTTPException
from openai import AzureOpenAI
import azure.cognitiveservices.speech as speechsdk
import os
from dotenv import load_dotenv
from pydantic import BaseModel

# Load Azure credentials from .env
load_dotenv()

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware


# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8502"],  # Change this to ["http://localhost:8501"] for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Azure OpenAI setup
openai_client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2023-09-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
)

AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")  # Set your Azure model deployment name

# Azure Speech setup
SPEECH_KEY = os.getenv("AZURE_SPEECH_KEY")
SPEECH_REGION = os.getenv("AZURE_SPEECH_REGION")

@app.post("/speech-to-text/")
async def speech_to_text():
    """Convert speech input to text using Azure Speech-to-Text."""
    try:
        speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
        audio_config = speechsdk.AudioConfig(use_default_microphone=True)

        recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
        print("Listening...")

        result = recognizer.recognize_once()

        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            return {"text": result.text}
        else:
            raise HTTPException(status_code=400, detail="Speech recognition failed")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
class PromptRequest(BaseModel):
    prompt: str

class speachRequest(BaseModel):
    text: str

#hello
@app.post("/generate-response/")
async def generate_response(request: PromptRequest):
    """Generate AI response using Azure OpenAI."""
    try:
        response = openai_client.chat.completions.create(
            model=AZURE_OPENAI_DEPLOYMENT,  # Use your Azure model deployment name
            messages=[{"role": "user", "content": request.prompt}],
        )
        return {"response": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Azure OpenAI request failed: {str(e)}")

@app.post("/text-to-speech/")
async def text_to_speech(request: speachRequest):
    """Convert text to speech using Azure Speech-to-Text."""
    try:
        speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

        result = speech_synthesizer.speak_text_async(request.text).get()

        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            return {"message": "Speech synthesis successful"}
        else:
            raise HTTPException(status_code=400, detail="Speech synthesis failed")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
