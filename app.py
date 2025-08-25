from fastapi import FastAPI, UploadFile, File
from feature_extraction import extract_deep_features
from humming_search import match_humming
from genre_mood_tempo import detect_genre, detect_mood, detect_tempo
from database import get_all_tunes
import torch
import numpy as np

app = FastAPI()

# Load trained model (replace with proper loading in real use)
model = torch.load("model/music_cnn.pt", map_location=torch.device('cpu'))
model.eval()

@app.post("/detect-tune/")
async def detect_tune(file: UploadFile = File(...)):
    contents = await file.read()
    temp_audio = "temp.wav"
    with open(temp_audio, "wb") as f:
        f.write(contents)
    input_features = extract_deep_features(temp_audio, model)
    tunes = get_all_tunes()
    best_match, best_score = None, -1
    for tune in tunes:
        tune_features = np.frombuffer(tune.features, dtype=np.float32)
        score = np.dot(input_features, tune_features) / (np.linalg.norm(input_features) * np.linalg.norm(tune_features))
        if score > best_score:
            best_score = score
            best_match = tune
    return {
        "match": best_match.name,
        "score": best_score,
        "genre": best_match.genre,
        "mood": best_match.mood,
        "tempo": best_match.tempo
    }

@app.post("/humming-search/")
async def humming_search(file: UploadFile = File(...)):
    contents = await file.read()
    temp_audio = "temp_hum.wav"
    with open(temp_audio, "wb") as f:
        f.write(contents)
    tunes = get_all_tunes()
    best_match, best_score = match_humming(temp_audio, model, tunes)
    return {
        "match": best_match.name,
        "score": best_score,
        "genre": best_match.genre,
        "mood": best_match.mood,
        "tempo": best_match.tempo
    }

@app.post("/genre-mood-tempo/")
async def genre_mood_tempo(file: UploadFile = File(...)):
    contents = await file.read()
    temp_audio = "temp_gmt.wav"
    with open(temp_audio, "wb") as f:
        f.write(contents)
    genre = detect_genre(temp_audio, model)
    mood = detect_mood(temp_audio)
    tempo = detect_tempo(temp_audio)
    return {"genre": genre, "mood": mood, "tempo": tempo}