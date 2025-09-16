
import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt

st.title("Regresion Lineal")
archivo = st.file_uploader("Sube un archivo CSV")

@st.cache_data
def cargar_datos(archivo):
    return pd.read_csv(archivo)

@st.cache_data
def entrenar_modelo(x, y):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    modelo = LinearRegression()
    modelo.fit(x_train, y_train)
    return modelo

if archivo is not None:
    df = cargar_datos(archivo)
    st.write("Vista previa de los datos:")
    st.dataframe(df.head())
    columnas_numericas = df.select_dtypes(include=['number']).columns.tolist()
    if len(columnas_numericas) < 2:
        st.error("El archivo debe tener al menos dos columnas numéricas.")
    else:
        col_x = st.selectbox("Selecciona la columna independiente (X)", columnas_numericas)
        col_y = st.selectbox("Selecciona la columna dependiente (Y)", [c for c in columnas_numericas if c != col_x])
        x = df[[col_x]]
        y = df[[col_y]]
        modelo = entrenar_modelo(x, y)
        nuevo_x = st.number_input(f"Valor para {col_x}", min_value=float(df[col_x].min()), max_value=float(df[col_x].max()), step=1.0)
        if st.button("Predecir"): 
            prediccion = modelo.predict([[nuevo_x]])
            st.write(f"Predicción para {col_y}: {prediccion[0][0]:.2f}")

            # Visualización: scatter plot y línea de regresión
            fig, ax = plt.subplots()
            ax.scatter(x, y, color='blue', label='Datos reales')
            ax.plot(x, modelo.predict(x), color='red', label='Regresión lineal')
            ax.set_xlabel(col_x)
            ax.set_ylabel(col_y)
            ax.legend()
            st.pyplot(fig)

            # Métricas del modelo
            y_pred = modelo.predict(x)
            r2 = r2_score(y, y_pred)
            mae = mean_absolute_error(y, y_pred)
            mse = mean_squared_error(y, y_pred)
            st.subheader("Métricas del modelo")
            st.write(f"R²: {r2:.3f}")
            st.write(f"MAE: {mae:.3f}")
            st.write(f"MSE: {mse:.3f}")
# --- IGNORE ---
