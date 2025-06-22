import numpy as np
import streamlit as st
from tensorflow.keras.models import load_model

# Load mô hình đã huấn luyện
model = load_model("cnn_vibration_model.h5")

st.title("🔮 Dự đoán trạng thái rung động bằng CNN")
st.markdown("Nhập vào 20 giá trị độ rung gần nhất để dự đoán trạng thái.")

# Nhập 20 giá trị rung
inputs = []
for i in range(20):
    value = st.number_input(f"Giá trị rung thứ {i+1}", min_value=0.0, max_value=10.0, step=0.01, key=f"input_{i}")
    inputs.append(value)

if st.button("Dự đoán"):
    input_array = np.array(inputs).reshape(1, 20, 1)
    prediction = model.predict(input_array)
    label = np.argmax(prediction)
    labels = ['Nhẹ (Light)', 'Trung bình (Medium)', 'Nặng (Heavy)']
    st.success(f"✅ Dự đoán: {labels[label]}")

