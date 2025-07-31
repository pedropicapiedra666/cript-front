from nicegui import ui
import requests
import webbrowser

API_URL = "https://cript-dy96.onrender.com"

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

with ui.column().classes('w-full max-w-md mx-auto p-4 bg-white shadow rounded-lg mt-10'):
    ui.label("Cripter").classes('text-2xl font-bold mb-4 text-center')

    ui.label("Mensaje:")
    mensaje = ui.textarea(placeholder="Escribe tu mensaje...").classes('w-full mb-2')

    ui.label("Clave:")
    clave = ui.input(placeholder="Clave de cifrado", password=True, password_toggle_button=True).classes('w-full mb-4')

    with ui.row().classes('justify-between w-full'):
        ui.button("Cifrar", on_click=cifrar).classes('bg-blue-500 text-white px-4 py-2 rounded')
        ui.button("Descifrar", on_click=descifrar).classes('bg-green-500 text-white px-4 py-2 rounded')

    ui.label("Resultado:").classes('mt-4')
    resultado = ui.label("").classes('bg-gray-100 p-2 rounded w-full')

    with ui.row().classes('justify-center w-full mt-2'):
        copiar_button = ui.image('assets/icons/list.png').on('click', copiar_resultado).classes('cursor-pointer w-10 h-10')
        whatsapp_button = ui.image('assets/icons/whatsapp.png').on('click', compartir_whatsapp).classes('cursor-pointer w-10 h-10')
        telegram_button = ui.image('assets/icons/telegram.png').on('click', compartir_telegram).classes('cursor-pointer w-10 h-10')

        actualizar_botones(False)

ui.run()
