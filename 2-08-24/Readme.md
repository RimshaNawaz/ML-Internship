# Specialist Recommendation System using RAG

This Gradio application recommends specialist doctors based on the symptoms provided by the user. The application utilizes the RAG (Retrieval-Augmented Generation) technique, but without embeddings, to match the input symptoms with the Mayo Clinic dataset and provide the corresponding specialist doctor.

## Features

- **Symptom Input**: Users can enter their symptoms in a text box.
- **Specialist Recommendation**: The system returns the name(s) of the specialist doctor(s) based on the symptoms provided.
- **Data Source**: Uses a custom Mayo Clinic dataset that includes symptoms and corresponding specialist doctors.

## Usage

1. **Clone the repository:**
  ``` bash 
git clone https://github.com/RimshaNawaz/ML-Internship.git
```

2.  **Navigate to the project directory:**
```bash
   cd 02-08-24
```
## Installation

To run this application, you need to install the following Python packages:

```bash
pip install pandas gradio
```

## Dataset

The dataset should be an Excel file named MayoClinic_Diseases(Custom Sheet).xlsx with at least two columns:

`Symptoms:` The symptoms described in text.

`Specialist Doctor:` The name of the specialist doctor corresponding to the symptoms.

## Usage

- **Load the Dataset:** Ensure the dataset is located at the correct file path.
- **Run the Application:** Execute the Python script to launch the Gradio interface.

## Running the Application:

- Save the code to a Python file (e.g., app.py).
- Ensure the dataset file is in the correct location.
- Run the Python script:
```bash
python app.py
```
A Gradio interface will launch in your default web browser.