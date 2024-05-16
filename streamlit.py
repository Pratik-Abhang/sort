import streamlit as st

def sad_you(ip):
    if ip == 'i love you':
        return ["Well, I found a woman, stronger than anyone I know<br> She shares my dreams, I hope that someday Ill share her home<br> I found a lover, to carry more than just my secrets To carry love, to carry children of our own"]
    elif ip == 'i hate you':
        return "We are still kids, but we're so in love Fighting against all odds<br> I know we'll be alright this time<br> Darling, just hold my hand Be my girl, I'll be your man<br> I see my future in your eyes"
    elif ip == 'i am mad at you':
        return "we were just kids when we fell in love<br> Not knowing what it was<br> I will not give you up this time<br> But darling, just kiss me slow<br> Your heart is all I own<br> And in your eyes, you're holding mine"
    elif ip == 'maska nko maru':
        return "I have faith in what I see<br> Now I know I have met an angel in person<br> And she looks perfect"
    elif ip == 'its ok':
        return "I don't deserve this<br>You look perfect tonight"
    elif ip == 'mg':
        return "Baby, I'm dancing in the dark<br> With you between my arms<br> Barefoot on the grass<br> Listening to our favourite song<br> When you said you looked a mess<br> I whispered underneath my breath<br> But you heard it<br> Darling, you look perfect tonight"
    elif ip == 'i dont want to talk':
        return "I found a love, for me<br> Darling, just dive right in and follow my lead<br> Well, I found a girl, beautiful and sweet<br> Oh, I never knew you were the someone waiting for me"
    else:
        return "I have faith in what I see<br> Now I know I have met an angel in person<br> And she looks perfect<br> I don't deserve this<br>You look perfect tonight"

st.title("Acchaaa ji mai hara chaloooo maaannn jaoo na")
ip = st.text_input("Enter here")
if st.button("click me"):
    st.markdown(sad_you(ip), unsafe_allow_html=True)
