import base64
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import streamlit_authenticator as stauth

# loading the saved models
diabetes_model = pickle.load(open('F:/New chapter/PG/DSA/Behredin_Disease_Pr/diabetes_model.sav','rb'))
heart_disease_model = pickle.load(open('F:/New chapter/PG/DSA/Behredin_Disease_Pr/heart_disease_model.sav','rb'))
breast_disease_model = pickle.load(open('F:/New chapter/PG/DSA/Behredin_Disease_Pr/breast_disease_model.sav', 'rb'))

def creds_entered():
    if st.session_state["user"].strip() =="behre" and st.session_state["passwd"].strip() =="redi":
       st.session_state["authenticated"]=True
    else:
        st.session_state["authenticated"]=False
        st.error("Invalid username or password :face_with_raised_eyebrow:")
def authenticate_user():
    if "authenticated" not in st.session_state:
            st.text_input(label="UserName: ",value="",key="user",on_change=creds_entered)
            st.text_input(label="Password :",value="",key="passwd",type="password",on_change=creds_entered)
            return False
    else:
            if st.session_state["authenticated"]:
                return True
            else:
                    st.text_input(label="UserName: ",value="",key="user",on_change=creds_entered)
                    st.text_input(label="Password :",value="",key="passwd",type="password",on_change=creds_entered)
                    return False
