# Website Review: Advanced Music Detection Using Tunes

---

## Overview

The website delivers a clean, modern interface for tune and music detection. Users can upload audio files (music or humming), run various analyses, and view detailed results including song identification, genre, mood, and tempo, with potential for visualization.

---

## User Experience & Design

**Strengths:**
- **Simple Onboarding:** Uploading audio or recording humming is intuitive.
- **Clear Actions:** Separate buttons for "Detect Tune", "Humming Search", and "Genre/Mood/Tempo".
- **Live Feedback:** Results display instantly after analysis.
- **Informative Output:** JSON panel gives all key info (matched tune, score, genre, mood, tempo).
- **Extensible:** Visualization area ready for spectrogram/chromagram addition.

**Areas for Improvement:**
- Add microphone recording (humming) directly in UI.
- Show top 3-5 matches, not just the top result.
- More engaging visualization (animated spectrogram, waveform).
- User authentication for saving tune history.
- Mobile-friendly layout and drag-and-drop upload.

---

## Functional Prototype (React)

Below is a fully functional React component you can use as your homepage.  
It works with your FastAPI backend at `/detect-tune/`, `/humming-search/`, and `/genre-mood-tempo/`.

```javascript name=frontend/src/App.js
import React, { useState } from 'react';

function App() {
  const [audioFile, setAudioFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => setAudioFile(e.target.files[0]);

  const handleSubmit = async (endpoint) => {
    if (!audioFile) {
      alert("Please select an audio file first!");
      return;
    }
    setLoading(true);
    const formData = new FormData();
    formData.append("file", audioFile);
    try {
      const response = await fetch(endpoint, {
        method: "POST",
        body: formData
      });
      const data = await response.json();
      setResult(data);
    } catch (err) {
      setResult({ error: "Failed to analyze audio. Is the backend running?" });
    }
    setLoading(false);
  };

  return (
    <div style={{
      maxWidth: 520,
      margin: "40px auto",
      padding: "32px",
      borderRadius: "16px",
      boxShadow: "0 0 32px rgba(0,0,0,0.08)",
      background: "#fff",
      fontFamily: "Segoe UI, Arial, sans-serif"
    }}>
      <h1 style={{ color: "#2a4d69" }}>Advanced Music Detection Using Tunes</h1>
      <hr />
      <div style={{ marginBottom: 20 }}>
        <input
          type="file"
          accept="audio/*"
          onChange={handleFileChange}
          style={{ marginRight: 10 }}
        />
        {/* Extension: Add microphone recording button here */}
      </div>
      <div style={{ marginBottom: 20 }}>
        <button
          onClick={() => handleSubmit("/detect-tune/")}
          style={{ marginRight: 10 }}
          disabled={loading}
        >
          Detect Tune
        </button>
        <button
          onClick={() => handleSubmit("/humming-search/")}
          style={{ marginRight: 10 }}
          disabled={loading}
        >
          Humming Search
        </button>
        <button
          onClick={() => handleSubmit("/genre-mood-tempo/")}
          disabled={loading}
        >
          Genre/Mood/Tempo
        </button>
      </div>
      {loading && <div style={{ color: "#49708a" }}>Analyzing audio...</div>}
      {result && (
        <div style={{
          border: "1px solid #49708a",
          borderRadius: "8px",
          background: "#f4faff",
          padding: "12px",
          marginTop: 20
        }}>
          <h2 style={{ color: "#2a4d69" }}>Result:</h2>
          <pre style={{ fontSize: 16 }}>
            {JSON.stringify(result, null, 2)}
          </pre>
        </div>
      )}
      {/* Visualization placeholder */}
      {/* <SpectrogramPlot audioFile={audioFile} /> */}
      <div style={{ marginTop: 30, fontSize: 14, color: "#888" }}>
        <em>
          Try uploading a music file or humming your favorite tune!
          <br />
          <b>Tip:</b> Backend should be running at <code>localhost:8000</code>.
        </em>
      </div>
    </div>
  );
}

export default App;
```

---

## Sample Result Panel

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

## Visualization (Future Extension)

- Spectrogram or chromagram appears below the result, visualizing frequency and pitch over time.
- Optionally, show waveform or melody contour.

---

## Recommendations

- Add microphone support for direct humming input.
- Display top matches with confidence scores.
- Animate visualizations for a richer experience.
- Allow users to save and share results.
- Make layout mobile-friendly for on-the-go music detection.

---

**This prototype is ready for user testing and further extension. You can deploy it locally or online, connect it to your backend, and start experimenting with real audio files!**