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

Instala los paquetes necesarios con:
```powershell
pip install streamlit pandas scikit-learn
```

## Estructura del CSV
El archivo debe tener al menos estas dos columnas:
```csv
Tecnicos_asignados,Tiempo_resolucion_horas
3,5.2
2,7.1
...
```

## Autor
Creado por aks-alx
