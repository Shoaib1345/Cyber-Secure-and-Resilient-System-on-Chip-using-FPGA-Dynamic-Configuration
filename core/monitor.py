"""
monitor.py
Telemetry monitor with simple model.
Tries to use IsolationForest (sklearn) if available, otherwise falls back to z-score checks.
"""
import time
import numpy as np

try:
    from sklearn.ensemble import IsolationForest
    import joblib
    SKLEARN_AVAILABLE = True
except Exception:
    SKLEARN_AVAILABLE = False

class TelemetryMonitor:
    def __init__(self):
        self.model = None
        self.keys = None

    def train_baseline(self, samples, use_isolationforest=True):
        """
        samples: list of telemetry dicts with same keys.
        """
        X = self._to_matrix(samples)
        if use_isolationforest and SKLEARN_AVAILABLE:
            self.model = IsolationForest(contamination=0.01, random_state=42)
            self.model.fit(X)
            return "Trained IsolationForest model"
        else:
            # store mean & std for z-score method
            self.keys = sorted(samples[0].keys())
            arr = np.array(X)
            self.mean = arr.mean(axis=0)
            self.std = arr.std(axis=0)
            return "Trained z-score baseline"

    def is_anomaly(self, telemetry):
        """
        telemetry: dict of same keys
        returns True/False
        """
        keys = sorted(telemetry.keys())
        X = np.array([telemetry[k] for k in keys]).reshape(1, -1)
        if self.model is not None:
            pred = self.model.predict(X)  # -1 anomaly, 1 normal
            return pred[0] == -1
        else:
            # z-score method
            z = (X - self.mean) / (self.std + 1e-9)
            # flag if any dimension has z>3
            return (np.abs(z) > 3.0).any()

    def _to_matrix(self, samples):
        keys = sorted(samples[0].keys())
        mat = []
        for s in samples:
            mat.append([s[k] for k in keys])
        return mat
