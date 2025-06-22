  # Vibration Monitoring and Prediction System
  
  ## 📌 Description
  
  A system for monitoring and predicting vibration in industrial machines (e.g., steel factories).  
  The project simulates vibration data, stores it in InfluxDB, trains a deep learning model (CNN), and displays predictions through a Streamlit web interface.
  
  ---
  
  ## 👨‍💻 Author
  
  - **Name:** NGUYEN XUAN HIEU
  - **Email:** nguyenxuanhieu167@gmail.com
  - **GitHub:** https://github.com/eooikut
  
  ---
  
  ## 🧱 Project Structure
  .
  ├── data_generator.py # Simulates vibration data and stores it in InfluxDB
  
  ├── train_model.py # Trains the CNN model
  
  ├── predict.py # Predicts machine status from data
  
  ├── app.py # Streamlit web interface
  
  ├── influx_config.py # InfluxDB connection configuration
  
  ├── requirements.txt # Project dependencies
  
  └── README.md # Project documentation
  
  
  ---
  
  ## 📦 Dependencies
  
  - Python >= 3.8
  - `streamlit`
  - `pandas`
  - `numpy`
  - `influxdb`
  - `tensorflow`
  - `matplotlib`
  - `scikit-learn`
  
  ### Installation
  
  ```bash
  pip install -r requirements.txt
  
  ⚙️ Start InfluxDB (Windows)
  Download and install from:
  👉 https://portal.influxdata.com/downloads/
  
  Then start the InfluxDB server:
  bash
  influxd
  
  🚀 How to Use
  1. Generate Simulated Data
  
  python data_generator.py
  
  2. Train the Model
  
  python train_model.py
  
  3. Launch the Web Interface
  
  streamlit run app.py
  
  ⚙️ Advanced Options
  Feature	Supported
  Grafana Integration	✅
  
  
  📤 Outputs
  Vibration status prediction interface
  
  Real-time data visualization
  
  Trained model saved as .h5 file
  
 ## 📚 References

- [InfluxDB Docs](https://docs.influxdata.com/)
- [Streamlit Docs](https://docs.streamlit.io/)
- [Keras CNN Examples](https://keras.io/examples/vision/)
