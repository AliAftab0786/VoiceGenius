# 🎙️ VoiceGenius: Your AI-Powered Conversational Companion 🧠

## 🌟 Introduction

Welcome to VoiceGenius, the cutting-edge voice-to-text-to-AI-to-speech application that brings your conversations with artificial intelligence to life! This innovative script combines the power of speech recognition, natural language processing, and text-to-speech technology to create a seamless, hands-free AI interaction experience.

## 🚀 Features

- 🎤 **Speech Recognition**: Captures your voice input with precision
- 🧠 **AI Processing**: Utilizes the Gemini 1.5 Flash model for lightning-fast responses
- 🔊 **Text-to-Speech Output**: Speaks the AI's response aloud
- 🔧 **Ambient Noise Adjustment**: Optimizes audio capture in various environments
- ⏱️ **Customizable Timeouts**: Flexible listening durations for your convenience

## 🛠️ Prerequisites

- Python 3.x
- `speech_recognition` library
- `requests` library
- Access to Google Speech Recognition API
- Gemini API key

## 🔧 Setup

1. Clone this repository
2. Install required dependencies: `pip install -r requirements.txt`
3. Replace `'Use-your-gemini-API-key'` with your actual Gemini API key
4. Ensure your system has a working microphone and speakers

## 🎭 Usage

Run the script and start talking! VoiceGenius will:
1. Listen to your speech
2. Convert it to text
3. Send it to the Gemini AI for processing
4. Speak the AI's response back to you

## 🌈 Customization

- Modify the `voice` parameter in the `speak()` function to change the voice output
- Adjust timeout and phrase limits in `recognize_speech_from_mic()` for different use cases

## 🚨 Troubleshooting

- If you encounter audio-related issues, check your system's microphone settings
- For API errors, verify your internet connection and API key validity

## 🤝 Contributing

We welcome contributions! Feel free to submit pull requests or open issues for bugs and feature requests.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## 🙏 Acknowledgments

- Google Speech Recognition for powering our voice-to-text functionality
- Gemini AI for providing the brains behind our responses
- The open-source community for inspiration and support

---

Happy talking with VoiceGenius! Let your voice be the key to unlocking AI's potential. 🗝️🤖