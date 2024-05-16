import requests
import importlib.util

# URL of the raw .py file on GitHub
github_url = "hello_you (1).py"

# Fetching the content of the .py file
response = requests.get(github_url)
code = response.text

# Executing the code to make the function available
exec(code)

# Now you can use the function
sad_you()

import streamlit as st 
from hello_you import sad_you()
st.title("Accha ji mai hara chaloo maaan jaoooo na")
ip = st.text_input("Enter here")
if st.button("click me"):
  st.write(sad_you(ip))

