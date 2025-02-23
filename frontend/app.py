import streamlit as st
import requests
import azure.cognitiveservices.speech as speechsdk
import os
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

# Azure Speech Service Configuration
SPEECH_KEY = os.getenv("AZURE_SPEECH_KEY")
SPEECH_REGION = os.getenv("AZURE_SPEECH_REGION")

# FastAPI Backend URL
BASE_URL = "http://127.0.0.1:8000"  # Update if deployed

# Initialize speech recognizer
speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
audio_config = speechsdk.AudioConfig(use_default_microphone=True)
recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

st.title("🎙️ AI Voice Assistant (Always Listening)")

# Function to listen continuously for wake word
def listen_for_wake_word():
    """Continuously listen for the wake word 'Agent'."""
    st.info("Listening for wake word: 'Agent'...")

    while True:
        result = recognizer.recognize_once()

        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            text = result.text.lower()
            print(f"Detected: {text}")

            if "agent" in text:
                st.success("Wake word detected! Entering conversation mode...")
                return start_conversation()

        time.sleep(1)  # Prevents CPU overload

# Function to start a continuous conversation
def start_conversation():
    """Start a conversation after detecting the wake word."""
    st.info("Conversation started. Say 'End conversation' to stop.")
    
    while True:
        user_command = capture_command()

        if user_command:
            if "end conversation" in user_command.lower():
                st.warning("Conversation ended. Returning to wake-word mode...")
                return listen_for_wake_word()

            st.write(f"📝 You said: **{user_command}**")

            ai_response = process_command(user_command)
            st.success(f"🤖 AI says: {ai_response}")

            speak(ai_response)

# Function to capture user command
def capture_command():
    """Captures user command during conversation."""
    st.info("Listening for your command...")

    result = recognizer.recognize_once()
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        return result.text
    return None

# Function to process command with LLM
def process_command(command):
    """Send command to LLM and get response."""
    response = requests.post(f"{BASE_URL}/generate-response/", json={"prompt": command})

    if response.status_code == 200:
        return response.json()["response"]
    else:
        return "I'm sorry, I couldn't process your request."

# Function to convert text to speech
def speak(text):
    """Convert AI response to speech."""
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
    synthesizer.speak_text_async(text).get()

# Start listening for wake word
if st.button("🎤 Start Always-Listening Mode"):
    listen_for_wake_word()
