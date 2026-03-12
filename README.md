# AI-Driven Healthcare Anomaly Detection System

## Project Overview
This platform is designed to monitor patient vital signs in real-time and detect life-threatening anomalies using Deep Learning. It acts as an early-warning system for healthcare providers by analyzing streams of heart rate, SpO2, and temperature data.

## Tech Stack
* Language: Python 3.9+
* AI Frameworks: TensorFlow/Keras (Autoencoders), Scikit-learn (MinMaxScaler)
* Streaming: Apache Kafka (KRaft Mode)
* Database: PostgreSQL (for historical alert storage)
* Backend/UI: Flask, Chart.js, Bootstrap
* LLM Integration: Gemini 1.5 Flash (for medical insights)

## Project Structure
* app/: Contains the Flask application and UI templates.
* data/: Contains patient vital datasets (CSV).
* models/: Stores trained AI models (Autoencoder) and scalers.
* scripts/: Contains the Real-time Kafka Producer and AI Consumer.
* notebooks/: Exploratory Data Analysis (EDA) and model training experiments.

## Milestone Summaries

### Phase 1: Infrastructure and Data Generation
Established the real-time data highway using Apache Kafka. Generated a synthetic dataset of 1,000 validated medical records containing Heart Rate, SpO2, and Temperature to define the medical baseline.

### Phase 2: EDA and Preprocessing
Performed Exploratory Data Analysis to identify "Safe Zones" for patients. Implemented a preprocessing pipeline using MinMaxScaler to transform features into a [0, 1] range for the neural network.

### Phase 3: AI Model Training
Developed and trained an Autoencoder neural network to detect anomalies. The model learns the pattern of "normal" vitals and flags deviations based on Reconstruction Error (Mean Squared Error).

### Phase 4: Real-Time Stream Processing
Integrated the AI model into a Kafka Consumer. The system now processes live data streams, calculates anomaly scores in real-time, and identifies high-risk patients.

### Phase 5: Generative AI and Persistence
Integrated Gemini 1.5 Flash to provide natural language medical insights for detected anomalies. Migrated data storage to PostgreSQL to ensure all alerts and AI insights are persisted for clinical review.

### Phase 6: System Validation and Deployment
Conducted stress testing using simulated medical emergencies (Tachycardia/Hypoxia). Verified the end-to-end pipeline from sensor data to the live dashboard. Organized the repository for professional deployment.

## Conclusion
This project demonstrates an end-to-end AI-driven healthcare solution. By combining Predictive AI (Autoencoders) for detection and Generative AI (Gemini) for explanation, the system provides healthcare workers with both "what" is happening and "why" it matters. The use of Kafka and PostgreSQL ensures the system is scalable and reliable for real-time clinical environments.