import streamlit as st
import pandas as pd
import requests
import json

st.markdown("""
# churn app

Select the correct option to view the churn
""")

st.sidebar.header("user Input Parameters: ")
SeniorCitizen = st.sidebar.selectbox("Senior Citizen",0, 1)
tenure = st.sidebar.slider("tenure", 1, 34, 2)
MonthlyCharges = st.sidebar.slider("Monthly", 25, 13.5, 25.5)
TotalCharges = st.sidebar.slider("Total charges", 800, 38, 45)
gender_Female = st.sidebar.selectbox("female gender",values=["true", "false"])
gender_Male = st.sidebar.selectbox("male gender", values=["true", "false"])
Partner_No = st.sidebar.selectbox("No partner", values=["true", "false"])
Partner_Yes = st.sidebar.selectbox("Yes partner", values=["true", "false"])
Dependents_No = st.sidebar.selectbox("No Dependents", values=["true", "false"])
Dependents_Yes = st.sidebar.selectbox("Yes Dependents", values=["true", "false"])
PhoneService_No = st.sidebar.selectbox("No phone service", values=["true", "false"])
PhoneService_Yes = st.sidebar.selectbox("Yes phone service", values=["true", "false"])
MultipleLines_No = st.sidebar.selectbox("No multiple lines", values=["true", "false"])
MultipleLines_No_phone = st.sidebar.selectbox("No phone multiple lines", values=["true", "false"])
service = st.sidebar.selectbox("service", values=["true", "false"])
MultipleLines_Yes = st.sidebar.selectbox("Yes multiple lines", values=["true", "false"])
InternetService_DSL = st.sidebar.selectbox("DSL internet services", values=["true", "false"])
InternetService_Fiber_optics = st.sidebar.selectbox("Fiber optic Internet service", values=["true", "false"])
InternetService_No = st.sidebar.selectbox("No internet service", values=["true", "false"])
OnlineSecurity_No = st.sidebar.selectbox("No online security", values=["true", "false"])
OnlineSecurity_No_internet_service = st.sidebar.selectbox("no internet services online security", values=["true", "false"])
OnlineSecurity_Yes = st.sidebar.selectbox("yes online security", values=["true", "false"])
OnlineBackup_No = st.sidebar.selectbox("No online backup", values=["true", "false"])
OnlineBackup_No_internet_service = st.sidebar.selectbox("no internet services online backup", values=["true", "false"])
OnlineBackup_Yes = st.sidebar.selectbox("yes online backup", values=["true", "false"])
DeviceProtection_No = st.sidebar.selectbox("No device protection", values=["true", "false"])
DeviceProtection_No_internet_service = st.sidebar.selectbox("no internet service device protection", values=["true", "false"])
DeviceProtection_Yes = st.sidebar.selectbox("yes device protection", values=["true", "false"])
TechSupport_No = st.sidebar.selectbox("No technology support", values=["true", "false"])
TechSupport_No_internet_service = st.sidebar.selectbox("no internet service support technology support", values=["true", "false"])
TechSupport_Yes = st.sidebar.selectbox("yes technology support", values=["true", "false"])
StreamingTV_No = st.sidebar.selectbox("No streaming tv", values=["true", "false"])
StreamingTV_No_internet_service =st.sidebar.selectbox("No streaming tv internet service", values=["true", "false"])
StreamingTV_Yes = st.sidebar.selectbox("yes streamingTV", values=["true", "false"])
StreamingMovies_No = st.sidebar.selectbox("no streaming movies", values=["true", "false"])
StreamingMovies_No_internet_service = st.sidebar.selectbox("no streaming movies internet service", values=["true", "false"])
StreamingMovies_Yes = st.sidebar.selectbox("yes streamingMovies", values=["true", "false"])
Contract_Month_to_month = st.sidebar.selectbox("contract month to month", values=["true", "false"])
Contract_One_year = st.sidebar.selectbox("contract one year", values=["true", "false"])
Contract_Two_year = st.sidebar.selectbox("contract two year", values=["true", "false"])
PaperlessBilling_No = st.sidebar.selectbox("no paperless billing", values=["true", "false"])
PaperlessBilling_Yes = st.sidebar.selectbox("yes paperless billing", values=["true", "false"])
PaymentMethod_Bank_transfer = st.sidebar.selectbox("payment method bank transfer", values=["true", "false"])
PaymentMethod_Credit_card = st.sidebar.selectbox("payment method credit card", values=["true", "false"])
PaymentMethod_Electronic_check = st.sidebar.selectbox("payment method electronic check", values=["true", "false"])
PaymentMethod_Mailed_check = st.sidebar.selectbox("payment method mailed check", values=["true", "false"])

