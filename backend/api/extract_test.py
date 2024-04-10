from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from typing import List

router = APIRouter()

@router.post("/process-video")
async def process_video(video: UploadFile = File(...), 
                        text_type: str = Form(...),
                        x: str = Form(...),
                        y: str = Form(...),
                        w: str = Form(...),
                        h: str = Form(...)):
    # Process the video and other parameters here
    # You can access the uploaded video using the `video` parameter
    # Other parameters are passed as form data
    
    # Example: Save the video to disk
    # with open(f"uploaded_videos/{video.filename}", "wb") as buffer:
    #     buffer.write(await video.read())
    
    # Example: Print received data
    print("Received Video:", video.filename)
    print("Text Type:", text_type)
    print("X:", x)
    print("Y:", y)
    print("Width:", w)
    print("Height:", h)
    
    # You can return any processed data back to the frontend
    return {"message": "Video processed successfully"}
