import pandas as pd

import pickle as pk
import streamlit as st


st.set_page_config(page_title='Car Price Prediction ML Model',page_icon=':car:')
model=pk.load(open('model.pkl','rb'))

html_temp = """
		<div style="background-color:#28B463;padding:8px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Multiple_Linear_Regression</h1>
        <h4 style="color:white;text-align:center;"> 🚗Car Price Prediction ML Model..🚙 </h4>
		</div>
		"""
def main():
    st.html(html_temp)

    car_data=pd.read_csv('Cardetails.csv')

    def get_brand_name(car_name):
        car_name=car_name.split(' ')[0]
        return car_name.strip()


        
        return float(value)

    car_data['name']=car_data['name'].apply(get_brand_name)
    # name	year	km_driven	fuel	seller_type	transmission	owner	mileage	engine	seats
    # st.dataframe(car_data)
    name=st.selectbox('Select the Care name: ',car_data['name'].unique())
    year=st.slider('Select the year',1994,2020)
    km_driven=st.slider('Select km_driven: ',11,200000)
    fuel=st.selectbox('Select the Fuel type: ',car_data['fuel'].unique())
    seller_type=st.selectbox('Select Seller_Type: ',car_data['seller_type'].unique())
    transmission=st.selectbox('Select transmission: ',car_data['transmission'].unique())
    owner=st.selectbox('Select Owner: ',car_data['owner'].unique())
    mileage=st.slider('Select mileage: ',10,42)
    engine=st.slider('Select Engine CC: ',700,5000)
    seats=st.slider('No of seats: ',5,10)

    if st.button('predic'):
        input_data_module=pd.DataFrame(
            [[name,year,km_driven,fuel,seller_type,transmission,owner,mileage,engine,seats]],
            columns=['name','year','km_driven','fuel','seller_type','transmission','owner','mileage','engine','seats']
        )
        

        input_data_module['owner'].replace(['First Owner', 'Second Owner', 'Third Owner','Fourth & Above Owner', 'Test Drive Car'],[1,2,3,4,5],inplace=True)
        input_data_module['transmission'].replace(['Manual', 'Automatic'],[1,2],inplace=True)
        input_data_module['seller_type'].replace(['Individual', 'Dealer', 'Trustmark Dealer'],[1,2,3],inplace=True)
        input_data_module['fuel'].replace(['Diesel', 'Petrol', 'LPG', 'CNG'],[1,2,3,4],inplace=True)
        input_data_module['name'].replace(['Maruti', 'Skoda', 'Honda', 'Hyundai', 'Toyota', 'Ford', 'Renault',
        'Mahindra', 'Tata', 'Chevrolet', 'Datsun', 'Jeep', 'Mercedes-Benz',
        'Mitsubishi', 'Audi', 'Volkswagen', 'BMW', 'Nissan', 'Lexus',
        'Jaguar', 'Land', 'MG', 'Volvo', 'Daewoo', 'Kia', 'Fiat', 'Force',
        'Ambassador', 'Ashok', 'Isuzu', 'Opel'],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],inplace=True)

        car_price=model.predict(input_data_module)
        st.success('Car Price is going to be: '+ str(car_price[0].round(2)))


if __name__=='__main__':
    main()