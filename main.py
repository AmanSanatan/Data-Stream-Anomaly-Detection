from zscore_anomaly_detection import ZScoreAnomalyDetector
from visulatisation import visualize_data_stream
if __name__ == "__main__":
    # Initialize the Z-score anomaly detector
    detector = ZScoreAnomalyDetector(window_size=50, threshold=3)
    # Run visualization calling the visualize function 
    visualize_data_stream(detector, stream_length=1000)
