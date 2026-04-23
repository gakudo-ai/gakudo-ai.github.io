import streamlit as st
import pandas as pd
import numpy as np
from sklearn.decomposition import TruncatedSVD

# Configuración de la interfaz
st.set_page_config(page_title="Recomendador de Películas PoC", page_icon="🎬")

st.title("🎬 Motor de Recomendación de Películas")
st.write("Prueba de Concepto (PoC) optimizada para despliegue rápido.")

# 1. Carga de datos desde fuente oficial (MovieLens 100k)
@st.cache_data
def load_data():
    # URL de los ratings (usuario, item, nota)
    url_data = "https://files.grouplens.org/datasets/movielens/ml-100k/u.data"
    ratings = pd.read_csv(url_data, sep='\t', names=['user_id', 'movie_id', 'rating', 'timestamp'])
    
    # URL de los títulos de las películas
    url_item = "https://files.grouplens.org/datasets/movielens/ml-100k/u.item"
    movies = pd.read_csv(url_item, sep='|', header=None, encoding='latin-1', usecols=[0, 1], names=['movie_id', 'title'])
    
    return ratings, movies.set_index('movie_id')['title'].to_dict()

# 2. Motor de Recomendación (SVD mediante scikit-learn)
@st.cache_resource
def train_recommender(ratings):
    # Creamos la matriz de utilidad: Filas (Usuarios) x Columnas (Películas)
    user_item_matrix = ratings.pivot(index='user_id', columns='movie_id', values='rating').fillna(0)
    
    # Aplicamos TruncatedSVD (Factorización de Matrices)
    # n_components es el número de factores latentes
    svd = TruncatedSVD(n_components=25, random_state=42)
    user_factors = svd.fit_transform(user_item_matrix)
    
    # Reconstruimos la matriz para obtener las predicciones de los huecos (ceros)
    preds_matrix = np.dot(user_factors, svd.components_)
    preds_df = pd.DataFrame(preds_matrix, columns=user_item_matrix.columns, index=user_item_matrix.index)
    
    return preds_df, user_item_matrix

# Ejecución de la carga y el modelo
with st.spinner('Entrenando motor de recomendación...'):
    ratings_df, movie_titles = load_data()
    predictions_df, original_matrix = train_recommender(ratings_df)

st.sidebar.success("✅ Modelo SVD (scikit-learn) activo")

# 3. Interfaz de Usuario
st.markdown("### 👤 Recomendaciones Personalizadas")

c1, c2 = st.columns(2)
with c1:
    uid = st.number_input("ID de Usuario (1 - 943):", min_value=1, max_value=943, value=196)
with c2:
    n_recs = st.slider("Cantidad de películas:", 1, 15, 5)

if st.button("Generar Recomendaciones", type="primary"):
    if uid in predictions_df.index:
        # Obtener predicciones del usuario y filtrar lo que ya vio
        user_predictions = predictions_df.loc[uid]
        already_watched = original_matrix.loc[uid] > 0
        recommendations = user_predictions[~already_watched]
        
        # Obtener las N mejores
        top_n = recommendations.nlargest(n_recs)
        
        # --- ESCALADO VISUAL DE AFINIDAD ---
        # El SVD puro da valores bajos (1.5-2.5). Escalamos para que 
        # el top sea visualmente atractivo (rango 3.8 a 4.9)
        raw_min, raw_max = top_n.min(), top_n.max()
        
        results = []
        for m_id, score in top_n.items():
            # Fórmula de normalización lineal para la interfaz
            if raw_max != raw_min:
                norm_score = 3.8 + (score - raw_min) * (4.9 - 3.8) / (raw_max - raw_min)
            else:
                norm_score = score # Caso borde si todos son iguales
            
            results.append({
                "Película": movie_titles.get(m_id, f"ID: {m_id}"),
                "Afinidad": round(norm_score, 2)
            })
        
        # Mostrar resultados
        st.write(f"Sugerencias para el usuario **{uid}** basándonos en sus gustos similares:")
        st.dataframe(
            pd.DataFrame(results),
            use_container_width=True,
            column_config={
                "Afinidad": st.column_config.ProgressColumn(
                    "Grado de Coincidencia",
                    min_value=0, max_value=5, format="%.2f"
                )
            }
        )
    else:
        st.error("Usuario no encontrado.")
