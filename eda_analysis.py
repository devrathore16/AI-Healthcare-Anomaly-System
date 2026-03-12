import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 1. Load the data from your CSV
file_path = 'data/patient_vitals.csv'

if not os.path.exists(file_path):
    print(f"❌ Error: Could not find {file_path}. Did you run the generation script first?")
else:
    df = pd.read_csv(file_path)
    print("✅ Data loaded successfully!")

    # Show the exact column names to be 100% sure
    print(f"Columns found in file: {df.columns.tolist()}")

    # 2. Show the "Stats" (Mean, Min, Max)
    # Using the exact Capital Letters from your output
    print("\n--- Medical Data Summary ---")
    print(df[['Heart_Rate', 'SpO2']].describe())

    # 3. Create Visualizations
    plt.style.use('ggplot')  # Makes the graphs look professional
    plt.figure(figsize=(12, 5))

    # Plot 1: Heart Rate Distribution
    plt.subplot(1, 2, 1)
    sns.histplot(df['Heart_Rate'], kde=True, color='dodgerblue')
    plt.title('Heart Rate Baseline (BPM)')
    plt.axvline(df['Heart_Rate'].mean(), color='black', linestyle='--', label='Mean')
    plt.legend()

    # Plot 2: SpO2 Distribution
    plt.subplot(1, 2, 2)
    sns.histplot(df['SpO2'], kde=True, color='crimson')
    plt.title('Oxygen Saturation Baseline (%)')
    plt.axvline(df['SpO2'].mean(), color='black', linestyle='--', label='Mean')
    plt.legend()

    plt.tight_layout()
    print("\n📊 Opening graphs... (Close the graph window to return to terminal)")
    plt.show()



