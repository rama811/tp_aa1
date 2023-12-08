import streamlit as st
import numpy as np
import joblib

st.title('Predicciones con Modelo de Clasificación')

# Cargar el modelo previamente entrenado
ruta = '/home/rama811/Descargas/modelo_clas.joblib'
modelo_entrenado = joblib.load(ruta)

# Obtener la lista de variables
variables_num = ['MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine',
       'WindGustSpeed', 'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am',
       'Humidity3pm', 'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm',
       'Temp9am', 'Temp3pm']

variables_cat = ['RainToday', 'WindGustDir_E', 'WindGustDir_ENE',
       'WindGustDir_ESE', 'WindGustDir_N', 'WindGustDir_NE', 'WindGustDir_NNE',
       'WindGustDir_NNW', 'WindGustDir_NW', 'WindGustDir_S', 'WindGustDir_SE',
       'WindGustDir_SSE', 'WindGustDir_SSW', 'WindGustDir_SW', 'WindGustDir_W',
       'WindGustDir_WNW', 'WindGustDir_WSW', 'WindDir9am_E', 'WindDir9am_ENE',
       'WindDir9am_ESE', 'WindDir9am_N', 'WindDir9am_NE', 'WindDir9am_NNE',
       'WindDir9am_NNW', 'WindDir9am_NW', 'WindDir9am_S', 'WindDir9am_SE',
       'WindDir9am_SSE', 'WindDir9am_SSW', 'WindDir9am_SW', 'WindDir9am_W',
       'WindDir9am_WNW', 'WindDir9am_WSW', 'WindDir3pm_E', 'WindDir3pm_ENE',
       'WindDir3pm_ESE', 'WindDir3pm_N', 'WindDir3pm_NE', 'WindDir3pm_NNE',
       'WindDir3pm_NNW', 'WindDir3pm_NW', 'WindDir3pm_S', 'WindDir3pm_SE',
       'WindDir3pm_SSE', 'WindDir3pm_SSW', 'WindDir3pm_SW', 'WindDir3pm_W',
       'WindDir3pm_WNW', 'WindDir3pm_WSW', 'Mes_1', 'Mes_2', 'Mes_3', 'Mes_4',
       'Mes_5', 'Mes_6', 'Mes_7', 'Mes_8', 'Mes_9', 'Mes_10', 'Mes_11',
       'Mes_12']

# Sidebar variables categóricas
st.sidebar.header('Variables categóricas:')
valores_input = []
for variable in variables_cat:
    # Utilizar checkbox para variables binarias
    valor = st.sidebar.checkbox(f'{variable}')
    valores_input.append(valor)

# Sidebar variables numéricas
st.sidebar.header('Variables numéricas:')
for variable in variables_num:
    valor = st.sidebar.number_input(f'{variable}', min_value=-10.0, max_value=1100.0)
    valores_input.append(valor)

# Crear un array numpy con los valores de entrada
datos_para_predecir = np.array([valores_input])

# Realizar la predicción con el modelo
prediccion = modelo_entrenado.predict(datos_para_predecir)

# Mostrar la predicción en la interfaz de Streamlit
umbral = 0.5

if prediccion[0] < umbral:
    st.write('Predicción: No lloverá')
else:
    st.write('Predicción: Lloverá')

