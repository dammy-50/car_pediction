import streamlit as st 
import numpy as np
import pandas as pd
import datetime
import xgboost as xgb

def main():
    html_temp="""
     <div style = "background-color:lightblue;padding:16px">
     <h2 style = "color:black;text-align:centre;">Car Price Prediction Using Machine Learning</h2>
     </div>
    """
    model = xgb.XGBRegressor()
    model.load_model('C:/Users/DAMMY/Desktop/Car_purchase_webapp/xgb_model.json')

    st.markdown(html_temp,unsafe_allow_html = True)
    st.write('')
    st.write('')

    st.markdown("##### Do you want to sell your car?\n##### Let me help you evaluate the Price.")
    p1 = st.number_input("What is the Current price of the car(In Naira)?",2.5,25.0,step = 1.0)
    p2 = st.number_input("What is the distance completed by the car(In kilometers)?",100,10000,step = 100)
    s1 = st.selectbox("What is the fuel type of the car?",('Petrol','Diesel','CNG'))
    if s1 == 'Petrol':
       p3= 0
    elif s1 == 'Diesel':
       p3=1
    elif s1 == 'CNG':
       p3=2
    s2 = st.selectbox("Are you a dealer or an individual?",('Dealer','Individual'))
    if s2 == 'Dealer':
       p4= 0
    elif s2 == 'Individual':
       p4=1
    s3 = st.selectbox("What is the car transmission type?",('Manual','Automatic'))
    if s3 == 'Manual':
       p5= 0
    elif s3 == 'Automatic':
       p5= 1
    p6 = st.slider('How many number of Owners have the Car previously had?',0,3)
    date_time = datetime.datetime.now()
    years = st.number_input("Which year was the car purchased?",1990,date_time.year)
    p7 = date_time.year - years
    new_data = pd.DataFrame({	
      'Present_Price':p1,		
      'Kms_Driven':p2,
      'Fuel_Type':p3,
      'Seller_Type':p4,
      'Transmission':p5,
      'Owner':p6,
      'Age':p7
},index = [0])
    try:
       if st.button('predict'):
           pred = model.predict(new_data)
           if pred>0:
               st.success("Your car is eligible for sale for {:.2f} Naira".format(pred[0]))
           else:
               st.warning("Sorry,your car is not eligible for sale")
    except:
        st.warning("Wrong input! please try again")

    



if __name__ == '__main__':
    main()
