# Real-Time Speech-to-Text Application

## Overview

This application allows users to perform real-time speech-to-text conversion using a web interface. Users can speak into their microphone, and the spoken words will be converted into text, displayed in real-time on the webpage.

## Installation

### Prerequisites

- Flask and SpeechRecognition libraries installed

   ```bash
    from flask import Flask, render_template, jsonify, request
    import speech_recognition as sr
    ```
### Installation Steps

- Clone the repository:

   ```bash
   git clone https://github.com/RimshaNawaz/ML-Internship.git
    ```
    
- Navigate to the project directory:

   ``` bash 
    cd 20-06-24
   ```    

## Usage   
1. Start the Flask server:

  ``` bash 
    python server.py
```
The server will start running on http://localhost:5000.

2. Open a web browser and go to http://localhost:5000.
3. Click the "Start Listening" button on the webpage.
4. Allow microphone access if prompted by the browser.
5. Speak into the microphone. The recognized text will appear in real-time on the webpage.
6. To stop listening, click the "Start Listening" button again.


## Dependencies

- Flask: Web framework for Python.
- SpeechRecognition: Library for performing speech recognition.



## Explanation:

- **Overview:** Provides a brief introduction to what the application does.
- **Installation:** Details the prerequisites and steps needed to set up the application.
- **Usage:** Describes how to run and interact with the application.
- **File Structure:** Lists the main files and directories in the project.
- **Dependencies:** Lists the external libraries required for the application.
- **Notes:** Provides additional information and considerations for using the application effectively.

