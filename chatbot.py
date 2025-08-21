
import json
import os
import torch
from transformers import pipeline
from TTS.api import TTS
import soundfile as sf
from IPython.display import Audio, display

# 1. Setup: Models and Paths
def setup():
    # Check for GPU
    device = "cuda" if torch.cuda.is_available() else "cpu"

    # STT (Whisper)
    stt_pipeline = pipeline("automatic-speech-recognition", model="openai/whisper-small", device=device)

    # TTS (Coqui TTS)
    tts_model_name = "tts_models/en/ljspeech/tacotron2-DDC"
    tts = TTS(model_name=tts_model_name, progress_bar=False).to(device)

    # FAQ
    with open("faq.json", "r") as f:
        faq_data = json.load(f)

    return stt_pipeline, tts, faq_data, device

# 2. Speech-to-Text (STT)
def speech_to_text(audio_path, stt_pipeline):
    if not os.path.exists(audio_path):
        return "Error: Audio file not found."
    try:
        transcription = stt_pipeline(audio_path)
        return transcription["text"]
    except Exception as e:
        return f"Error during STT: {e}"

# 3. Text-to-Speech (TTS)
def text_to_speech(text, tts_model, output_path="response.wav"):
    try:
        tts_model.tts_to_file(text=text, file_path=output_path)
        return output_path
    except Exception as e:
        return f"Error during TTS: {e}"

# 4. Chatbot Logic
def chatbot_logic(user_input, faq_data):
    # Check FAQ first
    if user_input in faq_data:
        return faq_data[user_input]

    # Web Search (if not in FAQ)
    # For this example, we'll simulate a web search prompt.
    # In a real scenario, you would integrate a search API here.
    if "search for" in user_input.lower():
        query = user_input.lower().replace("search for", "").strip()
        # This is where you would call your web search tool.
        # For now, we'll just return a placeholder response.
        return f"Searching the web for: '{query}'. I'll get back to you with the results."

    # Default response
    return "I'm not sure how to answer that. You can ask me a question from the FAQ or ask me to 'search for' something."

# 5. Main Function
def main():
    print("Setting up the chatbot...")
    stt_pipeline, tts, faq_data, device = setup()
    print("Chatbot is ready. Please provide the path to your audio file.")

    while True:
        audio_path = input("Audio file path (or 'quit' to exit): ")
        if audio_path.lower() == 'quit':
            break

        # STT
        user_text = speech_to_text(audio_path, stt_pipeline)
        print(f"You said: {user_text}")

        # Chatbot Logic
        response_text = chatbot_logic(user_text, faq_data)
        print(f"Chatbot says: {response_text}")

        # TTS
        output_audio_path = text_to_speech(response_text, tts)
        print(f"Response audio saved to: {output_audio_path}")
        display(Audio(output_audio_path, autoplay=True))

if __name__ == "__main__":
    main()
