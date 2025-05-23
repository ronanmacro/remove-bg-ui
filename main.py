from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from rembg import remove
from PIL import Image
import io

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or use your site URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/remove-bg")
async def remove_bg(file: UploadFile = File(...)):
    input_data = await file.read()
    output_data = remove(input_data)
    return StreamingResponse(io.BytesIO(output_data), media_type="image/png")
