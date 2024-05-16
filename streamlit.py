import streamlit as st 
st.title("Accha ji mai hara chaloo maaan jaoooo na")
user_input = st.text_input("Enter here")
if st.button("click me"):
  st.write(sad_you(user_input))

