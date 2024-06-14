# YOLOv8 Object Detection API

This project provides a FastAPI-based API for performing object detection using YOLOv8 Small model. Users can upload images, and the API will detect objects in the image and return the results.

## Features

- Accepts image uploads in JPEG and PNG formats.
- Performs object detection using YOLOv8 Small model.
- Returns detected objects with their class, confidence, and bounding box coordinates.
- Handles errors gracefully and returns appropriate HTTP responses.

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- `fastapi` library
- `uvicorn` library
- `numpy` library
- `opencv-python-headless` library
- `pydantic` library
- `ultralytics` library

You can install the required Python libraries using the following command:

```bash
pip install fastapi uvicorn numpy opencv-python-headless pydantic ultralytics
```

## Usage

- Clone the repository:

``` bash 
git clone https://github.com/RimshaNawaz/ML-Internship.git
```

- Navigate to the project directory:

``` bash 
cd 14-06-24
```
- Run the FastAPI application:

``` bash
uvicorn main:app --reload
```

## API Endpoints

### POST /detect_objects

- **Description**: Endpoint to detect objects in an uploaded image.
  
  **Parameters**:
  - `file`: The image file to be uploaded (JPEG or PNG format).
  
  **Returns**:
  - JSON response containing detected objects with their class, confidence, and bounding box coordinates.

### GET /

- **Description**: Root endpoint returning a welcome message.

  **Returns**:
  - JSON response with a welcome message.

## Output

- Detected objects are returned as JSON responses.
- Errors are handled gracefully with appropriate HTTP status codes and error messages.

## Note

- This API uses the YOLOv8 Small model for object detection. Ensure that the model file `yolov8s.pt` is located in the same directory as the main script or provide the correct path to the model file in the code.

- You can replace `"yourusername/your-repo"` in the clone command with your actual GitHub repository URL. 

- This README provides instructions for setting up and using the YOLOv8 Object Detection API, along with details about its features, usage, and output.
