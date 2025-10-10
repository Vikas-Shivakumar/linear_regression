import streamlit as st
import pickle
import pandas as pd

# Load model
with open('full_pipeline', 'rb') as f:
    model = pickle.load(f)

st.set_page_config(page_title="Loan Prediction", page_icon="💰", layout="centered")
st.title("💰 Loan Approval Prediction App")

# Inputs
Married = st.selectbox("Married", ["Yes", "No"])
Education = st.selectbox("Education", ["Graduate", "Not Graduate", "HSC"])
ApplicantIncome = st.number_input("Applicant Income", min_value=0, step=500)
LoanAmount = st.number_input("Loan Amount", min_value=0, step=50)
Credit_History = st.selectbox("Credit History", [1.0, 0.0])

if st.button("Predict"):
    input_df = pd.DataFrame({
        'Married': [Married],
        'Education': [Education],
        'ApplicantIncome': [ApplicantIncome],
        'LoanAmount': [LoanAmount],
        'Credit_History': [Credit_History]
    })

    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")

    st.subheader("Entered Details")
    st.write(input_df)
