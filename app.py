import streamlit as st
import joblib
import numpy as np

st.title("❤️ Heart Disease Prediction")
model=joblib.load("heart_disese")

st.subheader("Enter The Patient Details below")


age = st.number_input("Age", 1, 120, 50)
sex = st.selectbox("Sex (0=Female, 1=Male)", [0, 1])
cp = st.number_input("Chest Pain Type (0–3)", 0, 3, 1)
bp = st.number_input("Resting Blood Pressure", 80, 200, 120)
chol = st.number_input("Cholesterol", 100, 400, 200)
fbs = st.selectbox("Fasting Blood Sugar > 120 (0/1)", [0, 1])
ecg = st.number_input("Resting ECG (0–2)", 0, 2, 0)
hr = st.number_input("Max Heart Rate", 60, 220, 150)
angina = st.selectbox("Exercise Induced Angina (0/1)", [0, 1])
oldpeak = st.number_input("ST Depression", 0.0, 6.0, 1.0)
slope = st.number_input("ST Slope (0–2)", 0, 2, 1)
vessels = st.number_input("Major Vessels (0–3)", 0, 3, 0)
thal = st.number_input("Thalassemia (0–3)", 0, 3, 2)

if st.button("Predict"):
    data=np.arrayinput_data = np.array([[age, sex, cp, bp, chol, fbs, ecg, hr,
                            angina, oldpeak, slope, vessels, thal]])
    prediction=model.predict(data)
    if prediction[0] == 1:
        st.error("⚠ disese detected")
    else :
        st.success(" ✅No heart disese Risk")
