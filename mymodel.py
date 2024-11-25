import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import plotly.express as px

# Generamos datos sintéticos para el ejemplo
def generate_house_data(n_samples=100):
    np.random.seed(42)
    size = np.random.normal(1500, 500, n_samples)
    price = size * 100 + np.random.normal(0, 10000, n_samples)
    return pd.DataFrame({'size_sqft': size, 'price': price})

# Crear y entrenar el modelo
def train_model():
    # Generar datos
    df = generate_house_data()
    
    # Dividir en entrenamiento y prueba
    X = df[['size_sqft']]
    y = df['price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Entrenar modelo
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    return model

# Interfaz Streamlit
def main():
    st.title('🏠 Predictor de Precios de Viviendas')
    st.write('Ingrese el tamaño de la vivienda para predecir su precio')
    
    # Entrenar modelo
    model = train_model()
    
    # Input del usuario
    size = st.number_input('Tamaño de la vivienda (pies cuadrados)', 
                          min_value=500, 
                          max_value=5000, 
                          value=1500)
    
    if st.button('Predecir Precio'):
        # Hacer predicción
        prediction = model.predict([[size]])
        
        # Mostrar resultado
        st.success(f'Precio estimado: ${prediction[0]:,.2f}')
        
        # Visualización
        df = generate_house_data()
        fig = px.scatter(df, x='size_sqft', y='price', 
                        title='Relación Tamaño vs Precio')
        fig.add_scatter(x=[size], y=[prediction[0]], 
                       mode='markers', 
                       marker=dict(size=15, color='red'),
                       name='Predicción')
        st.plotly_chart(fig)

if __name__ == '__main__':
    main()
