# Importamos la librería Streamlit para construir la interfaz web.
import streamlit as st

# Importamos las funciones para entrenar el modelo y clasificar textos
# que hemos definido en spam_classifier.py
from spam_classifier import train_classifier, classify_email


# --------------------------------------------------------------
# 1. Configuración básica de la página Web con Streamlit
# --------------------------------------------------------------

# Configura el título y el ícono que aparecerán en la pestaña del navegador.
st.set_page_config(
    page_title="Clasificador de Spam (Asunto de correo)",
    page_icon="📧",
)

# Muestra el título principal en la parte superior de la aplicación.
st.title("📧 Clasificador de Spam (Asunto de correo)")

# Muestra un texto descriptivo explicando cómo funciona la app.
st.write(
    """
    Escribe el **asunto (subject)** de un correo electrónico y el modelo 
    te dirá si parece **Spam** o **No Spam**.

    Debajo usamos:
    - Embeddings de OpenAI (`text-embedding-3-small`)
    - Un clasificador `LogisticRegression` entrenado con el dataset clásico de spam.
    """
)


# --------------------------------------------------------------
# 2. Entrenamos el modelo UNA sola vez usando caché
# --------------------------------------------------------------

# Instructivo que hace que Streamlit almacene en caché el modelo entrenado
# para evitar que se entrene nuevamente cada vez que se recarga la página.
@st.cache_resource
def get_trained_model():
    # Llama a la función que entrena el modelo usando el archivo spam.csv.
    clf = train_classifier(csv_path="spam.csv")
    return clf  # Nos devuelve el modelo Clasificador de Spam entrenado.


# Mostramos un indicador visual mientras el modelo se entrena o carga desde caché.
with st.spinner("Cargando y entrenando el modelo de spam..."):
    clf = get_trained_model()  # Obtiene el modelo, ya sea entrenado o desde caché.

# Mostramos un mensaje indicando que el modelo está listo para usarse.
st.success("✅ Modelo cargado correctamente. Ya puedes probar asuntos de correos.")


# --------------------------------------------------------------
# 3. Inicializamos el historial de mensajes para el chat
# --------------------------------------------------------------

# Verifica si existe una variable 'messages' en la sesión de Streamlit.
if "messages" not in st.session_state:
    # Si no existe, inicializa la lista que guardará el historial del chat.
    st.session_state.messages = []  # Cada mensaje tendrá: {"role": "user"/"assistant", "content": str}


# --------------------------------------------------------------
# 4. Mostramos el historial del chat
# --------------------------------------------------------------

# Recorre todos los mensajes almacenados anteriormente.
for msg in st.session_state.messages:
    # Crea un bloque visual con formato de chat según el rol (user o assistant).
    with st.chat_message(msg["role"]):
        # Muestra el contenido del mensaje.
        st.markdown(msg["content"])


# --------------------------------------------------------------
# 5. Entrada tipo chat del usuario
# --------------------------------------------------------------

# Creamos un campo donde el usuario puede escribir el asunto del correo.
subject = st.chat_input("Escribe aquí el asunto del correo...")

# Si el usuario escribió algo, se procesa.
if subject:
    # Guarda el mensaje del usuario en el historial de la sesión.
    st.session_state.messages.append({"role": "user", "content": subject})

    # Muestra el mensaje del usuario dentro del chat visual.
    with st.chat_message("user"):
        st.markdown(subject)

    # --------------------------------------------------------------
    # Clasificación del texto ingresado por el usuario
    # --------------------------------------------------------------

    # Crea un bloque visual para la respuesta del modelo.
    with st.chat_message("assistant"):
        # Muestra un indicador mientras se ejecuta el análisis.
        with st.spinner("Analizando si es spam o no..."):
            # Llama a la función que clasifica el texto como spam o no spam.
            result = classify_email(clf, subject)

        # --------------------------------------------------------------
        # Construimos la  respuesta generada por el Modelo Clasificador de Spam amigable con emojis
        # --------------------------------------------------------------

        # Si el resultado contiene la palabra "Spam", se marca como spam.
        if "Spam" in result:
            answer = (
                f"🔴 **Resultado:** {result}\n\n"
                "Este asunto parece corresponder a un correo de **SPAM**."
            )
        else:
            # Si no contiene "Spam", se considera un correo legítimo.
            answer = (
                f"🟢 **Resultado:** {result}\n\n"
                "Este asunto parece un correo **legítimo (no spam)**."
            )

        # Mostramos la respuesta en el chat.
        st.markdown(answer)

        # Guardamos la respuesta en el historial de mensajes.
        st.session_state.messages.append({"role": "assistant", "content": answer})