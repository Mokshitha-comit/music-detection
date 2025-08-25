import argparse
import os
import numpy as np
from feature_extraction import extract_features

TUNES_PATH = "tunes_database/example_tunes/"

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def load_database_features():
    database = {}
    for fname in os.listdir(TUNES_PATH):
        if fname.endswith(".wav"):
            path = os.path.join(TUNES_PATH, fname)
            features = extract_features(path)
            database[fname] = features
    return database

def match_tune(input_features, database_features):
    best_match = None
    highest_score = -1
    for fname, features in database_features.items():
        score = cosine_similarity(input_features['mfcc'], features['mfcc'])
        if score > highest_score:
            highest_score = score
            best_match = fname
    return best_match, highest_score

def main(audio_file):
    input_features = extract_features(audio_file)
    database_features = load_database_features()
    match, score = match_tune(input_features, database_features)
    print(f"Best match: {match} (similarity: {score:.2f})")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Detect music tune from an audio file.")
    parser.add_argument("--input", type=str, required=True, help="Path to the input audio file")
    args = parser.parse_args()
    main(args.input)