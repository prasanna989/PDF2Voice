📖 EchoPages – PDF to Speech Converter

Turn your PDFs into audio effortlessly!
EchoPages reads any PDF document and converts it into a natural-sounding voice narration. Perfect for multitaskers, visually impaired users, or anyone who prefers listening over reading.

🎯 Features

Converts any multi-page PDF into an audio file (MP3)

Works offline on Windows, Mac, and Linux

Saves audio in a dedicated output/ folder

Easy to use — just place your PDFs in samples/

🛠️ Installation
1. Clone the repository
git clone https://github.com/your-username/echo-pages.git
cd echo-pages

2. Install dependencies
pip install -r requirements.txt


Note for Linux / Colab users:
You may need to install the espeak-ng TTS engine manually:

sudo apt-get update && sudo apt-get install espeak-ng

🚀 Usage

Place your PDF inside the samples/ folder (example: samples/example.pdf).

Run the program:

python main.py


The generated audio will appear in the output/ folder as output.mp3.


🎨 Customization

Change the output file name or folder in main.py.

Tweak pyttsx3 voice properties (rate, volume, male/female voice).

engine = pyttsx3.init()
engine.setProperty('rate', 150)    # Speed of speech
engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

🌟 Why EchoPages?

Saves reading time by converting text to speech

Makes PDFs accessible to everyone

Works offline, no cloud dependency

Lightweight, simple, and easy to extend

💡 Future Enhancements

Add multiple language support

Support voice selection (male/female)

Web interface for uploading PDFs online
