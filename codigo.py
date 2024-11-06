import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.sidebar.title("my first barra lateral")
st.sidebar.header("holis barra lateral")
st.sidebar.write("esto es una barra lateral")

st.sidebar.image("ESdyfEIXcAEArWx.jpg")

if st.sidebar.button("haz clik in the barra lateral"):
    st.sidebar.write("clik hecho")

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Función para dibujar el gráfico
def plot_chart(color):
    x = np.arange(10)
    y = np.random.randint(1, 10, size=10)
    plt.bar(x, y, color=color)
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    st.pyplot(plt.gcf())

# Opciones de colores
color_options = {
    'Rojo': 'red',
    'Azul': 'blue',
    'Dorado': 'gold',
    'Rosado': 'pink'
}

# Crear un selectbox para elegir el color
color_choice = st.selectbox('Cambia el color del gráfico', list(color_options.keys()))

# Dibujar el gráfico con el color seleccionado
plot_chart(color_options[color_choice])

user_input = st.sidebar.text_input("esribe algo")
st.sidebar.write(f"escribiste in the barra: ", user_input)
