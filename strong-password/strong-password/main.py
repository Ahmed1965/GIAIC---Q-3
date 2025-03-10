import streamlit as st
import re

st.set_page_config(
    page_title="Password Checker",
    page_icon= "🔒",
    layout="centered",
)
# style
st.markdown("""<style>
            .main {text-align: center;}
            .stTextInput{width:60% !important; margin: auto;}
            .stButton>button{width:50%; background-color: #4CAF50;color:white; font-size: 20px;}
            .stButton>button:hover{background-color: #45a049;}
            .stButton>button:active{background-color: #3e8e41;}`
            </style>""", unsafe_allow_html=True)

st.title('Strong Password Checker')
st.subheader('Check if your password is strong or not')
user = st.text_input('Enter your password', type='password')
if st.button('Check'):
    def password_checker(password):
        if len(password) < 8:
            return 'Password is too short'
        elif len(password) > 20:
            return 'Password is too long'
        elif not re.search("[a-z]", password):
            return 'Password must contain at least one lowercase letter'
        elif not re.search("[A-Z]", password):
            return 'Password must contain at least one uppercase letter'
        elif not re.search("[0-9]", password):
            return 'Password must contain at least one number'
        elif not re.search("[_@$!%^&*()]", password):
            return 'Password must contain at least one special character'
        else:
            return 'Password is strong'
    result = password_checker(user)
    st.write(result)