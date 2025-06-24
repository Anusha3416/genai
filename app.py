from flask_cors import CORS # first i imported the cors module to take care of the cross-origin requests
from flask import Flask, request, jsonify   #i need to import flask too to handle requests and make an app if i want to 
from langchain_google_genai import ChatGoogleGenerativeAI # this is where im importing the google generative AI module from langchain
from dotenv import load_dotenv #this is to ensure security and load environment variables
import os 



load_dotenv() # env variable
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY") # getting the google api key from the env variable

# initialising the google generative ai model gemini 2.0 flash
llm = ChatGoogleGenerativeAI( 
    model="gemini-2.0-flash", 
    
    temperature=0.7
)
app = Flask(__name__) # create flask app
CORS(app) #enabling cors for app
@app.route("/invoke", methods=["POST"])#route to handle requests to the /invoke endpoint
#handling the chat request
def chat():
    data = request.json
    message = data.get("message", "")
    if not message:
        return jsonify({"error": "No message provided"}), 400
    result = llm.invoke(message)
    return jsonify({"response": result.content})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
#simple call
