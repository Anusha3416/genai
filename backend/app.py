from flask_cors import CORS
from flask import Flask, request, jsonify   
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os


# Load from .env if you're using it
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")


# Create the LLM with Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash", 
     # Use "gemini-pro" for text
    temperature=0.7
)
app = Flask(__name__)
CORS(app)
@app.route("/invoke", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message", "")
    if not message:
        return jsonify({"error": "No message provided"}), 400
    result = llm.invoke(message)
    return jsonify({"response": result.content})
if __name__ == "__main__":
    app.run(debug=True)
# Simple call
