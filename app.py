
import streamlit as st

import numpy as np
import pandas as pd
from joblib import load
from PIL import Image
def load_model():
    return load('new_model.jb')
st.set_page_config(
    page_title="House Price Prediction",
    layout='centered',
    page_icon="🛃"
)
def introduction():
    # st.image('vg.gif', width=None)
    st.markdown("""
        
    Name : Prajjwal Singh
    \nQualification : Bachelor ofComputer Application(BCA)
    \nStream : Computer Science
    \nUniversity : University of Lucknow
    \nLocation : Lucknow, INDIA
    \nThis Project Perfrom Prdiction Wheather You Have Donated Blood Or not 
        
        - The Libraries I used in Project are:
            Matplotlib Explore here
            Sklearn Explore Here
            Streamlit Explore here
            Pandas 
            imbelearn 
        - Their Following Tasks are Implemented in the Project:
            Data Preparation and Cleaning
            Model design
            Best Feature Selectio 
            References and Future Work
    """)
    st.markdown("**Datset used**")
    st.caption("Datset used")
 
    df=load('Model/original_data.jb')
    # df=pd.read_csv(url)
    st.write(df)
    st.write("DAta Used FOr Maximum Accuracy:")
    clean_data=load('Model/data.jb')
    st.write(clean_data)
    st.caption("About The Data")
    st.write(	
        '''OverallQual: Rates the overall material and finish of the house

       10	Very Excellent
       9	Excellent
       8	Very Good
       7	Good
       6	Above Average
       5	Average
       4	Below Average
       3	Fair
       2	Poor    
       1	Very Poor''')
    st.write("YearBuilt: Original construction date")
    st.write("TotalBsmtSF: Total square feet of basement area")
    st.write("1stFlrSF: First Floor square feet")
    st.write("GrLivArea: Above grade (ground) living area square feet")
    st.write("FullBath: Full bathrooms above grade")
    st.write("TotRmsAbvGrd: Total rooms above grade (does not include bathrooms)")
    st.write("GarageCars: Size of garage in car capacity")
    st.write("GarageArea: Size of garage in square feet")
    st.write('''KitchenQual: Kitchen quality


       
        Ex	Excellent
       Gd	Good
       TA	Typical/Average
       Fa	Fair
       Po	Poor''')

    st.write('''BsmtQual: Evaluates the height of the basement


        Ex	Excellent (100+ inches)	
       Gd	Good (90-99 inches)
       TA	Typical (80-89 inches)
       Fa	Fair (70-79 inches)
       Po	Poor (<70 inches
       NA	No Basement''')

    st.write('''Foundation: Type of foundation

		
       BrkTil	Brick & Tile
       CBlock	Cinder Block
       PConc	Poured Contrete	
       Slab	Slab
       Stone	Stone
       Wood	Wood''')
    st.write('''
        ExterQual: Evaluates the quality of the material on the exterior 

		
       Ex	Excellent
       Gd	Good
       TA	Average/Typical
       Fa	Fair
       Po	Poor''')
    
    st.write('''
    GarageFinish: Interior finish of the garage


       Fin	Finished
       RFn	Rough Finished	
       Unf	Unfinished
       NA	No Garage''')
def execute():
    
   
    with st.form("form1",clear_on_submit=True):
        st.title("Chrun Prediction for Credit Card")
        inactive_month=st.number_input(" Months_Inactive_12_mon:Number of month from which user has been inactive",min_value=0,max_value=10,step=1)
        Contract_count=st.number_input("Contacts_Count_12_mon: Number of contract",min_value=0,max_value=6,step=1)
        revolving_balance=st.number_input("Total_Revolving_Bal: Total Revolving Balance on the Credit Card",min_value=0,max_value=3000,step=20)
        Transaction_amount=st.number_input("Total_Trans_Amt: Total Transaction Amount",min_value=50,max_value=30000,step=20)
        traction_count=st.number_input("Total_Trans_Ct: Total Transaction Coun",min_value=0,max_value=20,step=1)
        change_transaction_count=st.number_input("Total_Ct_Chng_Q4_Q1: Change in Transaction Count",min_value=0,max_value=10,step=1)
        average_card_ratio=st.number_input("Avg_Utilization_Ratio: Average Card Utilization Ratio",min_value=0,max_value=1)
        btn = st.form_submit_button("Predict Prices")
        if btn:
  
            model=load_model()

            result=np.array([inactive_month,Contract_count,revolving_balance,Transaction_amount,traction_count,change_transaction_count,average_card_ratio])
            result=pd.DataFrame(result).T
            # result=result.rename(columns={0:"OverallQual",1:"YearBuilt"	,2:"YearRemodAdd",	3:"TotalBsmtSF"	,4:"1stFlrSF",5:"GrLivArea"	,6:"FullBath"	,7:"TotRmsAbvGrd",	8:"GarageCars",	9:"GarageArea",10:"ExterQual",11:"Foundation",12:"BsmtQual",13:"KitchenQual",14:"GarageFinish"})
            result=result.rename(columns={0:"Months_Inactive_12_mon",1:"Contacts_Count_12_mon",2:"Total_Revolving_Bal",3:"Total_Trans_Amt",4:"Total_Trans_Ct",5:"Total_Ct_Chng_Q4_Q1",6:"Avg_Utilization_Ratio"})
            print(model.predict(result))
            # st.title(model.predict([result]))
            answer=int(model.predict(result))
            if answer==1:
                st.write("The Customer Will Leave The Bank")
            else:
                st.write("The Customer Will Not Leave The Bank")
           
      

# image=Image.open("house_sale.jpg")

st.header("House Price Prediction ")

options = ['Project Introduction', 'Execution']

sidebar = st.sidebar

sidebar.title('User Options')

selOption = sidebar.selectbox("Select an Option", options)

if selOption == options[0]:
    introduction()
elif selOption == options[1]:
    execute()