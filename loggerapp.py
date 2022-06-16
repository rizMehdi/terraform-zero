import streamlit as st
st.header("Welcome to Terraform Zero")


pictureready=False

form = st.form("my_form")

picture = form.camera_input("First, take a picture of the tree")
if picture is not None:
  #st.image(picture)
  pictureready=True

  
  
  
loggername = form.text_input("your name (optional)")
otherinfo = form.text_input("add any other comments here, like damage to tree etc")

# Now add a submit button to the form:
if pictureready==True:
  form.form_submit_button("Submit Report")
