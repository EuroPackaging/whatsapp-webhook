from flask import Flask, request, jsonify
import os
import logging

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
@app.route("/webhook", methods=["POST"])
def webhook():
    logging.info("🔥 NUEVO EVENTO 🔥")

    try:
        data = request.get_json()
        logging.info(f"JSON recibido: {data}")
    except Exception as e:
        logging.error(f"Error parseando JSON: {e}")

    return jsonify({"status": "ok"})

# 🔹 Run para Render
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))