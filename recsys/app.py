import streamlit as st
import pandas as pd
import numpy as np
from sklearn.decomposition import TruncatedSVD

# Configuración de la página
st.set_page_config(page_title="Recomendador de Películas", page_icon="🎬")

st.title("🎬 Motor de Recomendación de Películas")
st.write("Prueba de Concepto (PoC) 100% nativa usando scikit-learn (TruncatedSVD).")

# 1. Cargar datos directamente desde la web
@st.cache_data
def load_data():
    # Descargar ratings
    url_data = "https://files.grouplens.org/datasets/movielens/ml-100k/u.data"
    ratings = pd.read_csv(url_data, sep='\t', names=['user_id', 'movie_id', 'rating', 'timestamp'])
    
    # Descargar títulos
    url_item = "https://files.grouplens.org/datasets/movielens/ml-100k/u.item"
    movies = pd.read_csv(url_item, sep='|', header=None, encoding='latin-1', usecols=[0, 1], names=['movie_id', 'title'])
    
    return ratings, movies.set_index('movie_id')['title'].to_dict()

# 2. Entrenar el modelo (Matriz + SVD)
@st.cache_resource
def train_model(ratings):
    # Crear matriz de utilidad (filas: usuarios, columnas: películas)
    user_item_matrix = ratings.pivot(index='user_id', columns='movie_id', values='rating').fillna(0)
    
    # Aplicar SVD (Factorización de Matrices)
    svd = TruncatedSVD(n_components=20, random_state=42)
    matrix_svd = svd.fit_transform(user_item_matrix)
    
    # Reconstruir la matriz con las predicciones completas
    predicted_matrix = np.dot(matrix_svd, svd.components_)
    predicted_df = pd.DataFrame(predicted_matrix, columns=user_item_matrix.columns, index=user_item_matrix.index)
    
    return predicted_df, user_item_matrix

# Carga y entrenamiento en segundo plano
with st.spinner('Cargando datos y entrenando el modelo...'):
    ratings_df, movie_id_to_title = load_data()
    predicted_ratings_df, original_matrix = train_model(ratings_df)

st.sidebar.success("✅ Modelo SVD entrenado y listo")

# 3. Interfaz de Usuario
st.markdown("### 👤 Obtener Recomendaciones Personalizadas")

col1, col2 = st.columns(2)
with col1:
    user_id_input = st.number_input("Selecciona un ID de Usuario (1 - 943):", min_value=1, max_value=943, value=196)
with col2:
    num_recs = st.slider("Número de recomendaciones:", min_value=1, max_value=20, value=5)

if st.button("Generar Recomendaciones", type="primary"):
    if user_id_input in predicted_ratings_df.index:
        # 1. Obtener todas las predicciones para el usuario
        user_preds = predicted_ratings_df.loc[user_id_input]
        
        # 2. Filtrar las películas que el usuario YA ha visto
        already_watched = original_matrix.loc[user_id_input] > 0
        user_preds = user_preds[~already_watched]
        
        # 3. Obtener el Top N
        top_movies_ids = user_preds.nlargest(num_recs).index
        top_scores = user_preds.nlargest(num_recs).values
        
        # 4. Formatear para mostrar
        results = []
        for m_id, score in zip(top_movies_ids, top_scores):
            # Normalizar la puntuación visualmente (SVD a veces devuelve valores fuera de rango)
            display_score = min(max(score, 0), 5)
            results.append({
                'Película': movie_id_to_title.get(m_id, f"Desconocida ({m_id})"),
                'Afinidad Estimada': round(display_score, 2)
            })
            
        st.success(f"Top {num_recs} para el Usuario {user_id_input}:")
        st.dataframe(
            pd.DataFrame(results),
            use_container_width=True,
            column_config={
                "Afinidad Estimada": st.column_config.ProgressColumn(
                    "Score de Afinidad",
                    help="Estimación de afinidad (0 a 5)",
                    format="%.2f",
                    min_value=0,
                    max_value=5,
                ),
            }
        )
    else:
        st.error("ID de usuario no encontrado en la base de datos.")
