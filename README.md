# CDC Streamlit App

Esta aplicación permite realizar una regresión lineal sobre datos subidos en formato CSV usando Streamlit y scikit-learn.

## Uso

1. Ejecuta la app con:
   ```powershell
   streamlit run cdcstream.py
   ```
2. Sube un archivo CSV que contenga las columnas:
   - `Tecnicos_asignados`
   - `Tiempo_resolucion_horas`
3. Ingresa el número de técnicos asignados y presiona "Predecir el tiempo de resolución" para obtener la estimación.

## Requisitos
- Python 3.12+
- streamlit
- pandas
- scikit-learn
- matplotlib

Instala los paquetes necesarios con:
```powershell
pip install streamlit pandas scikit-learn matplotlib
```

## Visualización y métricas
La app muestra un gráfico de dispersión con la línea de regresión y las métricas del modelo (R², MAE, MSE) después de cada predicción.

## Estructura del CSV
El archivo debe tener al menos dos columnas numéricas. Puedes seleccionar cualquier par de columnas para realizar la predicción.
Ejemplo:
```csv
X,Y
3,5.2
2,7.1
...
```

## Autor
Creado por aks-alx
