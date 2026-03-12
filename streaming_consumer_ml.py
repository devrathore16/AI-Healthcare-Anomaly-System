from kafka import KafkaConsumer
import json

# Initialize the Consumer to listen to the 'patient_vitals' stream
consumer = KafkaConsumer(
    'patient_vitals',
    bootstrap_servers=['localhost:9022'],
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("📥 AI Consumer is active. Monitoring live patient vitals...")

for message in consumer:
    vitals = message.value
    # Placeholder for Milestone 3: model.predict(vitals)
    print(f"🤖 Analyzing Patient {vitals['Patient_ID']}: HR={vitals['Heart_Rate']:.1f} | Result: NORMAL")



