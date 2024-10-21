from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pytube import YouTube
from fastapi.responses import FileResponse
import os

app = FastAPI()

# Allow CORS (Cross-Origin Resource Sharing) for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # This allows requests from any origin (for testing purposes)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Directory to store downloaded videos
DOWNLOAD_DIR = "videos"
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

@app.post("/download")
async def download_video(request: Request):
    data = await request.json()
    video_url = data.get("url")

    try:
        yt = YouTube(video_url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').first()

        if stream:
            video_path = os.path.join(DOWNLOAD_DIR, "video.mp4")
            stream.download(output_path=DOWNLOAD_DIR, filename="video.mp4")
            return FileResponse(video_path, media_type="video/mp4", filename="video.mp4")
        else:
            return {"error": "No valid video stream found"}
    except Exception as e:
        return {"error": str(e)}




