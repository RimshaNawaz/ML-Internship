from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import speech_recognition as sr

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('audio_data')
def handle_audio(data):
    recognizer = sr.Recognizer()
    audio = sr.AudioData(data, 16000, 2)
    try:
        text = recognizer.recognize_google(audio)
        emit('text_data', text)
    except sr.UnknownValueError:
        emit('text_data', "Could not understand audio")
    except sr.RequestError as e:
        emit('text_data', f"Could not request results; {e}")

if __name__ == '__main__':
    socketio.run(app, debug=True)
