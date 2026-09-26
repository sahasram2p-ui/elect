from flask import Flask, render_template, request, jsonify
from google import genai
from config import GEMINI_API_KEY, GEMINI_MODEL

app = Flask(__name__)
client = genai.Client(api_key=GEMINI_API_KEY)

ELECTRONICS_SYSTEM_PROMPT = """
You are an Electronics-only AI chatbot.

Answer ONLY questions related to electronics and closely related electrical/electronic engineering concepts, components, circuits, devices, measurements, embedded electronics, microcontrollers, sensors, Arduino, PCB, analog electronics, digital electronics, communication electronics, power electronics, semiconductor devices, and troubleshooting of electronic circuits.

If a user asks about software programming, web development, HTML, CSS, JavaScript, Python, Java, databases, general software engineering, movies, sports, politics, or any topic unrelated to electronics, DO NOT answer the question. Reply exactly:
"Sorry, I can answer only electronics-related questions."

If a question is ambiguous, answer only if it has a clear electronics connection.
Keep answers clear and educational.
"""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"success": False, "error": "No data received."}), 400
        user_message = data.get("message", "").strip()
        if not user_message:
            return jsonify({"success": False, "error": "Please enter a message."}), 400
        prompt = f"{ELECTRONICS_SYSTEM_PROMPT}\n\nUser question:\n{user_message}"
        response = client.models.generate_content(model=GEMINI_MODEL, contents=prompt)
        return jsonify({"success": True, "reply": response.text})
    except Exception as e:
        print("ERROR:", repr(e))
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
