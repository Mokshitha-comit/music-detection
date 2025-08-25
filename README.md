# Advanced Music Detection Using Tunes

## Overview
This project detects music and tunes from audio, humming, or singing. It uses deep learning (CNN/RNN), stores features in a database, exposes a REST API, and provides a web frontend for user interaction, including real-time search and visualization.

## Features
- Deep learning for feature extraction and tune classification
- Real-time humming/singing melody search
- Genre, mood, and tempo detection
- REST API and web frontend
- Spectrogram and similarity visualization
- Database-backed tune library

## Getting Started

1. **Install dependencies**:  
   `pip install -r requirements.txt`
2. **Start backend**:  
   `uvicorn app:app --reload`
3. **Start frontend**:  
   `cd frontend && npm install && npm start`
4. **Train model**:  
   `python model/train_model.py`

## Directory Structure

```
advanced-music-detection/
├── app.py                  # FastAPI backend
├── model/
│   ├── train_model.py      # Deep learning training script
│   └── music_cnn.pt        # Trained model
├── feature_extraction.py
├── humming_search.py
├── genre_mood_tempo.py
├── database.py
├── tunes_database/
│   └── example_tunes/
├── frontend/
│   ├── src/
│   │   └── App.js
│   └── package.json
├── requirements.txt
└── README.md
```