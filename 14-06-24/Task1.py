"""FastAPI application integrating YOLOv8 Small for real-time object detection on image uploads."""
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from ultralytics import YOLO
import cv2
import numpy as np
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Load YOLOv8 Small model
try:
    model = YOLO("yolov8s.pt")
    logger.info("YOLOv8 model loaded successfully.")
except Exception as e:
    logger.error(f"Error loading YOLOv8 model: {str(e)}")
    raise RuntimeError("Error loading YOLOv8 model")

class DetectedObject(BaseModel):
    """Represents a detected object."""
    class_id: int
    class_name: str
    confidence: float
    box: tuple

class DetectionResponse(BaseModel):
    """Response model containing detected objects."""
    objects: list[DetectedObject]
    error: str = None

@app.post("/detect_objects", response_model=DetectionResponse)
async def detect_objects(file: UploadFile = File(...)):
    """Endpoint to detect objects in an uploaded image.

       Parameters:
       -----
        file (UploadFile): The image file to be uploaded (JPEG or PNG format).

        Returns:
        --------
        DetectionResponse: JSON response containing detected objects with their class, confidence, and bounding box coordinates.
    """
    try:
        # Validate file type
        if file.content_type not in ["image/jpeg", "image/png"]:
            logger.error(f"Invalid file type: {file.content_type}")
            raise HTTPException(status_code=400, detail="Invalid file type. Only JPEG and PNG are supported.")

        # Read image
        image_bytes = await file.read()
        np_arr = np.frombuffer(image_bytes, np.uint8)
        image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        # Check if image is read properly
        if image is None:
            logger.error("Invalid image data. Could not decode image.")
            raise HTTPException(status_code=400, detail="Invalid image data. Could not decode image.")

        # Perform object detection
        results = model(image, agnostic_nms=True)

        objects = []
        for result in results:
            for detection in result.boxes.data:
                x1, y1, x2, y2, confidence, class_id = detection[:6]
                objects.append(DetectedObject(
                    class_id=int(class_id),
                    class_name=model.names[int(class_id)],
                    confidence=float(confidence),
                    box=(int(x1), int(y1), int(x2), int(y2))
                ))

        return DetectionResponse(objects=objects)

    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return JSONResponse(
            status_code=500,
            content={"error": f"Internal Server Error. Please try again later. Error details: {str(e)}"}
        )

@app.get("/")
async def root():
   
    """Root endpoint returning a welcome message.

    Returns:
    --------
        dict: JSON response with a welcome message.
    """
    
    return {"message": "Welcome to the YOLOv8 Object Detection API"}

# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
