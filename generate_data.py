import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

# Create the data folder if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# 1. Setup parameters
num_records = 1000
patients = [f"P-{i:03d}" for i in range(1, 11)]  # 10 different patients

data = {
    "Patient_ID": np.random.choice(patients, num_records),
    "Timestamp": [(datetime.now() - timedelta(minutes=i)).strftime('%Y-%m-%d %H:%M:%S') for i in range(num_records)],

    # Heart Rate: Normal is 60-100. We add spikes up to 160 (Anomalies)
    "Heart_Rate": np.random.normal(80, 15, num_records).clip(50, 160),

    # SpO2 (Oxygen): Normal is 95-100. We add drops down to 80 (Anomalies)
    "SpO2": np.random.normal(97, 2, num_records).clip(80, 100),

    # Temperature: Normal is 36.5-37.5. We add fever spikes up to 41.0
    "Temperature": np.random.normal(37.0, 0.6, num_records).clip(35.5, 41.5)
}

# 2. Create DataFrame and Save
df = pd.DataFrame(data)
file_path = "data/patient_vitals.csv"
df.to_csv(file_path, index=False)

print(f"✅ Success! Generated {num_records} records at: {file_path}")
print(df.head())  # Shows the first 5 rows in your terminal



