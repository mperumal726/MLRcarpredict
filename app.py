import pandas as pd
import pickle as pk
import streamlit as st


st.set_page_config(page_title='Car Price Prediction ML Model',page_icon=':car:',layout='wide')
model=pk.load(open('model.pkl','rb'))

#<h4 style="color:white;text-align:center;"> 🚗Car Price Prediction ML Model..🚙 </h4>
html_temp = """
		<div style="background-color:#28B463;padding:08px;border-radius:08px">
		<h1 style="color:white;text-align:center;">🚗 Car Price Predictor..🚙</h1>
		</div>
		"""
m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #28B463;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #FF0000;
    color:##ff99ff;
    }
</style>""", unsafe_allow_html=True)

def main():
        # st.html(html_temp)
    # st.html(html_temp)
    # if st.button('Go to form'):

    car_data=pd.read_csv('Cardetails.csv')

    def get_brand_name(car_name):
        car_name=car_name.split(' ')[0]
        return car_name.strip()         
        return float(value)

    car_data['name']=car_data['name'].apply(get_brand_name)
        # name	year	km_driven	fuel	seller_type	transmission	owner	mileage	engine	seats
        # st.dataframe(car_data)
    st.html(html_temp)
   
    c1,c2,c3=st.columns(3)
    name=c1.selectbox('Select the Care name: ',car_data['name'].unique())
    year=c1.slider('Select the year',1994,2020)
    km_driven=c1.slider('Select km_driven: ',11,200000)
    fuel=c2.selectbox('Select the Fuel type: ',car_data['fuel'].unique())
    seller_type=c2.selectbox('Select Seller_Type: ',car_data['seller_type'].unique())
    transmission=c2.selectbox('Select transmission: ',car_data['transmission'].unique())
    owner=c3.selectbox('Select Owner: ',car_data['owner'].unique())
    mileage=c3.slider('Select mileage: ',10,42)
    engine=c3.slider('Select Engine CC: ',700,5000)
    seats=c1.slider('No of seats: ',5,10)

    if c2.button('predict'):
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
        if car_price>=0:
            c2.success('Car Price is going to be: '+ str(car_price[0].round(2))+'🚙')
            c2.link_button('About-Me😎','https://www.linkedin.com/in/muruga-perumal-iyadurai-7693592a7/')
        else:
            c2.warning('Please select different Car Feature ')
            
        


if __name__=='__main__':
    main()