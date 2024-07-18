# Image Classification API with FastAPI

This repository contains an implementation of an image classification API using FastAPI. The API utilizes a pre-trained ResNet-18 model to classify uploaded images.

## Table of Contents
- [Features](#features)
- [Usage](#usage)
- [Installation](#installation)
- [API Endpoint](#api-endpoint)

## Features

- **Image Classification:** Classify images using a pre-trained ResNet-18 model.
- **FastAPI Framework:** Utilizes FastAPI to create a fast and efficient web API.
- **Preprocessing Pipeline:** Automatically resizes, crops, normalizes, and converts images to tensors.
- **JSON Labels:** Fetches human-readable labels for classification from a GitHub repository.
- **Error Handling:** Includes error handling to manage issues during image processing and classification.

## Usage

1. **Clone the repository:**
  ``` bash 
git clone https://github.com/RimshaNawaz/ML-Internship.git
```

2.  **Navigate to the project directory:**
```bash
   cd 18-07-24
```

## Installation

3. **Install the required packages:**
    ```bash
    pip install fastapi uvicorn torch torchvision pillow requests
    ```

## To Run the Task

To start the FastAPI server, run:
```bash
python yourfile.py
```

The server will start at http://127.0.0.1:8000.


## API Endpoint

### `POST /classify_image/`

Upload an image to classify it using the pre-trained ResNet-18 model.

#### Request Parameters
- `file` (required): The image file to be classified.
- `model_name` (optional): Placeholder for model name, not used in the current implementation.
- `task` (optional): Placeholder for task name, not used in the current implementation.

#### Response
- `classification` (string): The classification label of the uploaded image.
- `error` (string): Error message if there is an issue processing the image.


### Additional Information
- The API uses a pre-trained ResNet-18 model from the torchvision.models module.
- The image preprocessing steps include resizing, center cropping, normalization, and conversion to tensor.