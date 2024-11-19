# JARVIS - Voice Assistant

This application is a robust voice assistant designed to run on the local machine, inspired by the JARVIS voice assistant from the Marvel Universe.

## Table of Contents

- [Features](#Features)
- [Advanced](#Advanced)
- [Tech-Stack](#Tech-Stack)
- [Screenshots](#Screenshots)
- [Installation](#Installation)
- [Usage](#Usage)

## Features
1. Provides intelligent responses to user inquiries through a chatbot interface
2. Opens websites seamlessly in the default browser
3. Initiates applications installed on the local machine
4. Plays videos directly from YouTube
5. Sends messages to contacts via WhatsApp or SMS
6. Makes phone calls through WhatsApp or from the mobile device

## Advanced
1. Utilizes facial authentication for secure access to the application
2. Listens for specific trigger phrases (hot words) to activate the voice assistant

## Tech-Stack
1. HTML, CSS and JavaScript for Frontend
2. SQLite for managing databases of contacts, websites, and installed software
3. Python modules:
   1. Hugging Face for the chatbot
   2. OpenCV for facial recognition
   3. SpeechRecognition for speech-to-text capabilities
   4. Pyttsx3 and playsound for text-to-speech synthesis
   5. OS for executing commands on the local machine
   6. Pvporcupine for hot words detection
   7. And many more like Pipes, Eel, PyWhatkit, PyAudio, Pyautogui, multiprocessing, subprocess, etc
4. VSCode for development requirements
5. Webcam and Windows OS for hardware requirements

## Screenshots

<p align="center">
  <img src="https://github.com/user-attachments/assets/eaddc716-9c72-412d-ba1a-553be4f4fe15" alt="Screenshot (189)" width="500"/>
   <img src="https://github.com/user-attachments/assets/c5128626-fe82-4495-a321-41ea0cabdf21" alt="Screenshot (187)" width="500"/>
   <img src="https://github.com/user-attachments/assets/3f66dbd3-d417-467b-b41f-66deb6e42bd0" alt="Screenshot (185)" width="500"/>
</p>

## Installation

Follow these steps to clone and set up the repository locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/SemalJohari/JARVIS-Voice-Assistant.git

2. Navigate to the project directory:
   ```bash
   cd JARVIS-Voice-Assistant

3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

## Usage

To run the project locally, start the development server or application using:
```bash
python main.py

