import uvicorn
from fastapi import FastAPI, UploadFile, File
import torch
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image
import requests

app = FastAPI()

# Load the pre-trained model
model = models.resnet18(pretrained=True)
model.eval()

# Define the image transformations
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Load the labels
LABELS_URL = "https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/imagenet-simple-labels.json"
labels = requests.get(LABELS_URL).json()

# Function to classify an image
def classify_image(image_path):
    try:
        # Load and preprocess the input image
        input_image = Image.open(image_path)
        input_tensor = preprocess(input_image)
        input_batch = input_tensor.unsqueeze(0)  # create a mini-batch as expected by the model

        # Perform inference
        with torch.no_grad():
            output = model(input_batch)

        # Get the classification label
        _, predicted_idx = torch.max(output, 1)
        label = labels[predicted_idx] if labels else "Unknown"

        return label

    except Exception as e:
        print(f"Error classifying image: {e}")
        return "Error"

# API endpoint to classify image
@app.post("/classify_image/")
async def classify_image_api(file: UploadFile = File(...), model_name: str = "", task: str = ""):
    try:
        # Save uploaded image
        with open(file.filename, "wb") as image:
            image.write(file.file.read())

        # Perform classification
        classification = classify_image(file.filename)

        return {"classification": classification}

    except Exception as e:
        return {"error": f"Error processing image: {e}"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
