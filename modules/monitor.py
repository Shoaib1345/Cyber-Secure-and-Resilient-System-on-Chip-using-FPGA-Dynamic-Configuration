# modules/monitor.py
import numpy as np

def detect_anomaly(values):
    """Detect anomalies using z-score method."""
    if len(values) < 3:
        return False
    mean, std = np.mean(values), np.std(values)
    latest = values[-1]
    return abs(latest - mean) > 2.5 * std
