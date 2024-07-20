# Image Segmentation with FastAPI

This project is a FastAPI application for performing image segmentation on a user-uploaded image, based on user-specified coordinates. The model used for segmentation is FCN ResNet50 from the PyTorch library.
## Table of Contents
- [Features](#features)
- [Usage](#usage)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [API Endpoint](#api-endpoint)

## Features

- **User-Specified Coordinates:** Allows users to specify the region of interest in the image for segmentation by providing coordinates.
- **Segmentation Overlay:** Overlays the segmentation result on the original image for better visualization.
- **Pre-trained Model:** Utilizes the pre-trained FCN ResNet50 model for accurate segmentation results.
- **File Upload:** Supports image file upload through a POST request.
- **Real-Time Processing:** Provides real-time segmentation results by processing the image and returning the segmented output quickly.

## Prerequisites

- Python 3.7 or later
- FastAPI
- Uvicorn
- Pillow
- Torch
- Torchvision
## Usage

1. **Clone the repository:**
  ``` bash 
git clone https://github.com/RimshaNawaz/ML-Internship.git
```

2.  **Navigate to the project directory:**
```bash
   cd 19-07-24
```

## Installation

2. Install the required dependencies:

    ```sh
    pip install fastapi uvicorn pillow torch torchvision
    ```

## Running the Application

1. Start the FastAPI application with Uvicorn:

    ```sh
    uvicorn main:app --reload
    ```

2. The application will be available at `http://127.0.0.1:8000`.

## API Endpoint

### Perform Segmentation

- **URL:** `/segmentation/`
- **Method:** `POST`
- **Content-Type:** `multipart/form-data`
- **Parameters:**
  - `image`: The image file to be segmented.
  - `task_name`: A string indicating the task name.
  - `model_name`: A string indicating the model name.
  - `left`: The left coordinate of the region to segment.
  - `upper`: The upper coordinate of the region to segment.
  - `right`: The right coordinate of the region to segment.
  - `lower`: The lower coordinate of the region to segment.

- **Example Request using `curl`:**

    ```sh
    curl -X POST "http://127.0.0.1:8000/segmentation/" -F "image=@path/to/your/image.jpg" -F "task_name=segmentation" -F "model_name=fcn_resnet50" -F "left=50" -F "upper=50" -F "right=200" -F "lower=200"
    ```

- **Response:**

  - The endpoint returns the segmented image.

## Code Explanation

- **Imports and Initial Setup:**
  - Imports necessary libraries and initializes the FastAPI application.
  - Downloads and loads the pre-trained FCN ResNet50 model from Torchvision.

- **Image Preprocessing:**
  - Defines image transformations such as resizing, converting to tensor, and normalizing.

- **Segmentation Function:**
  - The `segment_image_with_coordinates` function performs segmentation on a specified region of the image.
  - It crops the image based on provided coordinates, preprocesses it, performs segmentation, and overlays the segmentation result on the original image.

- **API Endpoint:**
  - The `/segmentation/` endpoint handles image upload and performs segmentation based on user-provided coordinates.
  - It reads the uploaded image, calls the segmentation function, and returns the segmented image as a response.

