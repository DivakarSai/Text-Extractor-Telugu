from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI, UploadFile, File
from typing import Dict

app = FastAPI()

@app.post("/api/process-video")
async def process_video(video: UploadFile = File(...)) -> Dict[str, int]:
    # Process the video to get its dimensions
    # Replace this with your actual video processing code
    # For demonstration purposes, let's assume we're getting the dimensions
    # of the first frame of the video
    video_dimensions = {"width": 1920, "height": 1080}  # Dummy dimensions

    return {"dimensions": video_dimensions}



