# Specialist Recommendation System using RAG

This Gradio application recommends specialist doctors based on the symptoms provided by the user. The application utilizes the RAG (Retrieval-Augmented Generation) technique, but without embeddings, to match the input symptoms with the Mayo Clinic dataset and provide the corresponding specialist doctor.

## Project Structure

- **data/**: Contains the Excel file with disease, symptoms, and specialist data.
- `data_loader.py`: Handles loading data from the Excel file.
- `chromadb_client.py`: Initializes the ChromaDB client and manages collections.
- `specialist_finder.py`: Contains logic for querying the ChromaDB collection to find specialists.
- `gradio_app.py`: Sets up and launches the Gradio interface.


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
   cd 5-08-24
```
## Installation

To run this application, you need to install the following Python packages:

```bash
pip install pandas
```
```bash
pip install chromadb
```
```bash
pip install gradio
```

## Dataset

The dataset should be an Excel file named MayoClinic_Diseases(Custom Sheet).xlsx with at least two columns:

`Symptoms:` The symptoms described in text.

`Specialist Doctor:` The name of the specialist doctor corresponding to the symptoms.

## Usage

- **Load the Dataset:** Ensure the dataset is located at the correct file path.
- **Run the Application:** Execute the Python script to launch the Gradio interface.

## Running the Application:

- Save the code to a Python file (e.g., gradio_app.py).
- Ensure the dataset file is in the correct location.
- Run the Python script:
```bash
python gradio_app.py
```
A Gradio interface will launch in your default web browser.