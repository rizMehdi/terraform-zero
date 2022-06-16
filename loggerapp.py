import streamlit as st
st.header("Welcome to Terraform Zero")


buttonDisabled=True

#form = st.form("my_form")

picture = st.camera_input("First, take a picture of the tree")
if picture is not None:
  #st.image(picture)
  buttonDisabled=False

  
  
  
loggername = st.text_input("your name (optional)")
isDead=  st.checkbox("Click here if the tree is damaged or dead")
needsHelp= st.checkbox("Click here if the tree needs immediate attention/care by Greensquad team")

otherinfo = st.text_input("add any other comments here, like the extent of damage to tree etc")



st.button("Submit Report",disabled=buttonDisabled)
# Now add a submit button to the form:
if buttonDisabled==True:
  st.warning("Take a picture before submitting")
 
