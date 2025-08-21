# Voice-to-Voice Chatbot

This project is a voice-to-voice chatbot that takes an audio file as input, transcribes the speech to text, processes the text to generate a response, and then converts the response back to speech in an audio file.

## How it Works

The chatbot operates in the following sequence:

1.  **Speech-to-Text (STT):** The user provides an audio file. The chatbot uses the `openai/whisper-small` model to transcribe the audio into text.
2.  **Chatbot Logic:** The transcribed text is processed by the chatbot's logic:
    *   It first checks if the input is a question present in the `faq.json` file. If a match is found, it returns the corresponding answer.
    *   If the input is not in the FAQ, it checks for the phrase "search for". If found, it simulates a web search with the subsequent query.
    *   If neither of the above conditions is met, it returns a default response.
3.  **Text-to-Speech (TTS):** The chatbot's text response is converted back into speech using the `tts_models/en/ljspeech/tacotron2-DDC` model from Coqui TTS.
4.  **Audio Output:** The generated speech is saved as `response.wav` and played back to the user.

## Features

*   Voice-based interaction
*   Speech-to-text transcription using Whisper
*   Text-to-speech synthesis using Coqui TTS
*   FAQ-based question answering
*   Simulated web search functionality

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd Module_7_Project_voice_to_voice_cahtbot
    ```

2.  **Create and activate a virtual environment:**
    *   On Windows:
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```
    *   On macOS/Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the chatbot, execute the `chatbot.py` script:

```bash
python chatbot.py
```

The script will prompt you to enter the path to an audio file. After processing, the chatbot's response will be played and saved as `response.wav`.

## Project Structure

*   `chatbot.py`: The main script containing the chatbot's logic.
*   `requirements.txt`: A list of the Python packages required for the project.
*   `faq.json`: A JSON file containing frequently asked questions and their answers.
*   `README.md`: This file.