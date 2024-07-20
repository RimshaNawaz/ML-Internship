import uvicorn
from fastapi import FastAPI, File, UploadFile, Form, Query
from fastapi.responses import FileResponse
import io
import torch
import torchvision.models as models
from torchvision.transforms import Compose, Resize, ToTensor, Normalize, ToPILImage
from PIL import Image

# Initialize FastAPI
app = FastAPI()

# Manually download and load FCN ResNet50
model = models.segmentation.fcn_resnet50(pretrained=True)
model.eval()

# Define the image transformations
preprocess = Compose([
    Resize((256, 256)),
    ToTensor(),
    Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Function to perform segmentation based on user-provided coordinates
def segment_image_with_coordinates(input_image, coordinates):
    # Convert provided coordinates to tuple (left, upper, right, lower)
    left, upper, right, lower = coordinates
    segmentation_coordinates = (left, upper, right, lower)
    
    # Crop the image based on provided coordinates
    roi = input_image.crop(segmentation_coordinates)

    # Preprocess the ROI
    roi_tensor = preprocess(roi)
    roi_batch = roi_tensor.unsqueeze(0)  # create a mini-batch as expected by the model

    # Perform segmentation inference on the ROI
    with torch.no_grad():
        output = model(roi_batch)['out'][0]  # Assuming batch size is 1, get the output

    # Convert segmentation output to a PIL image for visualization
    output_predictions = output.argmax(0).byte()  # Take the argmax to get the predicted class for each pixel
    output_predictions_pil = ToPILImage()(output_predictions)

    # Convert the ROI image to RGBA format for overlaying
    roi_rgba = roi.convert("RGBA")

    # Create a transparent mask for segmentation overlay
    overlay_color = (0, 255, 0, 100)  # Green with 50% opacity (RGBA format)
    segmentation_overlay = Image.new("RGBA", roi.size, overlay_color)

    # Overlay the segmentation on the ROI image
    segmented_roi = Image.alpha_composite(roi_rgba, segmentation_overlay)

    # Replace the ROI region in the original image with the segmented ROI
    input_image.paste(segmented_roi, segmentation_coordinates)

    return input_image

# FastAPI endpoint to perform segmentation with user-specified coordinates
@app.post("/segmentation/")
async def perform_segmentation(
    image: UploadFile = File(...),
    task_name: str = Form(...),
    model_name: str = Form(...),
    left: int = Form(...),
    upper: int = Form(...),
    right: int = Form(...),
    lower: int = Form(...),
):
    try:
        # Read and open the uploaded image
        contents = await image.read()
        img_pil = Image.open(io.BytesIO(contents))
        
        # Perform segmentation based on user-provided coordinates
        user_coordinates = (left, upper, right, lower)
        segmented_image = segment_image_with_coordinates(img_pil, user_coordinates)

        # Save the segmented image temporarily
        segmented_image_path = "segmented_output.png"
        segmented_image.save(segmented_image_path)

        # Return the segmented image as a response
        return FileResponse(segmented_image_path, media_type='image/png')

    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
