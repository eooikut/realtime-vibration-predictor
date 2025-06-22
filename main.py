from influxdb import InfluxDBClient
import random
import time
from datetime import datetime

# Kết nối tới InfluxDB
client = InfluxDBClient(host='localhost', port=8086)
client.switch_database('vibration_db')  # Đảm bảo đã tạo trong CLI

# Vòng lặp gửi dữ liệu rung động
while True:
    vibration = round(random.uniform(1,3.9), 2)  # Độ rung ngẫu nhiên từ 0.1 đến 5.0g
    #vibration = round(random.uniform(4.5,5.5), 2)
    timestamp = datetime.utcnow().isoformat() + "Z"

    json_body = [
        {
            "measurement": "vibration",
            "tags": {
                "sensor": "vib001",
                "location": "steel_factory"
            },
            "time": timestamp,
            "fields": {
                "value": vibration
            }
        }
    ]

    client.write_points(json_body)
    print(f"Measured Vibration: {vibration}g")
    time.sleep(1)


