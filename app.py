from flask import Flask, request, jsonify
import os

app = Flask(__name__)

VERIFY_TOKEN = "mi_token_123"

# 🔹 Verificación de Meta (esto es lo que preguntabas)
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
    data = request.json
    print("Mensaje recibido:", data)

    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))