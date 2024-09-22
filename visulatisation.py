import matplotlib.pyplot as plt
from data_stream_simulator import data_stream_simulator
def visualize_data_stream(detector, stream_length=1000):
    """
    Visualize the data stream in real time, marking detected anomalies.
    detector: The anomaly detection algorithm instance.
    stream_length: Number of data points to process.
    """
    plt.ion()  # Enable interactive mode
    fig, ax = plt.subplots()
    data_points, anomaly_points = [], []
    
    stream = data_stream_simulator(stream_length)
    for i, point in enumerate(stream):
        is_anomaly = detector.detect_anomaly(point)
        data_points.append(point)
        
        # Mark anomalies in red
        if is_anomaly:
            anomaly_points.append(i)
        
        # Update plot every 10 points for efficiency
        if i % 10 == 0:
            ax.clear()
            ax.plot(data_points, label='Data Stream')
            ax.scatter(anomaly_points, [data_points[i] for i in anomaly_points], color='red', label='Anomalies')
            ax.legend()
            plt.draw()
            plt.pause(0.01)

    plt.ioff()
    plt.show()
