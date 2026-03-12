AI-Driven Healthcare Anomaly Detection System
Project Overview

This platform is designed to continuously monitor patient vital signs and detect potentially life-threatening anomalies using Deep Learning techniques. The system acts as an intelligent early-warning solution for healthcare providers by analyzing real-time streams of physiological data such as Heart Rate, SpO₂ levels, and Body Temperature.

The system combines Predictive AI for anomaly detection with Generative AI for clinical explanation, enabling healthcare professionals to quickly understand abnormal patterns and take timely action. By leveraging real-time streaming pipelines, deep learning models, and scalable databases, the platform simulates how modern hospitals can implement AI-driven monitoring systems to improve patient safety and response time.

The architecture is designed to be scalable, modular, and real-time capable, making it suitable for integration with wearable devices, smart hospital equipment, or remote patient monitoring systems.

Tech Stack
Programming Language

Python 3.9+

Core development language used for data processing, model development, backend services, and streaming pipelines.

AI / Machine Learning Frameworks

TensorFlow / Keras

Used to design and train the Autoencoder neural network responsible for detecting anomalies in patient vital signals.

Scikit-learn

Used for preprocessing tasks including MinMaxScaler, data normalization, and feature transformation.

Real-Time Streaming

Apache Kafka (KRaft Mode)

Provides a distributed event streaming platform for real-time transmission of patient vitals.

Simulates continuous sensor data streams from medical devices.

Database

PostgreSQL

Stores historical patient vitals, anomaly alerts, and AI-generated insights.

Enables medical staff to review past alerts for clinical analysis and auditing.

Backend and Visualization

Flask

Lightweight backend framework for building REST APIs and serving dashboards.

Chart.js

Used to create dynamic real-time charts displaying patient vitals and anomaly alerts.

Bootstrap

Provides responsive UI components for building the monitoring dashboard.

Generative AI Integration

Gemini 1.5 Flash

Used to generate natural language explanations for detected anomalies.

Converts raw anomaly signals into interpretable medical insights for healthcare providers.

Project Structure
app/

Contains the Flask web application responsible for the monitoring dashboard.

Includes:

Backend API endpoints

Dashboard templates

Real-time chart visualizations

Alert display panels

data/

Stores datasets used during experimentation and training.

Includes:

Synthetic patient vitals dataset (CSV format)

Simulated medical events for stress testing

Baseline medical ranges used for model training

models/

Stores trained machine learning models and preprocessing components.

Includes:

Trained Autoencoder model

Feature scalers and preprocessing pipelines

Serialized models for real-time inference

scripts/

Contains the real-time data pipeline components.

Includes:

Kafka Producer

Simulates medical sensor devices sending patient vitals.

Kafka Consumer

Consumes real-time data streams.

Performs preprocessing and anomaly detection using the trained AI model.

notebooks/

Contains exploratory analysis and experimentation notebooks.

Includes:

Exploratory Data Analysis (EDA)

Data visualization and statistical analysis

Autoencoder training experiments

Hyperparameter tuning experiments

Milestone Summaries
Phase 1: Infrastructure and Data Generation

The first phase focused on building the real-time streaming infrastructure.

Key tasks included:

Setting up Apache Kafka in KRaft mode for distributed event streaming.

Designing a synthetic patient dataset containing 1,000 realistic medical records.

Generating vitals such as:

Heart Rate

SpO₂

Body Temperature

Ensuring medical realism by defining clinically validated baseline ranges for normal patient conditions.

This phase established the data pipeline foundation required for real-time anomaly monitoring.

Phase 2: Exploratory Data Analysis and Preprocessing

This phase focused on understanding the dataset and preparing it for deep learning.

Activities included:

Visualizing patient vital distributions using statistical plots.

Identifying normal physiological ranges ("Safe Zones") for each vital sign.

Detecting patterns and correlations among vital parameters.

Data preprocessing pipeline:

Applied MinMaxScaler to normalize features into the [0,1] range.

Removed noise and inconsistencies in the dataset.

Prepared structured inputs for neural network training.

This step ensured the model receives stable and properly scaled input data.

Phase 3: AI Model Training

In this phase, a Deep Learning Autoencoder model was developed to detect anomalies.

Why Autoencoder?

Autoencoders are ideal for anomaly detection because they:

Learn patterns of normal behavior

Reconstruct normal data efficiently

Produce high reconstruction errors when abnormal inputs appear

Model workflow

Input patient vitals

Encoder compresses data into latent representation

Decoder reconstructs the original data

Reconstruction error is calculated using Mean Squared Error (MSE)

If the error exceeds a predefined threshold → Anomaly detected

This allows the system to identify conditions such as:

Tachycardia (abnormally high heart rate)

Hypoxia (low oxygen levels)

Fever or abnormal temperature spikes

Phase 4: Real-Time Stream Processing

The trained model was integrated into the real-time streaming pipeline.

Process flow:

Medical sensor data is simulated using a Kafka Producer

Data streams into Kafka topics

Kafka Consumer continuously processes incoming data

Consumer loads the trained Autoencoder model

Model calculates anomaly score in real-time

Alerts are triggered if abnormal vitals are detected

This phase transforms the system into a live AI monitoring pipeline.

Phase 5: Generative AI and Persistence

This phase enhanced the system with explainable AI capabilities.

Two key improvements were implemented:

1. Generative AI Medical Insights

Gemini 1.5 Flash is used to generate human-readable medical explanations for anomalies.

Example:

Instead of showing:

Anomaly Score: 0.84

The system produces:

"Patient shows signs of tachycardia with elevated heart rate and slightly reduced oxygen levels. Immediate monitoring is recommended."

This improves interpretability for healthcare professionals.

2. Persistent Data Storage

Migrated alert storage to PostgreSQL to maintain historical records.

Stored information includes:

Timestamp of anomaly

Patient vitals

Anomaly score

AI-generated explanation

Alert severity level

This enables clinical review, reporting, and long-term analysis.

Phase 6: System Validation and Deployment

The final phase focused on validating system reliability.

Stress testing was performed using simulated medical emergencies such as:

Tachycardia scenarios

Hypoxia conditions

Sudden temperature spikes

The system was evaluated for:

Real-time latency

Model accuracy

Alert reliability

Dashboard responsiveness

The repository was then structured for professional deployment with:

Clean modular architecture

Organized documentation

Production-ready pipelines

Conclusion

This project demonstrates a complete end-to-end AI healthcare monitoring system that integrates multiple modern technologies.

Key innovations include:

Predictive AI (Autoencoders) for detecting abnormal physiological patterns

Generative AI (Gemini) for generating interpretable clinical insights

Apache Kafka for real-time data streaming

PostgreSQL for scalable medical data storage

Flask + Chart.js dashboards for live patient monitoring

By combining real-time streaming, deep learning, and generative AI, the system provides healthcare providers with both:

What is happening (anomaly detection)

Why it matters (AI-generated explanation)

Such architectures can be extended to smart hospitals, wearable health devices, telemedicine platforms, and remote patient monitoring systems, helping improve early detection of critical medical conditions and enabling faster clinical decision-making.
