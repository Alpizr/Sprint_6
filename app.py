import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Venta de coches')

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_checkbox = st.checkbox('Construir histograma') # crear un botón
        
if hist_checkbox: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    st.plotly_chart(fig, use_container_width=True)

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
diagram_checkbox = st.checkbox('Construir diagrama de dispersión')

if diagram_checkbox:
    st.write("Diagrama de dispersión para el conjunto de datos de anuncios de venta de coches")
    fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión

# mostrar un gráfico Plotly interactivos
    st.plotly_chart(fig, use_container_width=True)
    