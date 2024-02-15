import streamlit as st
import numpy as np
import joblib
import pandas as pd

# Cargar los modelos previamente entrenados
modelo_clas = joblib.load('modelo_clas.joblib')
modelo_reg = joblib.load('modelo_reg.joblib')
# Definir variables
numeric_features = ['MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine', 'WindGustSpeed', 'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm', 'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm', 'Temp9am', 'Temp3pm']
categorical_features = ['WindGustDir', 'WindDir9am', 'WindDir3pm', 'RainToday', 'Mes']
# Definir opciones para variables categóricas
cardinals_points = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW' ]
categorical_options = {'RainToday': ['Yes', 'No' ] , 'WindGustDir': cardinals_points, 'WindDir9am': cardinals_points, 'WindDir3pm': cardinals_points,
                       'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']}
# Definir rangos para variables numéricas
numeric_ranges = {
    'MinTemp': (-10.0, 50.0),
    'MaxTemp': (0.0, 50.0),
    'Rainfall': (0.0, 200.0),
    'Evaporation': (0.0, 25.0),
    'Sunshine': (0.0, 15.0),
    'WindGustSpeed': (0.0, 150.0),
    'WindSpeed9am': (0.0, 150.0),
    'WindSpeed3pm': (0.0, 150.0),
    'Humidity9am': (0.0, 100.0),
    'Humidity3pm': (0.0, 100.0),
    'Pressure9am': (900.0, 1100.0),
    'Pressure3pm': (900.0, 1100.0),
    'Cloud9am': (0.0, 9.0),
    'Cloud3pm': (0.0, 9.0),
    'Temp9am': (-10.0, 50.0),
    'Temp3pm': (-10.0, 50.0)
}


# Función para predecir
def predict_rain(data, modelo):
    prediction = modelo.predict(data)
    return prediction

# Interfaz de usuario de Streamlit
def main():
    # Crear campos de entrada para que el usuario ingrese los datos
    st.sidebar.header('Ingrese los datos para la predicción')
    new_data = {}
    # Variables numéricas
    for feature in numeric_features:
        min_val, max_val = numeric_ranges[feature]
        new_data[feature] = st.sidebar.number_input(f'Ingrese {feature}', min_value=min_val, max_value=max_val)
    # Variables categóricas
    for feature in categorical_features:
        options = st.sidebar.selectbox(f'Seleccione {feature}', categorical_options[feature])
        new_data[feature] = options
    # Convertir los datos ingresados a un DataFrame
    data = pd.DataFrame([new_data])
    # Interfaz de usuario para predecir
    if st.sidebar.button('Predecir'):
        prediction_clas = predict_rain(data, modelo_clas)
        prediction_reg = predict_rain(data, modelo_reg)
        # Establecer título
        st.title('Predicción de lluvia:')
        if prediction_clas[0] == 'Yes':
            st.write(f"Lloverán {format(prediction_reg[0], '.2f')} milímetros")
        else:
            st.write("No lloverá")
        

if __name__ == "__main__":
    main()
