import streamlit as st
import pickle
import os
from pages import utils

# @st.cache
def app():
    st.markdown("## Please Provide the following inputs.")
    st.write("\n")
    
    stream_ = {
        'Electrical': 2, 
        'Civil': 0, 
        'Computer Science': 1, 
        'Mechanical': 5, 
        'Information Technology': 4, 
        'Electronics And Communication': 3
    }
    cgpa_ = {
            8: 3, 
            6: 1,
            5: 0, 
            9: 4, 
            7: 2
    }
    with st.form('input_form'):
        name = st.text_input('Enter your name')
        gender = st.selectbox('Gender', ['Male', 'Female', 'Prefer not to say'])
        stream = st.selectbox('Stream', ['Electrical', 'Civil', 'Computer Science', 'Mechanical', 'Information Technology', 'Electronics And Communication'])
        internship = int(st.radio('Have you done internship?', [0, 1, 2, 3]))
        cgpa = int(st.slider('Select your pointer', 0.00, 10.00))
        hostel = st.radio('Do you stay in hostel?', ['Yes', 'No'])
        backlog = int(st.number_input('Do you have backlogs, if yes specify count ?'))
        submitted = st.form_submit_button("Predict")

        to_add_obj = {
            'Gender' : gender,
            'Stream' : stream,
            'Internship' : internship,
            'CGPA' : cgpa,
            'Hostel' : hostel,
            'Backlog' : backlog
        }

        if submitted:
            if gender == 'Female':
                gender = 0
            else:
                gender = 1
            if hostel == 'Yes':
                hostel = 1
            else:
                hostel = 0
            if backlog == 'Yes':
                backlog = 1
            else:
                backlog = 0
            if cgpa < 5:
                cgpa = 5
            if backlog >= 1:
                backlog = 1
            else:
                backlog = 0
            cgpa = cgpa_[cgpa]
            stream = stream_[stream]

            pp = open(os.getcwd() + '/data/dt_file', 'rb')     
            ppmodel = pickle.load(pp)

            input_arr = [gender, stream, internship, cgpa, hostel, backlog]
            predicted = ppmodel.predict([input_arr])

            predicted = predicted[0]
            to_add_obj['Predicted'] = predicted
            to_add_obj['Name'] = name
            if utils.add_data_to_csv(to_add_obj) == True:
                print("Data Added")
            else:
                print("error adding data")
            if predicted == 1:
                st.markdown("### Congratulations 🥳, You will get placed!")
            else:
                st.markdown("### Sorry, you will need to study hard!📚")

