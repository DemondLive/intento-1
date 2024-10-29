import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.sidebar.title("my first barra lateral")
st.sidebar.header("holis barra lateral")
st.sidebar.write("esto es una barra lateral")

st.sidebar.image("_93356478_trumpyobama1epanov10.jpg")

if st.sidebar.button("haz clik in the barra lateral"):
    st.sidebar.write("clik hecho")

user_input = st.sidebar.text_input("esribe algo")
st.sidebar.write(f"escribiste in the barra: ", user_input)
