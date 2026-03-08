
import streamlit as st
import pandas as pd

st.title("AI Healthcare Anomaly Detection Dashboard")

data = pd.read_csv("../dataset/patient_vitals.csv")

st.subheader("Patient Vital Signs Dataset")
st.dataframe(data)

st.subheader("Heart Rate Trend")
st.line_chart(data["heart_rate"])

st.subheader("Blood Pressure Trend")
st.line_chart(data["blood_pressure"])

st.subheader("Temperature Trend")
st.line_chart(data["temperature"])

st.subheader("Oxygen Level Trend")
st.line_chart(data["oxygen_level"])
