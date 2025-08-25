import librosa
import numpy as np

def detect_genre(audio_path, model):
    features = extract_deep_features(audio_path, model)
    genre_probs = model(torch.tensor(features, dtype=torch.float32).unsqueeze(0))
    genre_idx = np.argmax(genre_probs.detach().numpy())
    genres = ["Pop", "Rock", "Jazz", "Classical", "HipHop"]
    return genres[genre_idx]

def detect_mood(audio_path):
    y, sr = librosa.load(audio_path, sr=None)
    tempo, _ = librosa.beat.beat_track(y, sr=sr)
    rms = np.mean(librosa.feature.rms(y=y))
    if tempo > 120 and rms > 0.05:
        return "Energetic"
    elif tempo < 80:
        return "Calm"
    else:
        return "Neutral"

def detect_tempo(audio_path):
    y, sr = librosa.load(audio_path, sr=None)
    tempo, _ = librosa.beat.beat_track(y, sr=sr)
    return tempo