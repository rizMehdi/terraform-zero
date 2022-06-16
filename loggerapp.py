import streamlit as st
st.header("Welcome to Terraform Zero")
picture = st.camera_input("First, take a picture of the tree")
if picture is not None:
  st.image(picture)


form = st.form("my_form")
loggername = form.input_text("your name (optional)")
otherinfo = form.input_text("add any other comments here, like damage to tree etc")

# Now add a submit button to the form:
form.form_submit_button("Submit Report")
