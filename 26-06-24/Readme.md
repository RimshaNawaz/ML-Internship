# YOLOv8 Object Tracking

This project utilizes YOLOv8 for object tracking in videos and counts how many objects cross a defined line. It includes a Gradio interface for easy interaction.

## Features

- Object detection and tracking using YOLOv8.
- Counts objects that cross a defined line in the video.
- Annotations and visualizations overlayed on the processed video.
- Gradio interface for uploading and processing videos.

## Setup

1. Clone the repository:

``` bash 
git clone https://github.com/RimshaNawaz/ML-Internship.git
```

2. Navigate to the project directory:

``` bash 
cd 26-06-24
```
3. Download YOLOv8 model:

    Download `yolov8n.pt` and place it in the project directory.


## Prerequisites

Ensure you have the following installed:

- Python 3.x
- `pip` for package installation
- Required Python packages:
  - `ultralytics`
  - `torch`
  - `opencv-python`
  - `supervision`
  - `gradio`

Install the required packages using:

```bash
pip install ultralytics torch opencv-python supervision gradio
```    

## Usage

``` bash
python <your_gradio_script>.py
````
- Upload a video file using the interface.

- View the processed video with object annotations.    

## Parameters
- `video_file:` Path to the video file you want to process.

## Outputs

- The processed video is saved in the system's temporary directory as output_single_lines.mp4.