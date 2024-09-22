from collections import deque
import numpy as np
class ZScoreAnomalyDetector:
    def __init__(self, window_size=50, threshold=3):
        self.window_size = window_size
        self.threshold = threshold
        self.data_window = deque(maxlen=window_size)
    
    def detect_anomaly(self, new_value):
        # Add new value to window
        self.data_window.append(new_value)
        
        # Calculate mean and standard deviation from the window
        if len(self.data_window) < self.window_size:
            return False  # Not enough data to detect anomalies
        
        mean = np.mean(self.data_window)
        std_dev = np.std(self.data_window)
        
        # Calculate Z-score
        z_score = (new_value - mean) / (std_dev if std_dev > 0 else 1)
        
        # Check if Z-score exceeds the threshold
        if np.abs(z_score) > self.threshold:
            return True  # Anomaly detected
        
        return False
