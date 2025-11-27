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

Este proyecto implementa un **clasificador de spam** para el *subject* (asunto) de correos electrónicos.  
Hace parte de mi trabajo en la **Maestría en Inteligencia Artificial**, en la asignatura *Hackeando la Inteligencia Artificial*, donde exploramos cómo aprovechar modelos fundacionales (LLMs) combinados con técnicas tradicionales de Machine Learning.

---

## 🧠 Descripción del proyecto

El objetivo principal es entrenar un sistema que detecte si el asunto de un correo es:

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

Aquí uso el nombre `venvspam`, pero puede ser cualquiera:

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

1. La app entrenará el modelo la primera vez (queda cacheado).  
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

## 🎯 Objetivo académico

Este proyecto busca mostrar cómo:

- Los **embeddings de un LLM** pueden integrarse con modelos tradicionales.  
- Se puede “hackear” y reaprovechar la capacidad semántica de los LLMs.  
- Los modelos ligeros siguen siendo útiles y eficientes en tareas de clasificación.  

Ideal como ejercicio para la materia *Hackeando la Inteligencia Artificial*.

---

## 🚀 Mejoras futuras

Algunas ideas para extender este proyecto:

- Persistencia del modelo con `joblib` para evitar reentrenar.  
- Añadir explicabilidad (SHAP / LIME).  
- API REST con FastAPI.  
- Añadir análisis del cuerpo completo del correo.  
- Pipeline MLOps simple.

---

## 👨‍🎓 Autor

Proyecto realizado como parte de la **Maestría en Inteligencia Artificial**.  
Comentarios, mejoras o PRs son bienvenidos.
