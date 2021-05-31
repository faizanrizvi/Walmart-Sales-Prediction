import numpy as np
import pickle
import pandas as pd
import streamlit as st 
import joblib

# x = [Store, IsHoliday, Type, Size, Dept, Month, Week, Year,day]


@st.cache
def predict(x):
	rf = joblib.load('best_model.pkl')
	rf1 = np.round(rf.predict([x]),3)
	return rf1

def main():
	st.title("Walmart Sales Prediction")
	html_temp = """
	    <div style="background-color:tomato;padding:10px">
	    <h2 style="color:white;text-align:center;">Streamlit Walmart Sales Prediction ML App </h2>
	    </div>
	    """
	st.markdown(html_temp,unsafe_allow_html=True)
	Store = st.text_input("Store")
	IsHoliday = st.text_input("IsHoliday")
	Type = st.text_input("Type")
	Size = st.text_input("Size")
	Dept = st.text_input("Dept")
	Month = st.text_input("Month")
	Week = st.text_input("Week")
	Year = st.text_input("Year")
	day = st.text_input("day")

	x = [Store, IsHoliday, Type, Size, Dept, Month, Week, Year,day]

	result=""
	if st.button("Predict"):
	    result= predict(x)

	st.success('The output is {}'.format(result))
	
if __name__=='__main__':
    main()