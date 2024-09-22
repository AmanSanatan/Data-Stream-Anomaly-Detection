from data_stream_simulator import data_stream_simulator  # Import from data_simulator.py

def stream_anomaly_detection(detector, stream_length=1000):
    """
    Stream the data, applying the anomaly detection in real time.
    detector: The anomaly detection algorithm instance.
    stream_length: Number of data points to process.
    """
    stream = data_stream_simulator(stream_length)
    for point in stream:
        is_anomaly = detector.detect_anomaly(point)
        status = "Anomaly" if is_anomaly else "Normal"
        print(f"Data Point: {point:.2f}, Status: {status}")
