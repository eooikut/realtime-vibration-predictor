from influxdb import InfluxDBClient
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

client = InfluxDBClient(host='localhost', port=8086, database='vibration_db')

# 2. Lấy dữ liệu
query = "SELECT value FROM vibration ORDER BY time ASC LIMIT 10000"
result = client.query(query)
points = list(result.get_points())

df = pd.DataFrame(points)
df['time'] = pd.to_datetime(df['time'])
df = df.dropna()
print(f"Data points retrieved: {len(df)}")
# 3. Chia thành các cửa sổ (window) để feed vào CNN
WINDOW_SIZE = 20

X = []
y = []

for i in range(len(df) - WINDOW_SIZE):
    window = df['value'].iloc[i:i+WINDOW_SIZE].values
    label = np.mean(window)
    if label < 2:
        label = 0
    elif label < 4:
        label = 1
    else:
        label = 2

    X.append(window)
    y.append(label)

X = np.array(X)
y = np.array(y)

# 4. Định dạng cho CNN (reshape)
X = X.reshape((X.shape[0], X.shape[1], 1))  # [samples, time_steps, features]

# 5. Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. Tạo mô hình CNN
model = models.Sequential([
    layers.Conv1D(32, kernel_size=3, activation='relu', input_shape=(WINDOW_SIZE, 1)),
    layers.MaxPooling1D(pool_size=2),
    layers.Conv1D(64, kernel_size=3, activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(3, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# 7. Huấn luyện
history = model.fit(X_train, y_train, epochs=20, validation_data=(X_test, y_test))

# 8. Đánh giá
loss, acc = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {acc:.2f}")
model.save("cnn_vibration_model.h5")
# 9. Vẽ biểu đồ loss/acc
plt.plot(history.history['accuracy'], label='Train acc')
plt.plot(history.history['val_accuracy'], label='Val acc')
plt.legend()
plt.show()
