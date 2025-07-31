from nicegui import ui
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import requests
import webbrowser
import os
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

API_URL = os.getenv("API_URL", "http://localhost:8000")

# Crear instancia de FastAPI
app = FastAPI()

# Servir carpeta assets manualmente
app.mount('/assets', StaticFiles(directory=os.path.join(os.path.dirname(__file__), 'assets')), name='assets')

def actualizar_botones(visible: bool):
    copiar_button.visible = visible
    whatsapp_button.visible = visible
    telegram_button.visible = visible

def cifrar():
    mensaje_valor = mensaje.value
    clave_valor = clave.value
    if not mensaje_valor or not clave_valor:
        resultado.text = "⚠️ Por favor, completa todos los campos."
        actualizar_botones(False)
        return
    
    try:
        res = requests.post(f"{API_URL}/cifrar", json={"mensaje": mensaje_valor, "clave": clave_valor})
        data = res.json()
        resultado.text = data.get("mensaje_cifrado", "Error al cifrar.")
        mensaje.value = ""
        clave.value = ""
        actualizar_botones(True)
    except:
        resultado.text = "❌ Error de conexión con la API."
        actualizar_botones(False)

def descifrar():
    mensaje_valor = mensaje.value
    clave_valor = clave.value
    if not mensaje_valor or not clave_valor:
        resultado.text = "⚠️ Por favor, completa todos los campos."
        actualizar_botones(False)
        return

    try:
        res = requests.post(f"{API_URL}/descifrar", json={"mensaje": mensaje_valor, "clave": clave_valor})
        data = res.json()
        resultado.text = data.get("mensaje_descifrado", "Error al descifrar.")
        mensaje.value = ""
        clave.value = ""
        actualizar_botones(True)
    except:
        resultado.text = "❌ Error de conexión con la API."
        actualizar_botones(False)

def copiar_resultado():
    if resultado.text:
        ui.run_javascript(f'navigator.clipboard.writeText("{resultado.text}")')
        ui.notify("📋 Mensaje copiado al portapapeles")

def compartir_whatsapp():
    if resultado.text:
        url = f"https://wa.me/?text={resultado.text}"
        webbrowser.open(url)

def compartir_telegram():
    if resultado.text:
        url = f"https://t.me/share/url?url=&text={resultado.text}"
        webbrowser.open(url)

# Fondo de pantalla
ui.add_head_html("""
<style>
    body {
        background-image: url('/assets/icons/background.jpg');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        margin: 0;
        font-family: 'Arial', sans-serif;
    }
</style>
""")

# UI
with ui.column().classes('w-full max-w-md mx-auto p-6 bg-white shadow-xl rounded-lg mt-10 items-center'):
    ui.label("CripterOn").classes('text-3xl font-bold mb-6 text-center text-gray-800')

    ui.label("Mensaje:").classes('self-start')
    mensaje = ui.textarea(placeholder="Escribe tu mensaje...").classes('w-full mb-3 resize-none')

    ui.label("Clave:").classes('self-start')
    clave = ui.input(placeholder="Clave de cifrado", password=True, password_toggle_button=True).classes('w-full mb-4')

    with ui.row().classes('w-full gap-2 flex-wrap'):
        ui.button("Cifrar", on_click=cifrar).classes('bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded flex-1')
        ui.button("Descifrar", on_click=descifrar).classes('bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded flex-1')

    ui.label("Resultado:").classes('mt-4 text-gray-700')
    resultado = ui.label("").classes('bg-gray-100 p-3 rounded w-full min-h-[50px]')

    with ui.row().classes('justify-center w-full mt-3 gap-4'):
        copiar_button = ui.image('assets/icons/list.png').on('click', copiar_resultado).classes('cursor-pointer w-10 h-10')
        whatsapp_button = ui.image('assets/icons/whatsapp.png').on('click', compartir_whatsapp).classes('cursor-pointer w-10 h-10')
        telegram_button = ui.image('assets/icons/telegram.png').on('click', compartir_telegram).classes('cursor-pointer w-10 h-10')

        actualizar_botones(False)

with ui.column().classes('w-full max-w-md mx-auto p-4 bg-white shadow-xl rounded-lg mt-6 items-center'):
    ui.label("💖 ¿Quieres colaborar con el creador?").classes('text-md font-semibold text-center mb-2')

    with ui.row().classes('justify-center gap-6 mt-2'):
        ui.image('assets/icons/bitcoin.png').on('click', lambda: (
            ui.run_javascript('navigator.clipboard.writeText("bc1q2t9n33jyvh0u6yxjlr5cvcg22t920ag9kfgv25")'),
            ui.notify("📋 Dirección BTC copiada")
        )).classes('cursor-pointer w-12 h-12')

        ui.image('assets/icons/usdt.png').on('click', lambda: (
            ui.run_javascript('navigator.clipboard.writeText("0xB43e1ec91fdb8c0DCB6188D480B58Dc0D14196a0")'),
            ui.notify("📋 Dirección USDT copiada")
        )).classes('cursor-pointer w-12 h-12')

# Solo exporta para Gunicorn si no es ejecución local
if os.getenv("RENDER") == "true":
    ui.run_with(app)  # ⬅️ se pasa la instancia de FastAPI
else:
    ui.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))
