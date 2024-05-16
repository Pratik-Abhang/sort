import requests
import importlib.util

# URL of the raw .py file on GitHub
github_url = "https://github.com/Pratik-Abhang/sort/blob/main/hello_you%20(1).py"

# Fetching the content of the .py file
response = requests.get(github_url)
code = response.text

# Executing the code to make the function available
exec(code)

import streamlit as st 

def sad_you(ip):
    if ip=='i love you':
        print("Well, I found a woman, stronger than anyone I know\n She shares my dreams, I hope that someday Ill share her home\n I found a lover, to carry more than just my secrets To carry love, to carry children of our own")
    elif ip=='i hate you':
        print("We are still kids, but we're so in love Fighting against all odds\n I know we'll be alright this time\n Darling, just hold my hand Be my girl, I'll be your man\n I see my future in your eyes")
    elif ip=='i am mad at you':
        print("we were just kids when we fell in love\n Not knowing what it was\n I will not give you up this time\n But darling, just kiss me slow\n Your heart is all I own\n And in your eyes, you're holding mine")
    elif ip=='maska nko maru':
        print("I have faith in what I see\n Now I know I have met an angel in person\n And she looks perfect")
    elif ip=='its ok':
        print("I don't deserve this\nYou look perfect tonight")
    elif ip=='mg':
        print("Baby, I'm dancing in the dark\n With you between my arms\n Barefoot on the grass\n Listening to our favourite song\n When you said you looked a mess\n I whispered underneath my breath\n But you heard it\n Darling, you look perfect tonight")
    elif ip=='i dont want to talk':
        print("I found a love, for me\n Darling, just dive right in and follow my lead\n Well, I found a girl, beautiful and sweet\n Oh, I never knew you were the someone waiting for me\n")
    else:
        print("I have faith in what I see\n Now I know I have met an angel in person\n And she looks perfect\n I don't deserve this\nYou look perfect tonight")
        

st.title("Accha ji mai hara chaloo maaan jaoooo na")
ip = st.text_input("Enter here")
if st.button("click me"):
  st.write(sad_you(ip))

