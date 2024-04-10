from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from typing import List

router = APIRouter()

@router.post("/generate-sample-frame")
async def generate_sample_frame(video: UploadFile = File(...), 
                        text_type: str = Form(...),
                        x: str = Form(...),
                        y: str = Form(...),
                        w: str = Form(...),
                        h: str = Form(...)):
    
    # look for image_file at the root of the project
    image_file = "images/sample_image.jpg"

    # return the path to the image file
    return {"image_file": image_file}