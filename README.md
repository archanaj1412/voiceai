# VoiceAI - AI-Powered Voice Processing Web Application

An advanced AI-powered voice processing system with speaker detection, transcription, translation, deepfake detection, and sign language JSON conversion.

## Features

### Core Capabilities
- **Intelligent Speaker Detection**: Accurately detects single or multiple speakers
- **Speaker-Attributed Transcription**: Clean, accurate speech-to-text for each speaker
- **Speaker Separation**: Isolates individual voices with noise reduction
- **Automatic Language Detection**: Detects 80+ languages
- **English Translation**: Automatic translation for non-English content
- **Emotion-Based Deepfake Detection**: Analyzes voice authenticity with confidence scores
- **Editable JSON for Sign Language**: Structured output for sign language avatar animation
- **Noise Removal & Audio Enhancement**: Professional audio cleanup

### Input Methods
1. Audio file upload
2. Microphone recording
3. Live audio streaming

### Output per Speaker
- Speaker label and clean audio player
- Detected language and original text
- English translation
- Emotion analysis
- Deepfake detection result
- Editable JSON output

## Tech Stack

### Frontend
- **React** + **Vite**: Fast, modern UI development
- **TailwindCSS**: Beautiful, responsive styling
- **Modern Gradients & Animations**: Impressive visual design

### Backend
- **Python**: Core processing engine
- **SpeechRecognition Libraries**:
  - **Whisper** (OpenAI): High-accuracy transcription
  - **Vosk**: Lightweight offline STT (80+ languages)
- **Speaker Diarization**: pyannote.audio 3.0 (industry SOTA)
- **Deepfake Detection**: Wav2Vec2 fine-tuned models
- **Language Detection**: langdetect / fastText
- **Translation**: LibreTranslate (self-hosted)
- **Audio Processing**: Librosa + FFmpeg

### Infrastructure
- **Database**: MongoDB (local)
- **Task Queue**: Celery + Redis (for large files)
- **Containerization**: Docker & Docker Compose
- **Deployment**: Ready for web hosting

## Performance Requirements
- ✅ Fast processing with optimized algorithms
- ✅ Smooth experience with real-time updates
- ✅ Accurate results across multiple speakers
- ✅ Zero lag with streaming capabilities
- ✅ Reliable live updates

## Installation & Setup

### Prerequisites
- Python 3.9+
- Node.js 16+
- Docker & Docker Compose (optional)

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

### Docker Setup
```bash
docker-compose up
```

## Project Structure
```
voiceai/
├── frontend/                 # React + Vite application
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── pages/           # Page components
│   │   ├── services/        # API services
│   │   └── styles/          # Tailwind config
│   └── package.json
├── backend/                 # Python Flask/FastAPI
│   ├── app.py              # Main application
│   ├── modules/
│   │   ├── transcription/  # Whisper + Vosk
│   │   ├── speaker_diarization/  # pyannote.audio
│   │   ├── deepfake_detection/   # Wav2Vec2
│   │   ├── translation/    # LibreTranslate
│   │   ├── language_detection/   # langdetect
│   │   └── audio_processing/     # Librosa + FFmpeg
│   └── requirements.txt
├── docker-compose.yml       # Container orchestration
└── README.md               # This file
```

## Live Demo
Coming soon - deployment details will be added after initial development.

## License
MIT

## Support & Contribution
For issues, feature requests, or contributions, please open an issue or pull request.
