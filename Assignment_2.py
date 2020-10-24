# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 01:36:27 2020

@author: Admin 2
"""


import pickle
import streamlit as st
import numpy as np

pickle_in =open('xgboost_model.pkl','rb')
xgboost_model=pickle.load(pickle_in)

    
def churn_predict(SeniorCitizen,	PaperlessBilling,	PaymentMethod,MultipleLines,MonthlyCharges):
    input=np.array([[SeniorCitizen,	PaperlessBilling,	PaymentMethod,MultipleLines,MonthlyCharges]]).astype(np.float64)
    prediction=xgboost_model.predict(input)
    return prediction


def main():
    st.title("Customer Churn Prediction Application")
    html_temp = """
    <div style="background-color:#0252de ;padding:10px">
    <h2 style="color:white;text-align:center;">Churn Prediction Application </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
   # SeniorCitizen	PaperlessBilling	PaymentMethod	MonthlyCharges	MultipleLines
    #gender = st.text_input("Gennder","",key='gender')
    SeniorCitizen = st.text_input("SeniorCitizen","",key='SeniorCitizen')
    #Partner = st.text_input("Partner","",key='Partner ')
    #Dependents= st.text_input("Dependents","",key='Dependents ')
    #tenure = st.text_input("Tenure","",key='tenure ')
    #PhoneService= st.text_input("PhoneService","",key='PhoneService ')
    #MultipleLines = st.text_input("MultipleLines","",key='MultipleLines ')
    #InternetService= st.text_input("InternetService","Type Here",key='InternetService ')
    #OnlineSecurity = st.text_input("OnlineSecurity","Type Here",key='OnlineSecurity ')
    #OnlineBackup= st.text_input("OnlineBackup","Type Here",key='OnlineBackup ')
    #DeviceProtection = st.text_input("DeviceProtection","Type Here",key='DeviceProtection ')
   # TechSupport= st.text_input("TechSupports","Type Here",key='TechSupport ')
    #StreamingTV = st.text_input("StreamingTV","Type Here",key='StreamingTV ')
   # StreamingMovies = st.text_input("StreamingMovies","Type Here",key='StreamingMovies ')
   # Contract= st.text_input("Contract","Type Here",key='Contract ')
    PaperlessBilling = st.text_input("PaperlessBilling","",key='PaperlessBilling ')
    PaymentMethod= st.text_input("PaymentMethod","",key='PaymentMethod')
    MultipleLines = st.text_input("MultipleLines","",key='MultipleLines ')
    MonthlyCharges= st.text_input("MonthlyCharges","",key='MonthlyCharges')
    
    #TotalCharges= st.text_input("TotalCharges","Type Here",key='TotalChargess ')
    output=""
    
    
    safe_html="""  
      <div style="background-color:#F4D03F;padding:10px >
       <h2 style="color:white;text-align:center;"> No</h2>
       </div>
    """
    danger_html="""  
      <div style="background-color:#F08080;padding:10px >
       <h2 style="color:black ;text-align:center;">Yes</h2>
       </div>
    """
 
    if st.button("Predict"):
        output=churn_predict(SeniorCitizen,	PaperlessBilling,PaymentMethod,MultipleLines,MonthlyCharges)

        if output == 1:
            st.markdown(danger_html,unsafe_allow_html=True)
        else:
            st.markdown(safe_html,unsafe_allow_html=True)
 

 
if __name__=='__main__':
    main()
