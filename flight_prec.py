import streamlit as st
import time
from datetime import date
from datetime import datetime
import pickle


model_file = open("flight_predict.pkl","rb")
regressor=pickle.load(model_file)

def main():
    html_temp = """
        <div style="background-color:purple;padding:10px">
        <h2 style="color:black;text-align:center;">Flight Price Predictor </h2>
        </div>
        """
    st.markdown(html_temp,unsafe_allow_html=True)

    #Airline selection
    airline = st.selectbox('Airlines',('Air Asia', 'Air India', 'Go Air',
           'IndiGo', 'Jet Airways', 'Jet Airways Business',
           'Multiple carriers',
           'Multiple carriers Premium economy', 'SpiceJet',
           'Vistara', 'Vistara Premium economy'))

    #Source selection
    source=st.selectbox('Source',('Kolkata','Banglore', 'Chennai', 'Delhi',
            'Mumbai'))

    #Destination  selection
    destination=st.selectbox('Destination',('New Delhi','Kolkata','Banglore', 'Hyderabad', 'Cochin'))
    if source==destination:
        st.error('Source and Destination cannot be the same please select other option')
    #Stoppage selection
    stoppage=st.selectbox('Stoppage',(0,1,2,3,4))

    #Journey date
    date=st.date_input('Date of Journey')
    if date<date.today():
        st.error('You are selecting the day which has already been passed ,kindly change the date')

    #Departure time
    dep_time=st.time_input('Departure Time')

    #Arrival time
    arr_time=st.time_input('Arrival Time',value=datetime.strptime('2020-12-29T14:45:25Z', '%Y-%m-%dT%H:%M:%SZ'))



    #Chosing date of journey
    date_of_journey=date.day

    #chosing month of journey
    month_of_journey=date.month


    #taking hour of departure
    dep_hour=dep_time.hour

    #taking minute of departure
    dep_min=dep_time.minute

    #Arrival hour
    arr_hour=arr_time.hour

    #Arrival minute
    arr_min=arr_time.minute

    #Duration Hour
    dur_hour=abs(dep_hour - arr_hour)

    #Duration Minute
    dur_min=abs(dep_min - arr_min)

    #displaying error
    if dur_hour==0 and dur_min==0:
        st.error('Departure Time and Arrival Time cannot be the same')

    #Displaying duration
    st.markdown(f'Duration: {dur_hour} Hour {dur_min} Min')
    
    if st.button("Predict" ):
        progress = st.progress(0 )
        for i in range(100):
            time.sleep(0.001)
            progress.progress(i+1)

        result=flight_predictor(stoppage,airline,source,destination,
        date_of_journey,
        month_of_journey,
        dep_hour,
        dep_min,
        arr_hour,
        arr_min,
        dur_hour,
        dur_min)
        st.success(f"Your appromimate flight price  is  {result}")
        st.balloons()
    st.error("*Disclaimer: This flight price doesn't guaranteed you the actual on kindly! visit the respective airline website")
    html= """
        <div style="background-color:purple;padding:3px">
        <h3 style="color:black;text-align:center;">@Copyright Md Tausif </h3>
        </div>
        """
    st.markdown(html,unsafe_allow_html=True)

    #flight predictor function
def flight_predictor(stoppage,airline,source,destination,date_of_journey,month_of_journey,dep_hour,dep_min,arr_hour,arr_min,dur_hour,dur_min):
    Air_Asia=Air_India=Go_Air=IndiGo=Jet_Airways=Jet_Airways_Business=0
    Multiple_carriers=Multiple_carriers_Premium_economy=SpiceJet=Vistara=0
    Vistara_Premium_economy=0
    sor_Banglore=sor_Chennai=sor_Kolkata=sor_Mumbai=sor_Delhi=0
    dest_Banglore=dest_Hyderabad=dest_Kolkata=dest_New_Delhi=dest_Cochin=0

    if  airline=='Air Asia':
        Air_Asia=1
    elif airline=='Air India':
        Air_India=1
    elif airline=='Go Air':
        Go_Air=1
    elif airline=='IndiGo':
        IndiGo=1
    elif airline=='Jet Airways':
        Jet_Airways=1
    elif airline=='Jet Airways Business':
        Jet_Airways_Business=1
    elif airline=='Multiple carriers':
        Multiple_carriers=1
    elif airline=='Multiple carriers Premium economy':
        Multiple_carriers_Premium_economy=1
    elif airline=='SpiceJet':
        SpiceJet=1
    elif airline=='Vistara':
        Vistara=1
    elif airline =='Vistara Premium economy':
       Vistara_Premium_economy=1
    else:
        Air_Asia=0,
        Air_India=0,
        Go_Air=0,
        IndiGo=0,
        Jet_Airways=0,
        Jet_Airways_Business=0,
        Multiple_carriers=0,
        Multiple_carriers_Premium_economy=0,
        SpiceJet=0,
        Vistara=0,
        Vistara_Premium_economy=0

#Source selection
    if  source =='Bangalore':
        sor_Banglore=1

    elif source=='Chennai':
        sor_Chennai=1

    elif source=='Delhi':
        sor_Delhi=1

    elif source=='Kolkata':
        sor_Kolkata=1

    elif source=='Mumbai':
        sor_Mumbai=1
    else:
        sor_Banglore=0,
        sor_Chennai=0,
        sor_Delhi=0,
        sor_Kolkata=0,
        sor_Mumbai=0

#Destination selection

    if destination=='Banglore':
        dest_Banglore=1
    elif destination=='Cochin':
        dest_Cochin=1
    elif destination=='Hyderabad':
        dest_Hyderabad=1
    elif destination=='Kolkata':
        dest_Banglore=1
    elif destination=='New Delhi':
        dest_New_Delhi=1
    else:
        dest_Banglore=0,
        dest_Cochin=0,
        dest_Hyderabad=0,
        dest_Kolkata=0,
        dest_New_Delhi=0

#Stoppage#

#    if stoppage=='One stop':
#        One_stop=1
#    elif stoppage=='Two stop':
#        Two_stop=2
#    elif stoppage=='Three stop':
#        Three_stop=3
#    elif stoppage=='Four stop':
#        Four_stop=4
#    elif stoppage=='Non stop':
#        Non_stop=0
#    else:
#        One_stop

#prediction function
    price=regressor.predict([[stoppage,
        Air_Asia,
        Air_India,
        Go_Air,
        IndiGo,
        Jet_Airways,
        Jet_Airways_Business,
        Multiple_carriers,
        Multiple_carriers_Premium_economy,
        SpiceJet,
        Vistara,
        Vistara_Premium_economy,
        date_of_journey,
        month_of_journey,
        sor_Banglore,
        sor_Chennai,
        sor_Delhi,
        sor_Kolkata,
        sor_Mumbai,
        dest_Banglore,
        dest_Cochin,
        dest_Hyderabad,
        dest_Kolkata,
        dest_New_Delhi,
        dep_hour,
        dep_min,
        arr_hour,
        arr_min,
        dur_hour,
        dur_min ]])
    return round(price[0],2)
# taking zero index only because it return as a list and rounding off to two decimal

if __name__=='__main__':
    main()







