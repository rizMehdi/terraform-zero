import streamlit as st
picture = st.camera_input("First, take a picture...")
if picture is not None:
  st.image(picture)
