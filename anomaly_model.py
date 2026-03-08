
import pandas as pd
from sklearn.ensemble import IsolationForest

data = pd.read_csv("../dataset/patient_vitals.csv")

model = IsolationForest(contamination=0.1, random_state=42)
model.fit(data)

data["anomaly"] = model.predict(data)

print(data)

data.to_csv("prediction_output.csv", index=False)
