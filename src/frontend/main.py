import streamlit as st
import pandas as pd
import requests
import json

st.markdown("""
# churn app

Select the correct option to view the churn
""")

st.sidebar.header("user Input Parameters: ")
SeniorCitizen = st.sidebar.slider("Senior Citizen",0, 1)
tenure = st.sidebar.slider("tenure", 0, 34, 72)
MonthlyCharges = st.sidebar.slider("Monthly", 18.25, 50.0, 118.75)
TotalCharges = st.sidebar.slider("Total charges", 20, 2000, 7000)
gender_Female = st.sidebar.selectbox("female gender", ["true", "false"])
gender_Male = st.sidebar.selectbox("male gender", ["true", "false"])
Partner_No = st.sidebar.selectbox("No partner", ["true", "false"])
Partner_Yes = st.sidebar.selectbox("Yes partner", ["true", "false"])
Dependents_No = st.sidebar.selectbox("No Dependents", ["true", "false"])
Dependents_Yes = st.sidebar.selectbox("Yes Dependents", ["true", "false"])
PhoneService_No = st.sidebar.selectbox("No phone service", ["true", "false"])
PhoneService_Yes = st.sidebar.selectbox("Yes phone service", ["true", "false"])
MultipleLines_No = st.sidebar.selectbox("No multiple lines", ["true", "false"])
MultipleLines_No_phone = st.sidebar.selectbox("No phone multiple lines", ["true", "false"])
service = st.sidebar.selectbox("service", ["true", "false"])
MultipleLines_Yes = st.sidebar.selectbox("Yes multiple lines", ["true", "false"])
InternetService_DSL = st.sidebar.selectbox("DSL internet services", ["true", "false"])
InternetService_Fiber_optics = st.sidebar.selectbox("Fiber optic Internet service", ["true", "false"])
InternetService_No = st.sidebar.selectbox("No internet service", ["true", "false"])
OnlineSecurity_No = st.sidebar.selectbox("No online security", ["true", "false"])
OnlineSecurity_No_internet_service = st.sidebar.selectbox("no internet services online security", ["true", "false"])
OnlineSecurity_Yes = st.sidebar.selectbox("yes online security", ["true", "false"])
OnlineBackup_No = st.sidebar.selectbox("No online backup", ["true", "false"])
OnlineBackup_No_internet_service = st.sidebar.selectbox("no internet services online backup", ["true", "false"])
OnlineBackup_Yes = st.sidebar.selectbox("yes online backup", ["true", "false"])
DeviceProtection_No = st.sidebar.selectbox("No device protection", ["true", "false"])
DeviceProtection_No_internet_service = st.sidebar.selectbox("no internet service device protection", ["true", "false"])
DeviceProtection_Yes = st.sidebar.selectbox("yes device protection", ["true", "false"])
TechSupport_No = st.sidebar.selectbox("No technology support", ["true", "false"])
TechSupport_No_internet_service = st.sidebar.selectbox("no internet service support technology support", ["true", "false"])
TechSupport_Yes = st.sidebar.selectbox("yes technology support", ["true", "false"])
StreamingTV_No = st.sidebar.selectbox("No streaming tv", ["true", "false"])
StreamingTV_No_internet_service =st.sidebar.selectbox("No streaming tv internet service", ["true", "false"])
StreamingTV_Yes = st.sidebar.selectbox("yes streamingTV", ["true", "false"])
StreamingMovies_No = st.sidebar.selectbox("no streaming movies", ["true", "false"])
StreamingMovies_No_internet_service = st.sidebar.selectbox("no streaming movies internet service", ["true", "false"])
StreamingMovies_Yes = st.sidebar.selectbox("yes streamingMovies", ["true", "false"])
Contract_Month_to_month = st.sidebar.selectbox("contract month to month", ["true", "false"])
Contract_One_year = st.sidebar.selectbox("contract one year", ["true", "false"])
Contract_Two_year = st.sidebar.selectbox("contract two year", ["true", "false"])
PaperlessBilling_No = st.sidebar.selectbox("no paperless billing", ["true", "false"])
PaperlessBilling_Yes = st.sidebar.selectbox("yes paperless billing", ["true", "false"])
PaymentMethod_Bank_transfer = st.sidebar.selectbox("payment method bank transfer", ["true", "false"])
PaymentMethod_Credit_card = st.sidebar.selectbox("payment method credit card", ["true", "false"])
PaymentMethod_Electronic_check = st.sidebar.selectbox("payment method electronic check", ["true", "false"])
PaymentMethod_Mailed_check = st.sidebar.selectbox("payment method mailed check", ["true", "false"])

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
    url = "http://churn-app:5050/api/v1/classify?api_key=ChurnModel-2024$*"

    payload = json.dumps(dict_input)

    headers = {
     'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    st.write("Prediction: ", response.json()["prediction"])

    print(response.text)