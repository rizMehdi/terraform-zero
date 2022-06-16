import streamlit as st
#import SessionState

st.header("Welcome to Terraform Zero")
st.markdown("""
<style>
write {
  unicode-bidi:bidi-override;
  direction: RTL;
}
</style>
    """, unsafe_allow_html=True)

st.markdown(
    """
    <link href="//db.onlinewebfonts.com/c/6b75b24d502dab23003320c2e1b2fc68?family=Adobe+Arabic" rel="stylesheet" type="text/css"/>
    <style> bdi {font-family: 'Adobe Arabic';}</style>

    <p><bdi>ٹیرافارم</bdi></p>
    """,
    unsafe_allow_html=True,
)


#session_state = SessionState.get(checkboxed=False)

sent=False
buttonDisabled=True

if sent is False:
  #form = st.form("my_form")
  picture = st.camera_input("First, take a picture of the tree")
  if picture is not None:
    #st.image(picture)
    buttonDisabled=False




  loggername = st.text_input("your name (optional)")
  isDead=  st.checkbox("Click here if the tree is damaged or dead")
  needsHelp= st.checkbox("Click here if the tree needs immediate attention/care by Greensquad team")

  otherinfo = st.text_input("add any other comments here, like the extent of damage to tree etc")



  if st.button("Submit Report",disabled=buttonDisabled):
    sent=True
    st.write("Report sent. Thanks a lot")
    #if st.button('Click here for making a new report') or session_state.checkboxed:
     # session_state.checkboxed = True

  if buttonDisabled==True:
    st.warning("Take a picture before submitting")
else:
  st.write("Report sent. Thanks a lot....")
  

