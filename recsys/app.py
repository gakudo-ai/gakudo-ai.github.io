import streamlit as st
import pandas as pd
from surprise import SVD, Dataset, accuracy
from surprise.model_selection import train_test_split

# Configuración de la página
st.set_page_config(page_title="Recomendador de Películas", page_icon="🎬")

st.title("🎬 Motor de Recomendación de Películas")
st.write("Prueba de Concepto (PoC) utilizando Factorización de Matrices (SVD).")

# 1. Cargar el mapeo de películas (con caché para no descargarlo siempre)
@st.cache_data
def load_movie_titles():
    # Descargamos el u.item directamente de la fuente original para evitar problemas de rutas locales
    url = "https://files.grouplens.org/datasets/movielens/ml-100k/u.item"
    movies_df = pd.read_csv(
        url, sep='|', header=None, encoding='latin-1', usecols=[0, 1],
        names=['movie_id', 'title']
    )
    return movies_df.set_index('movie_id')['title'].to_dict()

# 2. Entrenar el modelo (con caché para que solo se entrene una vez al iniciar la app)
@st.cache_resource
def train_model():
    data = Dataset.load_builtin('ml-100k')
    trainset, testset = train_test_split(data, test_size=0.25)
    
    model = SVD(n_factors=20, n_epochs=20, lr_all=0.005, reg_all=0.02)
    model.fit(trainset)
    
    # Evaluar el modelo
    predictions = model.test(testset)
    rmse = accuracy.rmse(predictions, verbose=False)
    
    # Extraer todas las valoraciones para filtrar luego
    all_ratings = pd.DataFrame(data.raw_ratings, columns=['user_id', 'movie_id', 'rating', 'timestamp'])
    
    return model, all_ratings, rmse

# Mostrar un mensaje de carga mientras se entrena el modelo en segundo plano
with st.spinner('Cargando datos y entrenando el modelo... Esto tomará unos segundos la primera vez.'):
    movie_id_to_title = load_movie_titles()
    model, all_ratings, rmse = train_model()

# Mostrar la precisión del modelo entrenado
st.sidebar.markdown("### 📊 Métricas del Modelo")
st.sidebar.info(f"**RMSE (Error Cuadrático Medio):** {rmse:.4f}")
st.sidebar.write("*(Un RMSE más bajo indica mejores predicciones)*")

# 3. Interfaz de Usuario para generar recomendaciones
st.markdown("### 👤 Obtener Recomendaciones Personalizadas")

col1, col2 = st.columns(2)
with col1:
    # En el dataset ml-100k los IDs de usuario van del 1 al 943
    user_id_input = st.number_input("Selecciona un ID de Usuario (1 - 943):", min_value=1, max_value=943, value=196)
with col2:
    num_recs = st.slider("Número de recomendaciones:", min_value=1, max_value=20, value=5)

if st.button("Generar Recomendaciones", type="primary"):
    user_id_str = str(user_id_input)
    
    # Identificar películas que el usuario ya ha visto
    rated_movies = all_ratings[all_ratings['user_id'] == user_id_str]['movie_id'].tolist()
    all_movie_ids = list(movie_id_to_title.keys())
    
    # Filtrar películas no vistas
    unrated_movie_ids = [m_id for m_id in all_movie_ids if str(m_id) not in rated_movies]
    
    # Predecir rating para las no vistas
    predictions_list = []
    for movie_id in unrated_movie_ids:
        pred = model.predict(user_id_str, str(movie_id))
        predictions_list.append({
            'Película': movie_id_to_title.get(movie_id, f"Película Desconocida ({movie_id})"),
            'Rating Predicho': round(pred.est, 2)
        })
        
    # Crear DataFrame, ordenar y mostrar
    predictions_df = pd.DataFrame(predictions_list)
    top_recommendations = predictions_df.sort_values(by='Rating Predicho', ascending=False).head(num_recs)
    
    st.success(f"Aquí tienes el Top {num_recs} para el Usuario {user_id_input}:")
    
    # Mostrar como una tabla interactiva y limpia
    st.dataframe(
        top_recommendations.reset_index(drop=True),
        use_container_width=True,
        column_config={
            "Rating Predicho": st.column_config.ProgressColumn(
                "Rating Predicho (Estrellas)",
                help="Predicción del modelo de 1 a 5",
                format="%.2f",
                min_value=0,
                max_value=5,
            ),
        }
    )
