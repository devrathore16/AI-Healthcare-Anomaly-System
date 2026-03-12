import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.ensemble import IsolationForest
import joblib
import os

# --- PRE-REQUISITE: CREATE MODELS FOLDER ---
if not os.path.exists('models'):
    os.makedirs('models')

# --- TASK 3.1: SLIDING WINDOW (TEMPORAL MODELING) ---
def create_sequences(data, window_size=10):
    sequences = []
    for i in range(len(data) - window_size):
        sequences.append(data[i:i+window_size])
    return np.array(sequences)

# Load data
df = pd.read_csv('data/processed_vitals.csv')
features = ['Heart_Rate', 'SpO2', 'Temperature']
data_values = df[features].values

# Create windows
window_size = 10
X_train = create_sequences(data_values, window_size)
print(f"✅ Created {X_train.shape[0]} sequences of {window_size} seconds each.")

# --- TASK 3.2: 6-LAYER AUTOENCODER ---
# Fixed the units to be a plain integer for Keras
total_units = int(window_size * len(features))

model = models.Sequential([
    layers.Input(shape=(window_size, len(features))),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(32, activation='relu'), # The "Bottleneck"
    layers.Dense(64, activation='relu'),
    layers.Dense(128, activation='relu'),
    layers.Dense(total_units, activation='sigmoid'),
    layers.Reshape((window_size, len(features)))
])

model.compile(optimizer='adam', loss='mae')
print("\n🧠 Training Autoencoder (Deep Learning)...")
model.fit(X_train, X_train, epochs=30, batch_size=32, verbose=1)

# --- TASK 3.2: ISOLATION FOREST ---
print("\n🌲 Training Isolation Forest (Outlier Hunter)...")
X_train_flat = X_train.reshape(X_train.shape[0], -1)
iso_forest = IsolationForest(n_estimators=200, contamination=0.05, random_state=42)
iso_forest.fit(X_train_flat)

# --- SAVE MODELS ---
model.save('models/autoencoder_model.keras')
joblib.dump(iso_forest, 'models/isolation_forest.pkl')
print("\n🏆 MILESTONE 3 COMPLETE: Both models saved in /models/ folder!")



