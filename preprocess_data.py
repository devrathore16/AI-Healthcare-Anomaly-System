import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# 1. Load your 1,000 records
df = pd.read_csv('data/patient_vitals.csv')

# 2. Select the key medical features for the AI
features = ['Heart_Rate', 'SpO2', 'Temperature']
df_vitals = df[features]

# 3. Apply MinMaxScaler (Scales data between 0 and 1)
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(df_vitals)

# 4. Create the final clean DataFrame
df_scaled = pd.DataFrame(scaled_data, columns=features)

print("✅ Milestone 2.3 Complete: Data is Normalized!")
print(df_scaled.head())

# Save it for Milestone 3 AI Training
df_scaled.to_csv('data/processed_vitals.csv', index=False)



