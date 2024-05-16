from hello_you(1) import sad_you()
import streamlit as st 
st.title("Accha ji mai hara chaloo maaan jaoooo na")
ip = st.text_input("Enter here")
if st.button("click me"):
  st.write(sad_you(ip))

