from flask import Flask, render_template, request, jsonify
import json
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

class LLMAvatar:
    """
    A class to represent a Language Learning Model (LLM) Avatar.

    Attributes
    ----------
    model_name : str
        Name of the model to be used for prediction.
    url : str
        URL of the API endpoint.
    api : str
        API key for authentication.

    Methods
    -------
    llm_prediction(message: str)
        Makes a prediction based on the user's message.
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the LLMAvatar object.
        """
        self.model_name = os.getenv('MODEL_NAME')
        self.url = os.getenv('OPEN_ROUTER_URL')
        self.api = os.getenv('OPEN_API_KEY')

    def llm_prediction(self, message: str):
        """
        Makes a prediction based on the user's message.

        Parameters
        ----------
        message : str
            The user's input message.

        Returns
        -------
        dict
            The response from the LLM model in JSON format.
        """
        headers = {
            "Authorization": f'Bearer {self.api}',
            "Content-Type": "application/json"
        }
        data = json.dumps({
            "model": self.model_name,
            "messages": [{"role": "user", "content": message}]
        })
        response = requests.post(url=self.url, headers=headers, data=data)
        return response.json()

avatar = LLMAvatar()

@app.route('/')
def index():
    """
    Renders the index page.

    Returns
    -------
    str
        The rendered HTML content of the index page.
    """
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """
    Handles the chat functionality by receiving the user's message and
    returning the model's response.

    Returns
    -------
    Response
        A JSON response containing the model's prediction.
    """
    user_message = request.json['message']
    response = avatar.llm_prediction(user_message)
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
