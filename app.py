import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

# Class and Object (Project Condition)
class HeartPredictor:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100)
        self.scaler = StandardScaler()

    def train_model(self, data):
        X = data.drop('target', axis=1)
        y = data['target']
        X_scaled = self.scaler.fit_transform(X)
        self.model.fit(X_scaled, y)
        return "Trained"

st.title("Heart Disease Predictor ❤️")

# Load Data
df = pd.read_csv("heart.csv")
predictor = HeartPredictor()
predictor.train_model(df)

# All 13 Inputs from User
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 1, 100, 25)
    sex = st.selectbox("Sex (1=M, 0=F)", [1, 0])
    cp = st.selectbox("Chest Pain Type (0-3)", [0, 1, 2, 3])
    trestbps = st.number_input("Resting BP", 80, 200, 120)
    chol = st.number_input("Cholesterol", 100, 600, 200)
    fbs = st.selectbox("Fasting Blood Sugar > 120 (1=T, 0=F)", [0, 1])

with col2:
    restecg = st.selectbox("Resting ECG (0-2)", [0, 1, 2])
    thalach = st.number_input("Max Heart Rate", 60, 220, 150)
    exang = st.selectbox("Exercise Induced Angina (1=Y, 0=N)", [0, 1])
    oldpeak = st.number_input("ST Depression", 0.0, 6.0, 1.0)
    slope = st.selectbox("Slope of ST (0-2)", [0, 1, 2])
    ca = st.selectbox("Major Vessels (0-4)", [0, 1, 2, 3, 4])
    thal = st.selectbox("Thal (0-3)", [0, 1, 2, 3])

if st.button("Predict Result"):
    # Making array of all 13 features
    features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    scaled_features = predictor.scaler.transform(features)
    prediction = predictor.model.predict(scaled_features)
    
    if prediction[0] == 1:
        st.error("Possibility of Heart Disease")
    else:
        st.success("Heart is Healthy!")