import streamlit as st
import random

# generating varibale

st.set_page_config(page_title="Guess the number", page_icon=":smiley:", layout="centered")
st.title("Guess the number")    
st.write("Get Ready to play the game")

low = 1
high = 100
guesses = 0

# number = random.randint(low,high)

# while True:
#     guess = st.number_input(f"Enter number between ({low} - {high}) ", min_value=low, max_value=high)
#     guesses +=1
#     if guess < number:
#        st.write(f"{guess} is too low")
#     elif guess > number:
#         st.write(f"{guess} is too high")
#     else:
#         st.write(f"you guessed the number in {guesses} guesses")
#         break   
    
number = random.randint(low, high)

guess = st.number_input(f"Enter number between ({low} - {high})", min_value=low, max_value=high)
guesses = 0

if st.button("Submit"):
    guesses += 1
    if guess < number:
        st.write(f"{guess} is too low")
    elif guess > number:
        st.write(f"{guess} is too high") 
    else:
        st.write(f"You guessed the number in {guesses} guesses!")
        st.balloons()



