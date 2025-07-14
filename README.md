# JARVIS – Voice Assistant using Python 🎙️🤖

This is a voice-controlled virtual assistant built using Python. It can:
- Recognize speech
- Open websites like Google, YouTube, Facebook
- Play music from a custom library
- Fetch and read news
- Respond to custom queries using OpenAI GPT-4

## 🎯 Features

- 🎤 **Voice Activation** with the wake word **"Jarvis"**
- 🔊 **Text-to-Speech** responses using `pyttsx3`
- 🌐 **Open Websites** like Google, YouTube, Facebook via voice
- 🎵 **Play Music** from a pre-defined library
- 📰 **Fetch Latest News** using NewsAPI
- 🤖 **AI Responses** via OpenAI GPT API
- 🗣️ **Speech Recognition** powered by Google API

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/jarvis-voice-assistant.git
cd jarvis-voice-assistant
```

### 2. Create and Activate Virtual Environment

```bash

python -m venv .venv
.\.venv\Scripts\activate
```

### 3. Install Requirements

```bash

pip install -r requirements.txt
```

### 4. Add API Keys in .env

Create a .env file in the root directory:

```ini

new_api_key=YOUR_NEWS_API_KEY
openAi_api_key=YOUR_OPENAI_API_KEY
```

🚀 Usage
Once setup is done, simply run:

```bash

python main.py
```

Then say "Jarvis" to activate the assistant and give further voice commands like:

"Open Google"

"Play [song name]"

"Tell me the news"

"What is the capital of France?"


