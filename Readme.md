# 🔐 CripterOn

CripterOn es una herramienta pública, libre y educativa de cifrado y descifrado de mensajes, desarrollada con fines demostrativos e interactivos.
El objetivo de este proyecto es mostrar cómo funcionan los principios de comunicación segura en la actualidad, inspirándose en tecnologías históricas como la máquina Enigma, pero adaptadas al entorno moderno con mejoras significativas.

## ✨ Características

* 🔑 Cifrado y descifrado de mensajes mediante una clave definida por el usuario.
* 🔄 Diccionario dinámico de cifrado:

  * El sistema actualiza automáticamente el mapa de sustitución de caracteres y palabras cada cierto tiempo.
  * Utiliza datos dinámicos generados de manera interna (seeds criptográficas) combinados con la clave ingresada por el usuario.
  * Esto garantiza que incluso con la misma clave, el resultado sea diferente en distintos momentos, ofreciendo una seguridad mucho mayor.
* 📱 Interfaz responsiva y amigable creada con NiceGUI.
* 📋 Copiado rápido del mensaje cifrado o descifrado.
* 📤 Compartir mensajes fácilmente mediante:

  * WhatsApp
  * Telegram
* 🔒 Ocultamiento de clave para mayor privacidad.
* 🌐 API desarrollada con FastAPI, desplegable de forma independiente al frontend.
* 🚀 Listo para desplegar en Render o Vercel.

## 📂 Estructura del proyecto

```
CripterOn/
│
├── cript-api/           # API backend con FastAPI
│   ├── main.py
│   └── requirements.txt
│
├── cript-frontend/      # Frontend con NiceGUI
│   ├── assets/icons     # Íconos de las acciones (copiar, whatsapp, telegram)
│   ├── main.py
│   └── requirements.txt
│
└── README.md            # Documentación del proyecto
```

## 🔐 Inspiración y funcionamiento

CripterOn toma como inspiración la máquina Enigma, utilizada durante la Segunda Guerra Mundial, pero incorpora mejoras modernas:

* Diccionario dinámico y variable en el tiempo, evitando patrones predecibles.
* Semillas criptográficas internas que refuerzan la entropía de cada cifrado.
* Interactividad en tiempo real, mostrando cómo los algoritmos pueden evolucionar.

Estas características buscan demostrar la importancia de la comunicación segura y cómo tecnologías modernas pueden superar las limitaciones históricas.

<!-- ## 🚀 Instalación y ejecución local

### 1️⃣ Clonar el repositorio:

```bash
git clone https://github.com/tu-usuario/CripterOn.git
cd CripterOn
```

### 2️⃣ Backend (API con FastAPI)

```bash
cd cript-api
python -m venv venv
source venv/bin/activate   # En Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

La API estará disponible en:
➡ [http://localhost:8000](http://localhost:8000)

### 3️⃣ Frontend (NiceGUI)

```bash
cd ../cript-frontend
python -m venv venv
source venv/bin/activate   # En Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

El frontend estará disponible en:
➡ [http://localhost:8080](http://localhost:8080) -->

## 🌍 Despliegue en la nube

* **Backend (API):** Render
* **Frontend:** Render o Vercel

Asegúrate de configurar la variable `API_URL` en el frontend para que apunte a la API desplegada.

## ⚠️ Aviso Legal

CripterOn es un proyecto con fines educativos e interactivos.
El cifrado es una tecnología poderosa que debe ser usada de manera responsable.
El desarrollador **NO** se hace responsable de usos indebidos de esta herramienta con fines ilegales o malintencionados.

Este proyecto busca demostrar la importancia de las libertades digitales, la privacidad y la regulación adecuada para evitar abusos en tecnologías de cifrado.

## 🛠 Tecnologías usadas

* Python 3.12
* FastAPI
* NiceGUI
* Requests

## 🏛 Inspiración

CripterOn se inspira en la máquina Enigma usada en la Segunda Guerra Mundial para mostrar cómo la comunicación segura puede ser comprendida y adaptada a nuestros tiempos modernos, promoviendo la educación en seguridad informática y demostrando que el cifrado dinámico es una de las herramientas más potentes para la privacidad.

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas!
Puedes proponer mejoras, reportar errores o agregar nuevas funcionalidades mediante Pull Requests o Issues.

## 📜 Licencia

Este proyecto está bajo la licencia MIT.
Consulta el archivo LICENSE para más información.
