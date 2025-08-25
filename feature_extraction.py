import librosa
import numpy as np
import torch

def extract_deep_features(audio_path, model=None):
    y, sr = librosa.load(audio_path, sr=None)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    mel = librosa.feature.melspectrogram(y=y, sr=sr)
    features = np.concatenate([np.mean(mfcc, axis=1), np.mean(chroma, axis=1), np.mean(mel, axis=1)])
    if model is not None:
        features_tensor = torch.tensor(features, dtype=torch.float32).unsqueeze(0)
        deep_features = model(features_tensor).detach().numpy().flatten()
        return deep_features
    return features

def plot_spectrogram(audio_path):
    import matplotlib.pyplot as plt
    y, sr = librosa.load(audio_path)
    S = librosa.feature.melspectrogram(y, sr=sr)
    S_dB = librosa.power_to_db(S, ref=np.max)
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(S_dB, sr=sr, x_axis='time', y_axis='mel')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Mel-frequency spectrogram')
    plt.tight_layout()
    plt.show()