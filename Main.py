# -*- coding: utf-8 -*-

import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('C:/Users/NOAH/Desktop/TestData/trained_model.sav', 'rb'))


# creating a function for Prediction

def diabetes_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] != 0):
      return 'The person is diabetic'
    else:
      return 'The person is not diabetic'
  
    
  
def main():
    
    
    # giving a title
    st.title('Diabetes Prediction Web App')
    
    
    # getting the input data from the user
    
    Age = st.text_input('Age of the Person')
    Hypertension = st.text_input('Hyperextension - 0=No 1=Yes')
    Heart_Disease = st.text_input('Heart Disease - 0=No 1=Yes')
    BMI = st.text_input('BMI value')
    HbA1c_Level = st.text_input('HbA1c Level value')
    Body_Glucose = st.text_input('Body Glucose value')
    
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Age, Hypertension, Heart_Disease, BMI, HbA1c_Level, Body_Glucose])
        
        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()