dict_input = {
    "senior_citizen": SeniorCitizen,
    "tenure": tenure,
    "MonthlyCharges": MonthlyCharges,
    "TotalCharges": TotalCharges,
    "gender_Female": gender_Female,
    "gender_Male": gender_Male,
    "Partner_No": Partner_No,
    "Partner_Yes": Partner_Yes,
    "Dependents_No": Dependents_No,
    "Dependents_Yes": Dependents_Yes,
    "PhoneService_No": PhoneService_No,
    "PhoneService_Yes": PhoneService_Yes,
    "MultipleLines_No": MultipleLines_No,
    "MultipleLines_No_phone": MultipleLines_No_phone,
    "service": service,
    "MultipleLines_Yes": MultipleLines_Yes,
    "InternetService_DSL": InternetService_DSL,
    "InternetService_Fiber_optics": InternetService_Fiber_optics,
    "InternetService_No": InternetService_No,
    "OnlineSecurity_No": OnlineSecurity_No,
    "OnlineSecurity_No_internet_service": OnlineSecurity_No_internet_service,
    "OnlineSecurity_Yes": OnlineSecurity_Yes,
    "OnlineBackup_No": OnlineBackup_No,
    "OnlineBackup_No_internet_service": OnlineBackup_No_internet_service,
    "OnlineBackup_Yes": OnlineBackup_Yes,
    "DeviceProtection_No": DeviceProtection_No,
    "DeviceProtection_No_internet_service": DeviceProtection_No_internet_service,
    "DeviceProtection_Yes": DeviceProtection_Yes,
    "TechSupport_No": TechSupport_No,
    "TechSupport_No_internet_service": TechSupport_No_internet_service,
    "TechSupport_Yes": TechSupport_Yes,
    "StreamingTV_No": StreamingTV_No,
    "StreamingTV_No_internet_service": StreamingTV_No_internet_service,
    "StreamingTV_Yes": StreamingTV_Yes,
    "StreamingMovies_No": StreamingMovies_No,
    "StreamingMovies_No_internet_service": StreamingMovies_No_internet_service,
    "StreamingMovies_Yes": StreamingMovies_Yes,
    "Contract_Month_to_month": Contract_Month_to_month,
    "Contract_One_year": Contract_One_year,
    "Contract_Two_year": Contract_Two_year,
    "PaperlessBilling_No": PaperlessBilling_No,
    "PaperlessBilling_Yes": PaperlessBilling_Yes,
    "PaymentMethod_Bank_transfer": PaymentMethod_Bank_transfer,
    "PaymentMethod_Credit_card": PaymentMethod_Credit_card,
    "PaymentMethod_Electronic_check": PaymentMethod_Electronic_check,
    "PaymentMethod_Mailed_check": PaymentMethod_Mailed_check
}

df_input = pd.DataFrame(dict_input, index = [0])
st.subheader("User Input")
st.write(df_input)

if st.button("predict"):
    url = "http://0.0.0.0:5050/api/v1/classify?api_key=ChurnModel-2024$*"

    payload = json.dumps(dict_input)

    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    st.write("Prediction: ",response.json()["prediction"])

    print(response.text)