# import the dependencies

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# tittle
st.markdown("<h1 style='text-align: center; color: red;'>MULTIPLE DISEASE PREDICTION BY USING ML </h1>", unsafe_allow_html=True)

#load the picke file

diabetes_model = pickle.load(open("diabetes_model.sav","rb"))
heart_diseas_model = pickle.load(open("heart_disease_model.sav","rb"))
parkinsons_model = pickle.load(open("parkinsons_model.sav","rb"))


#disease choice
with st.sidebar:
	
	selected = option_menu("Multiple Diseas Prediction System",["Diabetes Prediction","Heart Disease Prediction","Parkinsons Prediction"],
	icons = ["activity","heart","person"],default_index=1)

# diabetes prediction
try:
    if (selected == "Diabetes Prediction"):
        st.title("Diabetes Prediction using ML")
        col1, col2 = st.columns(2)
        with col1:
            Pregnancies = st.text_input('Number of Pregnancies')
        with col2:
            Glucose = st.text_input('Glucose Level')
        with col1:
            BloodPressure = st.text_input('Blood Pressure value')
        with col2:
            SkinThickness = st.text_input('Skin Thickness value')
        with col1:
            Insulin = st.text_input('Insulin Level')
        with col2:
            BMI = st.text_input('BMI value')
        with col1:
            DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
        with col2:
            Age = st.text_input('Age of the Person')
        diab_diagnosis = ''
        if st.button('Diabetes Test Result'):
            diabetes_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
            if (diabetes_prediction[0] == 1):
                diabetes_diagnosis = 'The person is diabetic'
            else:
                diabetes_diagnosis = 'The person is not diabetic'
        st.success(diabetes_diagnosis)
        
except:
    st.error(f"PLEASE ENTER THE CORRECT VALUE")

# heart disease prediction
if (selected == "Parkinsons Prediction"):
	st.title("Parkinson's Disease Prediction using ML")
	col1, col2, col3 = st.columns(3)
	with col1:
		fo = st.text_input('MDVP:Fo(Hz)')
	with col2:
		fhi = st.text_input('MDVP:Fhi(Hz)')
	with col3:
		flo = st.text_input('MDVP:Flo(Hz)')
	with col1:
		Jitter_percent = st.text_input('MDVP:Jitter(%)')
	with col2:
		Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
	with col3:
		RAP = st.text_input('MDVP:RAP')
	with col1:
		PPQ = st.text_input('MDVP:PPQ')
	with col2:
		DDP = st.text_input('Jitter:DDP')
	with col3:
		Shimmer = st.text_input('MDVP:Shimmer')
	with col1:
		Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
	with col2:
		APQ3 = st.text_input('Shimmer:APQ3')
	with col3:
		APQ5 = st.text_input('Shimmer:APQ5')
	with col1:
		APQ = st.text_input('MDVP:APQ')
	with col2:
		DDA = st.text_input('Shimmer:DDA')
	with col3:
		NHR = st.text_input('NHR')
	with col1:
		HNR = st.text_input('HNR')
	with col2:
		RPDE = st.text_input('RPDE')
	with col3:
		DFA = st.text_input('DFA')
	with col1:
		spread1 = st.text_input('spread1')
	with col2:
		spread2 = st.text_input('spread2')
	with col3:
		D2 = st.text_input('D2')
	with col1:
		PPE = st.text_input('PPE')
	parkinsons_diagnosis = ''
	if st.button("Parkinson's Test Result"):
		parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
		if (parkinsons_prediction[0] == 1):
			parkinsons_diagnosis = "The person has Parkinson's disease"
		else:
			parkinsons_diagnosis = "The person does not have Parkinson's disease"
	st.success(parkinsons_diagnosis)
