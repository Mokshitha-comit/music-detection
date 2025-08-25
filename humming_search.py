import numpy as np
from feature_extraction import extract_deep_features

def match_humming(humming_path, model, tune_db):
    humming_features = extract_deep_features(humming_path, model)
    best_match, best_score = None, -1
    for tune in tune_db:
        tune_features = np.frombuffer(tune.features, dtype=np.float32)
        score = np.dot(humming_features, tune_features) / (np.linalg.norm(humming_features) * np.linalg.norm(tune_features))
        if score > best_score:
            best_score = score
            best_match = tune
    return best_match, best_score