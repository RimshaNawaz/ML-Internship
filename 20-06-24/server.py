" Real-Time Speech-to-Text Application "

from flask import Flask, render_template, jsonify, request
import speech_recognition as sr

app = Flask(__name__)

@app.route('/')
def index():
    """
    Renders the index.html page for the speech-to-text interface.

    Returns:
    -------
        str: The rendered HTML content of the index.html page.

    Note:
    -----
        This function uses Flask's render_template function to render the index.html page,
        which serves as the interface for the real-time speech-to-text application.
    """
    return render_template('index.html')

@app.route('/speech-to-text', methods=['POST'])
def speech_to_text():
    """
    Accepts audio data, performs speech recognition, and responds with recognized text.

    Returns:
    --------
        JSON object:
            - If successful: {'text': 'Recognized text'}
            - If error occurs: {'error': 'Error message'}
    """
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file found'})

    audio_file = request.files['audio']
    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(audio_file) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
            return jsonify({'text': text})
    except sr.UnknownValueError:
        return jsonify({'error': 'Speech recognition could not understand audio'})
    except sr.RequestError as e:
        return jsonify({'error': f'Recognition service error: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True)
