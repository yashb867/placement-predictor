from turtle import width
import streamlit as st

from pages import utils
import matplotlib.pyplot as plt
import pandas as pd
import os

admin = {
	"admin@gmail.com" : "password",
	"admin1@gmail.com" : "password",
	"admin2@gmail.com" : "password"
}

def app():
	logger = st.empty()
	status = 0
	with logger.form('login_form'):
		st.markdown("### Enter your credentials")
		email = st.text_input('Enter your email')
		password = st.text_input('Enter your password', type='password')
		submitted = st.form_submit_button("Log IN")
		if submitted:
			try:
				ad = admin[email]
				if password == ad:
					st.write('Login Successful')
					logger.empty()
					status = 1
				else:
					st.write('User not found/incorrect password')
			except:
				st.write('User not found/incorrect password')
	if status == 1:
		admin_dashboard()


def admin_dashboard():
	st.markdown('## Showing detailed analysis')
	df = pd.read_csv('student_data.csv')
	with st.container():
		st.markdown('### Showing data')
		st.write(df)

	with st.container():
		st.markdown('#### Department wise placed unplaced ratio')
		e_placed = len(df.query('Predicted > 0 and Stream == "Electrical"'))
		e_unplaced = len(df.query('Predicted == 0 and Stream == "Electrical"'))
		
		c_placed = len(df.query('Predicted > 0 and Stream == "Civil"'))
		c_unplaced = len(df.query('Predicted == 0 and Stream == "Civil"'))
		
		cs_placed = len(df.query('Predicted > 0 and Stream == "Computer Science"'))
		cs_unplaced = len(df.query('Predicted == 0 and Stream == "Computer Science"'))
		
		m_placed = len(df.query('Predicted > 0 and Stream == "Mechanical"'))
		m_unplaced = len(df.query('Predicted == 0 and Stream == "Mechanical"'))
		
		it_placed = len(df.query('Predicted > 0 and Stream == "Information Technology"'))
		it_unplaced = len(df.query('Predicted == 0 and Stream == "Information Technology"'))
		
		entc_placed = len(df.query('Predicted > 0 and Stream == "Electronics And Communication"'))
		entc_unplaced = len(df.query('Predicted == 0 and Stream == "Electronics And Communication"'))
		
		labels = ['Electrical', 'Civil', 'CS', 'Mechanical', 'IT', 'ENTC']
		placed = [e_placed, c_placed, cs_placed, m_placed, it_placed, entc_placed]
		unplaced = [e_unplaced, c_unplaced, cs_unplaced, m_unplaced, it_unplaced, entc_unplaced]
		w = 0.6
		fig2, ax1 = plt.subplots()
		ax1.bar(labels, placed, w)
		ax1.bar(labels, unplaced, w, bottom=placed)
		ax1.legend(['Placed', 'Unplaced'])
		st.pyplot(fig2)

	with st.container():
		st.markdown('#### Total students predicted:')
		placed = df.query('Predicted > 0')
		len_placed = len(placed)
		unplaced = df.query('Predicted == 0')
		len_unplaced = len(unplaced)
		sizes = [len_placed, len_unplaced]
		labels = ["Placed Students", "Unplaced Students"]
		fig1, ax1 = plt.subplots()
		ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True)
		ax1.axis('equal')
		st.pyplot(fig1, width=250)

	with st.container():
		st.markdown('#### Total students predicted by branches:')
		placed = df.query('Predicted > 0')
		labels = ['Electrical', 'Civil', 'Computer Science', 'Mechanical', 'Information Technology', 'Electronics And Communication']
		sizes = [len(df.query('Stream == "Electrical"')), len(df.query("Stream == 'Civil'")), len(df.query("Stream == 'Computer Science'")), len(df.query("Stream == 'Mechanical'")), len(df.query("Stream == 'Information Technology'")),len(df.query("Stream == 'Electronics And Communication'")) ]
		fig2, ax2 = plt.subplots()
		ax2.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True)
		ax2.axis('equal')
		st.pyplot(fig2, width=250)
	
	
	
