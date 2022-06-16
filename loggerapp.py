import streamlit as st
st.header("Welcome to Terraform Zero")


buttonDisabled=True

#form = st.form("my_form")

picture = st.camera_input("First, take a picture of the tree")
if picture is not None:
  #st.image(picture)
  buttonDisabled=False

  
  
  
loggername = st.text_input("your name (optional)")
otherinfo = st.text_input("add any other comments here, like damage to tree etc")

st.button("Submit Report",disabled=buttonDisabled)
# Now add a submit button to the form:
if buttonDisabled==True:
  st.write("Take a picture before submitting")
 
