# Website Preview: Advanced Music Detection Using Tunes

---

## Home Page

**Header:**  
> Advanced Music Detection Using Tunes

---

**Upload Section:**  
- [Choose Audio File] (audio or humming)
- [Record Humming] (microphone input - optional extension)

**Actions:**  
- [Detect Tune] — Identify the song/tune from your audio
- [Humming Search] — Find a song by your humming/melody
- [Genre/Mood/Tempo] — Analyze the audio for genre, mood, and tempo

---

**Result Panel:**  
Displays JSON-style output or a formatted result:

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

**Visualization:**  
- Spectrogram or chromagram visualization of your uploaded audio
- Shows frequency/time plot to help you “see” the tune

---

## Example User Flow

1. User visits the page and sees the upload and action panel.
2. Uploads an audio file or records humming.
3. Clicks "Detect Tune" or "Humming Search".
4. Result appears: matching song/tune, genre, mood, tempo, similarity score.
5. Spectrogram visualization is displayed below the result.

---

## Sample UI Mockup

```
+------------------------------------------------+
| Advanced Music Detection Using Tunes           |
+------------------------------------------------+
| [ Choose Audio File ]   [ Record Humming ]     |
+------------------------------------------------+
| [Detect Tune] [Humming Search] [Genre/Mood/Tempo] |
+------------------------------------------------+
| Result:                                        |
| {                                              |
|   "match": "tune1.wav",                        |
|   "score": 0.92,                               |
|   "genre": "Rock",                             |
|   "mood": "Energetic",                         |
|   "tempo": 135.5                               |
| }                                              |
+------------------------------------------------+
| [Spectrogram Visualization]                    |
+------------------------------------------------+
```

---

## Example React Component

```javascript name=frontend/src/App.js
import React, { useState } from 'react';

function App() {
  const [audioFile, setAudioFile] = useState(null);
  const [result, setResult] = useState(null);

  const handleFileChange = (e) => setAudioFile(e.target.files[0]);
  const handleSubmit = async (endpoint) => {
    const formData = new FormData();
    formData.append("file", audioFile);
    const response = await fetch(endpoint, {
      method: "POST",
      body: formData
    });
    const data = await response.json();
    setResult(data);
  };

  return (
    <div style={{ maxWidth: 600, margin: "auto", padding: 20 }}>
      <h1>Advanced Music Detection Using Tunes</h1>
      <input type="file" accept="audio/*" onChange={handleFileChange} />
      <button onClick={() => handleSubmit("/detect-tune/")}>Detect Tune</button>
      <button onClick={() => handleSubmit("/humming-search/")}>Humming Search</button>
      <button onClick={() => handleSubmit("/genre-mood-tempo/")}>Genre/Mood/Tempo</button>
      {result && (
        <div>
          <h2>Result:</h2>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
      {/* Add visualization here, e.g. <SpectrogramPlot audioFile={audioFile} /> */}
    </div>
  );
}

export default App;
```

---

## Visualization Example

- A plot appears under the result panel:
    - **Spectrogram**: Shows frequency vs time for uploaded audio.
    - **Chromagram**: Shows pitch classes present in the tune.

---

## Extensions

- Add microphone recording for humming input.
- Animate spectrogram during playback.
- Show a list of top 5 matches with links.
- Allow users to share results.

---

This preview demonstrates the complete user experience for your music detection web app, including interactive analysis, tune identification, and audio visualization.