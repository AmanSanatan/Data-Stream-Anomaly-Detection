import numpy as np
import time

def data_stream_simulator(stream_length=1000, anomaly_rate=0.01):
    """
    Simulate a data stream with periodic pattern, noise, and occasional anomalies.
    stream_length: Total number of data points in the stream.
    anomaly_rate: Probability of introducing an anomaly in the stream.
    Yields real-time data points.
    """
    t = 0
    while t < stream_length:
        # Simulate seasonal data (sinusoidal pattern)
        seasonal_component = 10 * np.sin(0.2 * t) 
        
        # Add random noise
        noise_component = np.random.normal(0, 1)
        
        # Introduce anomalies randomly
        anomaly = 0
        if np.random.rand() < anomaly_rate:
            anomaly = np.random.choice([20, -20])  # Large spike or drop
        
        # Combine the components
        value = seasonal_component + noise_component + anomaly
        yield value
        
        # Simulate real-time streaming (optional delay for visualization)
        time.sleep(0.01)  # Stream 100 data points per second
        t += 1
