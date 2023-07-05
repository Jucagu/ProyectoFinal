import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

# Obtener la ruta del archivo .py
ruta_actual = os.path.dirname(os.path.abspath(__file__))

st.title("Despliegue modelo para prediccion de precios de Airbnb")


# Ruta del archivo pickle del modelo descomprimido
ruta_pickle = 'model.pkl'
ruta_pickle = os.path.join(ruta_actual, ruta_pickle)
ruta_scaler = 'normalizador2.pkl'
ruta_scaler = os.path.join(ruta_actual, ruta_scaler)
# Cargar el modelo desde el archivo pickle descomprimido
with open(ruta_pickle, 'rb') as file:
    modelo = pickle.load(file)
# Cargar el normalizador desde el archivo pickle descomprimido
with open(ruta_scaler, 'rb') as file:
    normalizador = pickle.load(file)
# Función para realizar predicciones
def predecir(datos_entrada):
    # Realizar predicciones utilizando el modelo
    predicciones = modelo.predict(datos_entrada)
    # Desnormalizar las predicciones
    predicciones = normalizador.inverse_transform([predicciones])
    return predicciones

# Función para mostrar el resultado de las predicciones
def mostrar_resultados(predicciones):
    # Mostrar el resultado de las predicciones
    st.subheader('El precio estimado es: ' + str(predicciones[0][0]) + '€')
#cajas para ingresar datos
st.sidebar.header('Ingrese los datos de la propiedad')
x1 = st.sidebar.number_input('Latitud', min_value=40.332210, max_value=40.520140, value=40.332210)
x2 = st.sidebar.number_input('Longitud', min_value=-3.835330, max_value=-3.552786, value=-3.835330)
x3 = st.sidebar.number_input('Huéspedes', min_value=1.000000, max_value=16.000000, value=1.000000)
x4 = st.sidebar.number_input('Dormitorios', min_value=1.000000	, max_value=18.000000, value=1.000000)
x5 = st.sidebar.number_input('Camas', min_value=1.000000, max_value=100.0, value=40.000000)
x6 = st.sidebar.number_input('min noches', min_value=1.000000, max_value=1125.000000, value=1.000000)
x7 = st.sidebar.number_input('max noches', min_value=1.000000, max_value=142365.000000, value=1.000000)
x8 = st.sidebar.number_input('Puntaje', min_value=0, max_value=5, value=0)
x9 = st.sidebar.number_input('Casa', min_value=0, max_value=1, value=1)
x10 = st.sidebar.number_input('Hotel', min_value=0, max_value=1, value=0)
x11= st.sidebar.number_input('Habitación privada', min_value=0, max_value=1, value=0)
x12 = st.sidebar.number_input('Habitación compartida', min_value=0, max_value=1, value=0)

# Crear un dataframe con los datos de entrada
datos_entrada = pd.DataFrame({'latitude': x1,
                                'longitude': x2,
                                'accommodates': x3,
                                'bedrooms': x4,
                                'beds': x5,
                                'minimum_nights': x6,
                                'maximum_nights': x7,
                                'review_scores_rating': x8,
                                'Entire home/apt': x9,
                                'Hotel room': x10,
                                'Private room': x11,
                                'Shared room': x12}, index=[0])
# Realizar predicciones con el modelo cargado
predicciones = predecir(datos_entrada)
# Mostrar el resultado de las predicciones
mostrar_resultados(predicciones)

