# Electronics Chatbot

A Flask + Google Gemini AI chatbot that answers only electronics-related questions.

## Setup
1. `python -m venv venv`
2. `venv\Scripts\activate`
3. `pip install -r requirements.txt`
4. Put your Gemini API key in `.env`.
5. Run `python app.py`
6. Open `http://127.0.0.1:5000`

Non-electronics questions receive: "Sorry, I can answer only electronics-related questions."
