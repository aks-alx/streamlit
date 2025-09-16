
import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

st.title("Regresion Lineal")
archivo = st.file_uploader("Busca el archivo a subir")
@st.cache_data
def cargar_datos(archivo):
    return pd.read_csv(archivo)

@st.cache_data
def entrenar_modelo(df):
    x = df[["Tecnicos_asignados"]]
    y = df[["Tiempo_resolucion_horas"]]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    modelo = LinearRegression()
    modelo.fit(x_train, y_train)
    return modelo

if archivo is not None:
    df = cargar_datos(archivo)
    if "Tecnicos_asignados" in df.columns and "Tiempo_resolucion_horas" in df.columns:
        modelo = entrenar_modelo(df)
        nuevos_ta = st.number_input("Tecnicos asignados", min_value=0, step=1)
        if st.button("Predecir el tiempo de resolución"):
            prediccion = modelo.predict([[nuevos_ta]])
            st.write(f"Tiempo de resolución estimado: {prediccion[0][0]:.2f} horas")
    else:
        st.error("El archivo debe contener las columnas 'Tecnicos_asignados' y 'Tiempo_resolucion_horas'.")
# --- IGNORE ---
