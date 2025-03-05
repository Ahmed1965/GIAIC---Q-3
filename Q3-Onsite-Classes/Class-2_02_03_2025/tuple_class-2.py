import streamlit as st

st.markdown("<h1>Immutable Collections:</h1>", unsafe_allow_html=True)

my_set = {"apple", "banana", "cherry","apple", "Hamaza", "Hamza' marriage"}

st.write(my_set)

word = "Hello world hello python hello world hello python"
word_split = word.split()

unique_list = set(word_split)
for word in word_split:
    if word not in unique_list:
        unique_list.append(word)   
        
        st.write(unique_list)