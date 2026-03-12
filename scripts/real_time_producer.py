from kafka import KafkaProducer
import pandas as pd
import json
import time

# 1. Setup Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

# 2. Load the data you generated
try:
    df = pd.read_csv('../data/patient_vitals.csv')
    print("📂 Original patient vitals loaded.")
except FileNotFoundError:
    print("❌ Error: data/patient_vitals.csv not found!")
    exit()

print("🚀 Starting real-time stream to Kafka (Normal Mode)...")

# 3. Stream each row at a steady pace
for index, row in df.iterrows():
    data = row.to_dict()

    # Sending exactly what is in the CSV
    producer.send('patient-vitals', value=data)

    print(f"📡 Sent to Kafka: {data['Patient_ID']} - HR: {data['Heart_Rate']:.2f}")

    # 1 second delay for a realistic human pulse feel
    time.sleep(1)

