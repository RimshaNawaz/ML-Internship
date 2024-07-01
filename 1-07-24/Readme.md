# LLM-Based Talking Avatar

This project is a Flask-based web application that uses a Language Learning Model (LLM) to create an interactive talking avatar. The avatar responds to user queries by making predictions based on the provided input.

# Code Explanation

### `llm_avatar.py`

- **Imports required libraries and modules.**
- **Loads environment variables using `dotenv`.**
- **Defines the `LLMAvatar` class with methods to interact with the LLM.**
- **Provides an example usage of the class to make a prediction.**

### `app.py`

- **Imports required libraries and modules.**
- **Loads environment variables using `dotenv`.**
- **Defines the `LLMAvatar` class with methods to interact with the LLM.**
- **Creates Flask routes to handle the web interface and chat functionality.**

## Features

- Interactive user interface for chatting with the LLM-based avatar.
- Uses environment variables for configuration.
- Clean and modular code structure.


## Installation

1. **Clone the repository**
   
``` bash 
git clone https://github.com/RimshaNawaz/ML-Internship.git
```

2.  Navigate to the project directory:

``` bash 
cd 1-07-24
```
## Prerequisites

- Python 3.7+
- Flask
- requests
- python-dotenv

2. **Create a `.env` file in the project root directory and add your environment variables**

    ```env
    MODEL_NAME=openchat/openchat-7b:free
    OPEN_ROUTER_URL=https://openrouter.ai/api/v1/chat/completions
    OPEN_API_KEY=your_open_api_key
    ```


## Usage of llm_avatar.py

1. **Run the script**

    ```bash
    python llm_avatar.py
    ```

2. **The script will output the model's response to a predefined user message**

    ```
    Making prediction with LLM
    Response: 200 - {"id":"cmpl- 
    6eOaDYJAI4tV8WhPhZB4","object":"text_completion","created":1679607073,"model":"text-davinci-    003","choices":[{"text":"Hello! How can I assist you today?","index":0,"logprobs":null,"finish_reason":"stop"}]}
    ```


## Usage of app.py

    
1. **Run the Flask application**

    ```bash
    python app.py
    ```

2. **Open your web browser and go to**

    ```
    http://127.0.0.1:5000/
    ```

3. **Interact with the avatar by typing your messages and receiving responses.**

## Project Structure
1-07-24/
│
├── app.py                # Main Flask application
├── templates/
│   └── index.html        # HTML template for the web interface
├── static/
│   ├── videos/           # Folder for videos
│   │   └── avatar_talking.mp4   # Example video file
│   └── images/           # Folder for images
│       └── avatar_still.png   # Example image file
├── .env                  # Environment variables
└── README.md             # Project documentation


