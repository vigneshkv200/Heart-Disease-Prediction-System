# Heart Disease Prediction System

This project predicts the risk of heart disease using a machine learning model (Random Forest / CatBoost). It takes patient health parameters such as age, cholesterol, blood pressure, and heart rate, and outputs whether the patient is at risk.

## Features
- Trained ML classifier with ~75% accuracy
- High recall (~80%) for detecting heart disease cases
- Feature importance analysis for interpretability
- Streamlit web app for real-time prediction

## Tech Stack
- Python
- Scikit-learn
- Pandas / NumPy
- Streamlit

## How to Run
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the Streamlit app:
```bash
streamlit run app.py
```

## Project Structure
```
heart_disease_project/
│
├── app.py
├── heart_disease_model.pkl
├── heart_disease_dataset.csv
├── requirements.txt
└── README.md
```

## Results
The model achieved:
- Accuracy: 0.75
- Recall: 0.80

## Author
Vignesh KV

---
This project is built for learning and demonstrating an end-to-end ML deployment workflow.
