# --------------------------------------------------------------
# spam_classifier.py — Clasificador de SPAM usando embeddings OpenAI
# --------------------------------------------------------------

import os                    # Manejo de variables de entorno y operaciones del sistema
import numpy as np           # Manipulación de arreglos numéricos
import pandas as pd          # Lectura y manipulación de datos tabulares (CSV)

from dotenv import load_dotenv                   # Librería para cargar variables desde archivo .env
from sklearn.model_selection import train_test_split  # Librería para hacer división de datos en entrenamiento y prueba
from sklearn.linear_model import LogisticRegression   # Libreria para uso de Modelo (ML) de clasificación
from sklearn.metrics import classification_report, confusion_matrix  # Librería para generar Métricas de evaluación
from openai import OpenAI                         # Librería para hacer llamados de Modelos desde OpenAI para API

# 1. Cargamos las variables de entorno desde archivo .env 
# Aquí se espera que esté la API Key para poder interactuar con OpenAI y usar sus modelos
load_dotenv()

# 2. Leemos la API Key desde las variables de entorno cargadas con load_dotenv
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Nos aseguramos que la API key exista para evitar errores posteriores
if OPENAI_API_KEY is None:
    raise ValueError(
        "No se encontró la variable de entorno OPENAI_API_KEY. "
        "Crea un archivo .env o exporta la variable en tu sistema."
    )

# Inicializamos cliente OpenAI usando la API Key
client = OpenAI(api_key=OPENAI_API_KEY)

# Definimos el nombre del modelo de embeddings que usaremos
EMBEDDING_MODEL = "text-embedding-3-small"

# Definición del Mapa de etiquetas para mostrar el resultado en formato amigable
LABEL_MAP = {"spam": "Spam ❌", "ham": "Not spam ✅"}


# --------------------------------------------------------------
# Definición de la función para generar embeddings
# --------------------------------------------------------------
def get_embeddings(texts, batch_size: int = 100) -> np.ndarray:
    """
    Esta funcion genera los embeddings para una lista (o Serie) de textos.
    """

    # Si es una Serie de pandas, convertir a lista
    if isinstance(texts, pd.Series):
        texts = texts.tolist()

    all_embeddings = []  # Inicialización de la Lista que guardará de todos los embeddings

    # Vamos a procesar los textos en lotes para optimizar llamadas a la API
    for i in range(0, len(texts), batch_size):
        batch_texts = texts[i:i + batch_size]  # Seleccionamos lote por lote definido

        # Llamamos a la API que usa el Modelo seleccionado para generar embeddings
        response = client.embeddings.create(
            model=EMBEDDING_MODEL,
            input=batch_texts,
        )

        # Extraemos los embeddings del resultado despues de ser procesados por la API
        batch_embeddings = [item.embedding for item in response.data]

        # Añadimos los embeddings generados  a la lista definida
        all_embeddings.extend(batch_embeddings)

    # Convertimos la Lista a un arreglo NumPy y es el retorno de la función
    # Necesitamos que sea un arreglo NumPy para que sklearn pueda trabajar con ellos
    return np.array(all_embeddings)


# --------------------------------------------------------------
# Función para cargar dataset para entrenamiento y pruebas del clasificador de Spam
# --------------------------------------------------------------
def load_dataset(csv_path: str = "spam.csv") -> pd.DataFrame:
    """
    Carga el dataset spam.csv y estandariza nombres de columnas.
    """
    df = pd.read_csv(csv_path, encoding="latin1")  # Cargar CSV

    # Renombramos las columnas para estandarizar
    df = df.rename(columns={"v1": "label", "v2": "text"})

    # Seleccionamos las columnas necesarias
    df = df[["label", "text"]]

    # Retornamos el DataFrame limpio y estandarizado
    return df


# --------------------------------------------------------------
# Definición de la función para entrenar el Modelo clasificador de Spam
# --------------------------------------------------------------
def train_classifier(
    csv_path: str = "spam.csv",
    test_size: float = 0.2,
    random_state: int = 42,
):
    """
    Entrena un modelo LogisticRegression usando embeddings OpenAI.
    """

    print("Cargando dataset...")
    # Cargamos el dataset que hemos seleccionado para entrenamiento y prueba del clasificador
    df = load_dataset(csv_path)  

    # Dividimos los datos en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(
        df["text"],
        df["label"],
        test_size=test_size,
        stratify=df["label"],   # Garantizamos que la proporción de clases se mantenga (spam y no spam)
        random_state=random_state,
    )

    # Generamos los embeddings para entrenamiento usando la función definida get_embeddings
    print("Generando embeddings para entrenamiento...")
    X_train_emb = get_embeddings(X_train.reset_index(drop=True))

    # Generamos los  embeddings para prueba usando la función definida get_embeddings
    print("Generando embeddings para prueba...")
    X_test_emb = get_embeddings(X_test.reset_index(drop=True))

    print(f"Forma de X_train_emb: {X_train_emb.shape}")

    # Creamos y entrenamos modelo LogisticRegression
    print("Entrenando el modelo de Clasificación de Spam...")
    clf = LogisticRegression(max_iter=1000)
    clf.fit(X_train_emb, y_train)

    # Evaluación del modelo con el conjunto de datos de prueba
    print("Evaluando el Modelo de Clasificación de spam con los datos de prueba...")
    y_pred = clf.predict(X_test_emb)

    print(classification_report(y_test, y_pred))  # Reporte de métricas
    print(confusion_matrix(y_test, y_pred))       # Matriz de confusión

    # Retornamos el Modelo clasificador de spam entrenado
    return clf  


# --------------------------------------------------------------
# Definición de la función para clasificar un solo asunto (subject) de email
# --------------------------------------------------------------
def classify_email(clf: LogisticRegression, text: str) -> str:
    """
    Clasifica un texto como spam o no spam y devuelve etiqueta amigable.
    """

    # Generamos el embedding del texto dado, que es el asunto (subject) del email
    emb = get_embeddings(pd.Series([text]))

    # Hacemos la predicción usando el modelo Clasificador de spam entrenado
    pred_label = clf.predict(emb)[0]

    # Devolvemos la etiqueta en formato amigable (emoji)
    return LABEL_MAP.get(pred_label, pred_label)