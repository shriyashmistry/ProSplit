import streamlit as st

st.title("SplitSmart")
st.write("Split expenses with friends and keep track of your budget.")

name = st.text_input("What's your name?", "")

if name:
    st.write(f"Hello, {name}!")