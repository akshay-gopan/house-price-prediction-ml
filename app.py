import streamlit as st
import joblib as jb
import numpy as np

model = jb.load("model.pkl")


st.markdown("<h1 style='text-align: center;'>House Price Prediction</h1>", unsafe_allow_html=True)
st.divider()



bedrooms = st.number_input("Number of Bedrooms", min_value=0, value=0)

bathrooms = st.number_input("Number of Bathrooms", min_value=0, value=0)

living_area = st.number_input("Living Area", min_value=0, value=2000)

condition = st.number_input("Condition of the House", min_value=0, value=3)

numberofschools = st.number_input("Number of Schools Nearby", min_value=0, value=0)

st.divider()

x = [[bedrooms, bathrooms, living_area, condition, numberofschools]]

predictButton = st.button("Predict")

if predictButton:
    x_array = np.array(x)

    prediction = model.predict(x_array)[0]

    
    st.markdown(f"<h2 style='font-weight: bold; font-size: 24px;'>Predicted Price is INR {prediction:,.2f}</h2>", unsafe_allow_html=True)

else:
    st.write("Press the predict button after entering values")







#used criterions
#Index(['number of bedrooms', 'number of bathrooms', 'living area',
       #'condition of the house', 'Number of schools nearby'],
     # dtype='object')