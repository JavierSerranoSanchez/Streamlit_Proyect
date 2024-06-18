import streamlit as st
import pickle
import numpy as np

# Cargar el modelo
with open('modelo.pkl', 'rb') as f:
    modelo = pickle.load(f)

# Título de la aplicación
st.title('Predicción de Cargos Médicos')

# Crear entradas para las variables predictoras
age = st.number_input('Edad', min_value=0, max_value=120, value=25)
bmi = st.number_input('Índice de Masa Corporal (BMI)', min_value=0.0, max_value=50.0, value=22.0, format="%.1f")
children = st.number_input('Número de Hijos', min_value=0, max_value=10, value=0)
smoker = st.selectbox('¿Es fumador?', ('No', 'Sí'))

# Convertir la entrada de fumador a 0 o 1
smoker = 1 if smoker == 'Sí' else 0

# Realizar la predicción cuando el usuario hace clic en el botón
if st.button('Predecir'):
    input_data = np.array([[age, bmi, children, smoker]])
    prediccion = modelo.predict(input_data)
    st.write(f'El cargo médico estimado es: ${prediccion[0]:.2f}')

