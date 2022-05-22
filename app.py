from flask import  Flask,jsonify
import os
import chatbot
app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome"

@app.route("/<string:question>")
def get_message(question):
    message = chatbot.chat(question)
    return jsonify({"message" : message})


