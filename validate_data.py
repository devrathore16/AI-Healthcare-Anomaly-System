import pandas as pd

# 1. Load the generated data
try:
    df = pd.read_csv('data/patient_vitals.csv')
    print("✅ Data loaded successfully.\n")
except FileNotFoundError:
    print("❌ Error: CSV file not found. Run generate_data.py first!")
    exit()

# 2. Check for Missing Values (The "Null" Check)
print("--- Missing Values Check ---")
print(df.isnull().sum())

# 3. Clinical Range Validation (The "Lead" Logic)
print("\n--- Clinical Range Validation ---")
# Flagging data that is physically impossible for a human
invalid_hr = df[(df['Heart_Rate'] < 30) | (df['Heart_Rate'] > 220)]
invalid_spo2 = df[(df['SpO2'] < 50) | (df['SpO2'] > 100)]

print(f"Total records checked: {len(df)}")
print(f"⚠️ Out-of-range Heart Rate detected: {len(invalid_hr)}")
print(f"⚠️ Out-of-range SpO2 detected: {len(invalid_spo2)}")

# 4. Statistical Profile
print("\n--- Statistical Summary ---")
print(df.describe())



