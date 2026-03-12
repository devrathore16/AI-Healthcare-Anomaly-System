import json
import numpy as np
import tensorflow as tf
import joblib
import pandas as pd
import os
import warnings
import google.generativeai as genai
from kafka import KafkaConsumer
from collections import deque
from sklearn.preprocessing import MinMaxScaler
from datetime import datetime
import psycopg2


def log_to_db(p_id, vitals, mse, severity, insight):
    try:
        # Connect to your local Postgres
        # IMPORTANT: Replace 'YOUR_PASSWORD' with your actual pgAdmin password
        conn = psycopg2.connect(
            dbname="healthcare_db",
            user="postgres",
            password="kirtik",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()

        # This matches the table you just created in pgAdmin
        query = """
        INSERT INTO patient_alerts 
        (patient_id, heart_rate, spo2, temperature, anomaly_score, severity, gemini_insight)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        data = (p_id, vitals[0], vitals[1], vitals[2], float(mse), severity, insight)

        cur.execute(query, data)
        conn.commit()
        cur.close()
        conn.close()
        print(f"📡 Data synced to PostgreSQL for {p_id}")
    except Exception as e:
        print(f"❌ Database Error: {e}")

warnings.filterwarnings("ignore", category=UserWarning)

# --- 1. GEMINI SETUP ---
genai.configure(api_key="AIzaSyAXul4atlYubns39_qkSmTJG4tf4klE5-s")
gemini_model = genai.GenerativeModel('gemini-1.5-flash')


def get_gemini_insight(p_id, vitals, mse, severity):
    prompt = f"Patient {p_id} vitals: HR {vitals[0]}, SpO2 {vitals[1]}, Temp {vitals[2]}. AI Score: {mse:.4f}. Status: {severity}. Give a 1-sentence medical explanation."
    try:
        response = gemini_model.generate_content(prompt)
        return response.text.strip()
    except:
        return "Stable monitoring in progress."


# --- 2. UPDATED DATA BRIDGE (Added Insight Column) ---
def log_to_csv(p_id, vitals, mse, severity, insight):
    file_path = '../data/processed_vitals.csv'
    log_entry = {
        "Timestamp": datetime.now().strftime('%H:%M:%S'),
        "Patient_ID": p_id,
        "Heart_Rate": round(vitals[0], 1),
        "SpO2": round(vitals[1], 1),
        "Temperature": round(vitals[2], 1),
        "Score": round(float(mse), 4),
        "Severity": severity,
        "Insight": insight  # 📍 New column for Gemini text
    }
    df_new = pd.DataFrame([log_entry])
    header = not os.path.exists(file_path)
    df_new.to_csv(file_path, mode='a', index=False, header=header)


# --- 3. MODEL SETUP ---
autoencoder = tf.keras.models.load_model('../models/autoencoder_model.keras')
iso_forest = joblib.load('../models/isolation_forest.pkl')
df_raw = pd.read_csv('../data/patient_vitals.csv')
scaler = MinMaxScaler()
scaler.fit(df_raw[['Heart_Rate', 'SpO2', 'Temperature']])

patient_windows = {}
window_size = 10

consumer = KafkaConsumer(
    'patient-vitals',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("👨‍⚕️ AI Monitor with Gemini & Live Table ACTIVE...")

for message in consumer:
    data = message.value
    p_id = data['Patient_ID']
    raw_sample = [data['Heart_Rate'], data['SpO2'], data['Temperature']]

    if p_id not in patient_windows:
        patient_windows[p_id] = deque(maxlen=window_size)
    patient_windows[p_id].append(raw_sample)

    if len(patient_windows[p_id]) == window_size:
        current_window = np.array(list(patient_windows[p_id]))
        scaled_window = scaler.transform(current_window)
        ai_input = np.array([scaled_window])

        reconstructed = autoencoder.predict(ai_input, verbose=0)
        mse = np.mean(np.power(ai_input - reconstructed, 2))
        is_outlier = iso_forest.predict(ai_input.reshape(1, -1))[0]

        if mse > 0.02 and is_outlier == -1:
            severity = "HIGH"
        elif mse > 0.01:
            severity = "MEDIUM"
        else:
            severity = "LOW"

        # 1. This correctly stores the Gemini text in 'insight'
        insight = get_gemini_insight(p_id, raw_sample, mse, severity)

        # 2. Use 'insight' for both logs (DELETE the lines below these in your file)
        log_to_csv(p_id, raw_sample, mse, severity, insight)
        log_to_db(p_id, raw_sample, mse, severity, insight)

        # 3. Print the result
        print(f"✅ Logged: {p_id} | {severity} | {insight}")