if authenticate_user():
        with st.sidebar:
            selected = option_menu(menu_title="Main Menu", options=['Home','Prediction','Data Analysis','About'],
                                    icons=['house','book','envelope','list'],orientation="Horizontal",
            styles={
            "container":{"background-color":"#EC7063"},
                "nav-link":{"font-size":"21px","--hover-color":"#C843335","color":"#17202A" },
                "nav-link-selected":{"background-color":"#F8F521"},
                "icon":{"font-size":"20px" }}, )
        if(selected=="Home"):
            st.markdown("""
            <style>
            .big-foot1{font-size:50px|important;color:green;text-align:center;font-weight:bold;background-color:yellow;}
            </style>
            """,unsafe_allow_html=True)
            st.markdown('<h1 class="big-foot1">Fundamentals of Data Science and Analytics Project</h1>',unsafe_allow_html=True)
            st.markdown('<h3 style=color:red>Hello  Welcome to My Multi Disease Prediction App </h3>',unsafe_allow_html=True)
            st.subheader("To use this streamlit app for prediction please click Prediction button from main menu ")
            st.markdown('<h1 style="text-align:center;font-weight: bold; background-color:green">እንኳን ደህና መጡ። ይህ የMulti Disease Prediction Dashboard ነው። </p>',unsafe_allow_html=True)
        if(selected=='Prediction'):
            #labe=st.sidebar
            #username=labe.text_input("User Name")
            #password=st.sidebar.text_input("Password",type='password')
            #st.sidebar.button("Login")
            #if password=="behre1234" and username=='behredin':
             #   if(len(password)>=8 and len(username)>=5):
                        #st.balloons()
                    select=option_menu( menu_title=None, options=['Help','Heart Disease','Diabetes','Breast_Cancer'],
                        icons=['question','heart','list','envelope'],orientation="horizontal",
                        styles={
                        "container":{ "background-color":"green"} },  )
                    if(select=='Help'):
                                st.markdown('<h3 style=color:green>Hello  Welcome to my Multi Disease Prediction Dashboard </h3>',unsafe_allow_html=True)
                                st.markdown("If you want to check any one of three disease please select from the above menu and fill the given form properly by looking from the given dataset and finally click :red[check Result] Button below")
                                st.markdown("If You want to see data Analysis please click :green[data set] menu from left side corner")
                            # Diabetes Prediction Page
                    if (select == 'Diabetes'):    
                        st.title('Diabetes Prediction Dashboard')
                    # getting the input data from the user
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            Pregnancies = st.text_input('Number of Pregnancies')
                        with col2:
                            Glucose = st.text_input('Glucose Level')
                        with col3:
                            BloodPressure = st.text_input('Blood Pressure value')
                        with col1:
                            SkinThickness = st.text_input('Skin Thickness value')
                        with col2:
                            Insulin = st.text_input('Insulin Level')
                        with col3:
                            BMI = st.text_input('BMI value')
                        with col1:
                            DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
                        with col2:
                            Age = st.text_input('Age of the Person')
                        # code for Prediction
                        diab_diagnosis = ''
                        # creating a button for Prediction
                        if st.button('Check Result'):
                            diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])               
                            if (diab_prediction[0] == 1):
                                diab_diagnosis = 'Sorry the person is diabetic'
                                #st.write("If you want any advice please click the given checkbo button")
                                #st.checkbox("Advice")
                            else:
                                diab_diagnosis = 'The person is not diabetic'                
                        st.success(diab_diagnosis)
                    # Heart Disease Prediction Page

                    if (select == 'Heart Disease'):    
                    # page title
                        st.title(':green[Heart Disease Prediction Dashboard]')
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            age = st.text_input('Age')
                        with col2:
                                sex = st.selectbox('Sex',(0,1))
                        with col3:
                            cp = st.selectbox('Chest Pain types',(0,1,2,3))
                        with col1:
                            trestbps = st.text_input('Resting Blood Pressure')
                        with col2:
                            chol = st.text_input('Serum Cholestoral in mg/dl')
                        with col3:
                            fbs = st.selectbox('Fasting Blood Sugar',(0,1))
                        with col1:
                            restecg = st.text_input('Resting Electrocardiographic results')
                        with col2:
                            thalach = st.text_input('Maximum Heart Rate achieved')
                        with col3:
                            exang = st.selectbox('Exercise Induced Angina',(0,1))
                        with col1:
                            oldpeak = st.text_input('ST depression induced by exercise')
                        with col2:
                            slope = st.text_input('Slope of the peak exercise ST segment')
                        with col3:
                            ca = st.selectbox('Major vessels colored by flourosopy',(0,1,2))
                        with col1:
                            thal = st.selectbox('thal: ',(0,1,2,3))
                            # code for Prediction
                        heart_diagnosis = ''
                        # creating a button for Prediction
                        if st.button('Check Result'):
                            heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])                          
                            if (heart_prediction[0] == 1):
                                heart_diagnosis = 'Sorry The person is having heart disease'
                        else:
                            heart_diagnosis = 'The person does not have any heart disease'
                        st.success(heart_diagnosis)
                    # Parkinson's Prediction Page
                    if (select == "Breast_Cancer"):
                        st.subheader("Breast Cancer Disease Prediction Dashboard")
                        col1, col2, col3 = st.columns(3)  
                        with col1:
                            mr = st.text_input('mean_radius')
                        with col2:
                            mt = st.text_input('mean_texture')
                        with col3:
                            mp = st.text_input('mean_perimeter')
                        with col1:
                            ma = st.text_input('mean_area')
                        with col2:
                            ms = st.text_input('mean_smoothness')
                    # code for Prediction
                        cancer_diagnosis = ''
                    # creating a button for Prediction    
                        if st.button("Check Result"):
                            cancer_prediction = breast_disease_model.predict([[mr, mt, mp, ma, ms]])                          
                            if (cancer_prediction[0] == 1):
                                cancer_diagnosis = "Sorry The person has Breast_Cancer Disease"
                                #st.write("If you want any first Aid please Advice button below")
                                #if st.checkbox("Advice"):
                                #   st.write("please go to nearby hospital")
                            else:
                                cancer_diagnosis = "The person does not have Breast_Cancer Dsisease"
                        st.success(cancer_diagnosis)
        #else:
         #           st.warning("Please Enter Correct Username and Password to Acces Prediction Dashboard")
        if(selected=="Data Analysis"):
            st.markdown("""
                <style>
                    .big-foot1{font-size:50px|important;color:green;text-align:center;font-weight:bold;background-color:yellow;}</style>
                """,unsafe_allow_html=True)
            st.markdown('<h1 class="big-foot1">Data Analysis</h1>',unsafe_allow_html=True)
            select=option_menu(menu_title=None,options=['Home','Heart Disease Dataset','Diabetes Disease Dataset','Breast_Cancer Disease Dataset'],orientation="Horizontal",)
            if select=='Heart Disease Dataset':
                heart = pd.read_csv('F:/New chapter/PG/DSA/Behredin_Disease_Pr/heart.csv')
                st.markdown('<h5 style=color:green;background-color:black;font-size:30px> Heart Dataset</h5>',unsafe_allow_html=True)
                if st.checkbox("Dataset"):
                    st.dataframe(heart.head(20))
                    st.subheader('Visualization')
                    st.bar_chart(heart)
                if st.checkbox('Display rows and Column Shape'):
                    st.write(heart.shape)
                if st.checkbox('Display Heatmap'):
                        st.write(sns.heatmap(heart.corr(),linewidths=1.0))
                        st.set_option('deprecation.showPyplotGlobalUse', False)
                        st.pyplot()
                if st.checkbox('Select Multiple Columns'):
                        selected_columns=st.multiselect('Please Select prefered columns:',heart.columns)
                        df1=heart[selected_columns]
                        st.dataframe(df1)
                if st.checkbox('Display Summary'):
                        st.write(heart.describe().T)
            if select=='Diabetes Disease Dataset':
                diabetes = pd.read_csv('F:/New chapter/PG/DSA/Behredin_Disease_Pr/diabetes.csv')
                st.markdown('<h5 style=color:blue;background-color:black;font-size:30px> Diabetes Dataset</h5>',unsafe_allow_html=True)
                if st.checkbox("Dataset"):
                    st.dataframe(diabetes.head(20))
                    st.subheader('Visualization')
                    st.bar_chart(diabetes)
                if st.checkbox('Display rows and Column Shape'):
                    st.write(diabetes.shape)      
                if st.checkbox('Display Heatmap'):
                        st.write(sns.heatmap(diabetes.corr(),linewidths=1.0))
                        st.set_option('deprecation.showPyplotGlobalUse', False)
                        st.pyplot()
                if st.checkbox('Select Multiple Columns'):
                        selected_columns=st.multiselect('Please Select prefered columns:',diabetes.columns)
                        df1=diabetes[selected_columns]
                        st.dataframe(df1)
                if st.checkbox('Display Summary'):
                        st.write(diabetes.describe().T)
            if select=='Breast_Cancer Disease Dataset':
                parkin = pd.read_csv('F:/New chapter/PG/DSA/Behredin_Disease_Pr/Breast_cancer_data.csv')
                st.markdown('<h5 style=color:yellow;background-color:black;font-size:30px> Breast_Cancer Dataset</h5>',unsafe_allow_html=True)
                if st.checkbox("Dataset"):
                    st.dataframe(parkin.head(20))
                    st.subheader('Visualization')
                    st.bar_chart(parkin)
                if st.checkbox('Display rows and Column Shape'):
                    st.write(parkin.shape)
                if st.checkbox('Display Heatmap'):
                        st.write(sns.heatmap(parkin.corr(),linewidths=1.0))
                        st.set_option('deprecation.showPyplotGlobalUse', False)
                        st.pyplot()
                if st.checkbox('Select Multiple Columns'):
                        selected_columns=st.multiselect('Please Select prefered columns:',parkin.columns)
                        df1=parkin[selected_columns]
                        st.dataframe(df1)
                if st.checkbox('Display Summary'):
                        st.write(parkin.describe().T)
        if(selected=="About"):
                st.markdown('<h4>One of my Goal is Creating Multiple Disease prediction that predicts three types of disease based on the given Data set. </h4> ',unsafe_allow_html=True)
                if st.checkbox("Owner of the app"):
                    st.markdown("""
                <style>
                .behre{font-size:20px;text-align:justify;font:weight:bold;}
                .behre1{font-size:200%;font-weight:bold;color:green;text-align:justify;}
                </style>
                """,unsafe_allow_html=True)
                    image = Image.open('F:/New chapter/PG/DSA/Behredin_Disease_Pr/aa.jpg')
                    st.image(image,width=300)
                    st.title("Name : BEHREDIN REDI YILMA")
                    st.markdown('<p class="behre1">Jimma Institute of Technology</p>',unsafe_allow_html=True)
                    st.markdown('<p class="behre">Program : Msc in Artificial Intelligence</p>',unsafe_allow_html=True)
                    st.markdown('<p class="behre">Phone Number : 0932632526</p>',unsafe_allow_html=True)
                    st.markdown('<p class="behre">Email : behreredi5497@gmail.com</p>',unsafe_allow_html=True)
                    st.markdown('<p class="behre1">Year : @ May 2023 GC</p>',unsafe_allow_html=True)