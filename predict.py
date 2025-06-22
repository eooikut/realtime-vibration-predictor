from influxdb import InfluxDBClient
import numpy as np
from tensorflow.keras.models import load_model
import time

# Kết nối InfluxDB
client = InfluxDBClient(host='localhost', port=8086, database='vibration_db')

# Load mô hình đã huấn luyện
model = load_model("cnn_vibration_model.h5")

WINDOW_SIZE = 20

def get_latest_window():
    query = f"SELECT value FROM vibration ORDER BY time DESC LIMIT {WINDOW_SIZE}"
    result = client.query(query)
    points = list(result.get_points())
    if len(points) < WINDOW_SIZE:
        return None
    values = [p['value'] for p in reversed(points)]
    return np.array(values).reshape((1, WINDOW_SIZE, 1))

status_map = {0: "🟢 Bình thường", 1: "🟠 Trung bình", 2: "🔴 Nguy hiểm"}

while True:
    window = get_latest_window()
    if window is not None:
        prediction = model.predict(window)
        label = np.argmax(prediction)
        print(f"Dự đoán: {status_map[label]} - Xác suất: {prediction[0][label]:.2f}")
    else:
        print("Chưa đủ dữ liệu để dự đoán.")
    time.sleep(2)
