import streamlit as st
import helper
import pickle

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

# Set page title and layout
st.set_page_config(
    page_title="Duplicate Question Checker",
    page_icon=":mag:",
    layout="centered",
    initial_sidebar_state="auto"
)

# Page title and description
st.title('Duplicate Question Pairs Checker')
st.write('Enter two questions below to check if they are duplicates.')

# Input fields for user to enter questions
q1 = st.text_input('Enter Question 1:')
q2 = st.text_input('Enter Question 2:')

# Button to trigger the comparison
if st.button('Check Duplicate', key='check_button'):
    # Create query point for the model
    query = helper.query_point_creator(q1, q2)
    # Predict using the model
    result = model.predict(query)[0]

    # Display result based on prediction
    if result:
        st.markdown('<div style="background-color: #ff5733; padding: 10px; border-radius: 5px;"><p style="color: white;">These questions are <strong>duplicates</strong>.</p></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div style="background-color: #28a745; padding: 10px; border-radius: 5px;"><p style="color: white;">These questions are <strong>not duplicates</strong>.</p></div>', unsafe_allow_html=True)

