# Preview: Advanced Music Detection Using Tunes

## System Architecture

1. **Frontend (React)**
   - Simple UI for uploading audio or humming recordings.
   - Buttons for tune detection, genre/mood/tempo analysis, and melody (humming) search.
2. **Backend (FastAPI)**
   - REST endpoints for audio analysis.
   - Connects to a database storing tune features and metadata.
   - Uses a trained deep learning model for feature extraction and classification.
3. **Database (SQLite/SQLAlchemy)**
   - Stores tune features, genre, mood, tempo, and audio paths.
4. **Deep Learning Model (PyTorch)**
   - Classifies tunes and extracts advanced features.
5. **Feature Extraction (Librosa)**
   - Processes audio files for MFCC, chroma, tempo, and other features.
6. **Visualization**
   - Spectrogram plotting for user feedback.

---

## Main Workflow

1. **User uploads audio/humming via frontend.**
2. **Audio sent to backend API.**
3. **Feature extraction (Librosa + Deep Model).**
4. **Tune matching/classification against DB.**
5. **Genre/mood/tempo detected.**
6. **Results returned to frontend and displayed.**

---

## Key Code Snippets

### Frontend (React)

```javascript
<input type="file" accept="audio/*" onChange={handleFileChange} />
<button onClick={() => handleSubmit("/detect-tune/")}>Detect Tune</button>
<button onClick={() => handleSubmit("/humming-search/")}>Humming Search</button>
<button onClick={() => handleSubmit("/genre-mood-tempo/")}>Genre/Mood/Tempo</button>
<pre>{result && JSON.stringify(result, null, 2)}</pre>
```

---

### Backend API (FastAPI)

```python
@app.post("/detect-tune/")
async def detect_tune(file: UploadFile = File(...)):
    # Extract features, match tune, respond with result
    ...

@app.post("/humming-search/")
async def humming_search(file: UploadFile = File(...)):
    # Match humming melody to database
    ...

@app.post("/genre-mood-tempo/")
async def genre_mood_tempo(file: UploadFile = File(...)):
    # Return genre, mood, and tempo
    ...
```

---

### Feature Extraction

```python
def extract_deep_features(audio_path, model):
    y, sr = librosa.load(audio_path, sr=None)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    # ... chroma, mel, etc.
    features = np.concatenate([...])
    deep_features = model(torch.tensor(features, dtype=torch.float32).unsqueeze(0)).detach().numpy().flatten()
    return deep_features
```

---

### Database Model

```python
class Tune(Base):
    __tablename__ = 'tunes'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    features = Column(LargeBinary)
    genre = Column(String)
    mood = Column(String)
    path = Column(String)
    tempo = Column(Float)
```

---

### Visualization

```python
def plot_spectrogram(audio_path):
    y, sr = librosa.load(audio_path)
    S = librosa.feature.melspectrogram(y, sr=sr)
    S_dB = librosa.power_to_db(S, ref=np.max)
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(S_dB, sr=sr, x_axis='time', y_axis='mel')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Mel-frequency spectrogram')
    plt.tight_layout()
    plt.show()
```

---

## Example Result

```json
{
  "match": "tune1.wav",
  "score": 0.92,
  "genre": "Rock",
  "mood": "Energetic",
  "tempo": 135.5
}
```

---

## Next Steps

- Add real tunes to the database for testing.
- Train your model with more audio data.
- Extend the frontend for live recording.
- Integrate more advanced visualizations.
