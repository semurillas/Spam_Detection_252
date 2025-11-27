<h1> <img width="207" height="112" alt="image" src="https://github.com/user-attachments/assets/89fd906b-04fb-4d4f-b5e6-8375083a8a01" /></h1>
<h1>📚 Maestría en Inteligencia Artificial Aplicada – 3er Semestre</h1>

<h3>Asignatura: Hackeando la Inteligencia Artificial</h3>

<h3>Taller Detección de Spam</h3>

<hr style="width:60%;">

<h3>👨‍🎓 Estudiantes</h3>
<ul style="list-style:none; padding:0; font-size:18px;">
    <li>Claudia Martinez</li>
    <li>Enrique Manzano</li> 
    <li>Sebastián Murillas</li>
    <li>Octavio Guerra</li>
</ul>

<hr style="width:60%;">

<h3>📅 Fecha: Noviembre 27, 2025</h3>


# 📧 Clasificador de Spam usando LLM Embeddings + Logistic Regression

En este Taller práctico que hace parte del proceso de aprendizaje de la asignatura **Hackeando la Inteligencia Artificial** hemos desarrollado e implementado un **clasificador de spam** para el *subject* (asunto) de algún correo electrónico, usando un modelo de Lenguaje Grande (LLM) combinado con técnicas tradicionales de Machine Learning. Este último para realizar el proceso de Clasificación binaria, que determina si el asunto (subject) es Spam o no lo es.

---

## 🧠 Descripción del proyecto

El objetivo principal es entrenar un sistema que detecte si el asunto (subject) de un correo es:

- **Spam ❌**  
- **No Spam ✅**

Para esto se utiliza un enfoque híbrido:

1. **Embeddings generados por un Modelo de Lenguaje (LLM)**  
   Modelo usado: `text-embedding-3-small` de OpenAI.
2. **Clasificador tradicional (Logistic Regression)**  
   Basado en los vectores generados por el LLM.

El resultado es un clasificador eficiente, interpretable y fácil de usar, con una interfaz interactiva construida en **Streamlit** que permite interactuar mediante un chat.

---

## 📂 Estructura del repositorio

```
.
├── spam.csv                    # Dataset clásico de spam/ham
├── spam_classifier.py          # Entrenamiento, embeddings y función de clasificación
├── app_spam_mail_interface.py  # Aplicación Streamlit con interfaz tipo chat
├── requirements.txt            # Dependencias del proyecto
├── .env                        # (Opcional) Clave de API de OpenAI
└── README.md                   # Documentación del proyecto
```

---

## 🔧 Instalación y ejecución

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
```

---

### 2️⃣ Crear entorno virtual

Aquí usamos el nombre `venvspam`, pero puede ser cualquiera:

```bash
python -m venv venvspam
```

Activación:

#### Windows (PowerShell)
```bash
venvspam\Scripts\Activate.ps1
```

#### Linux / macOS
```bash
source venvspam/bin/activate
```

---

### 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configurar clave de OpenAI

Crear archivo `.env` en la raíz del proyecto:

```
OPENAI_API_KEY=tu_clave_aqui
```

> ❗ No subir este archivo a GitHub.

---

### 5️⃣ Ejecutar la aplicación Streamlit

```bash
streamlit run app_spam_mail_interface.py
```

Abrir en el navegador:

```
http://localhost:8501
```

---

## 💻 Uso de la aplicación

1. La app entrenará el modelo la primera vez.  
2. Aparecerá una interfaz tipo **chat**.  
3. Se ingresa el asunto (*subject*) de un correo.  
4. El modelo devolverá una predicción:

- **🔴 Spam (❌)**
- **🟢 No Spam (✅)**

---

## 🧪 Tecnologías utilizadas

- **Python 3.10+**
- **Streamlit** (UI)
- **OpenAI API** (embeddings)
- **scikit-learn** (clasificador)
- **pandas / numpy**
- **dotenv**

---
