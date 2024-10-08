import pickle
import streamlit as st
import numpy as np


st.title('BBHS student prediction model for external exams 🔮')

Study_hours = st.text_input("Enter weekly study hours", max_chars=2)
prev_grade = st.text_input("Enter cummulative from previous term percentage", max_chars=3) 
mock_grade = st.text_input("Enter mock cummulative percentage", max_chars=3)  


def predict_price():
    with open('model_pickle','rb') as file:
      pred_model = pickle.load(file)    

    x = np.zeros(3)
    x[0] = Study_hours
    x[1] = prev_grade
    x[2] = mock_grade
    prediction = pred_model.predict([x])[0]
    if prediction == 1:
        st.success('Likely to pass, Do not relent ')
    else:
      st.error('Likely to fail, Keep pushing harder') 


st.button('Predict', on_click=predict_price)