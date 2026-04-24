from flask import Flask, request, jsonify
import os
import logging
import requests 

app = Flask(__name__)

# 🔥 Logging bien configurado para Render
logging.basicConfig(level=logging.INFO)

VERIFY_TOKEN = "mi_token_123"

# 🔹 Ruta base
@app.route("/")
def home():
    return "VERSION NUEVA! Servidor funcionando 🚀"

# 🔹 Verificación de Meta
@app.route("/webhook", methods=["GET"])
def verify():
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if token == VERIFY_TOKEN:
        return challenge
    return "Error de verificación", 403

# 🔹 Recepción de mensajes
import requests

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()

    try:
        # enviar a n8n
        requests.post(
            "https://n8n-service-jelf.onrender.com/webhook/whatsapp",
            json=data
        )

        logging.info("📤 Enviado a n8n")

    except Exception as e:
        logging.error(f"Error enviando a n8n: {e}")

    return jsonify({"status": "ok"})

# 🔹 Run para Render
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))