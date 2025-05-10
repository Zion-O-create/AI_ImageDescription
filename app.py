import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv('KEY')



from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import requests
import io
import base64
from huggingface_hub import InferenceClient

# Initialize FastAPI app
app = FastAPI()

# Enable CORS for frontend-backend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Hugging Face Model API (Using Together.ai provider)
API_KEY = key  # Replace with your actual Hugging Face API key
client = InferenceClient(provider="together", api_key=key)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    # Read the image
    image = await file.read()
    img = Image.open(io.BytesIO(image))

    # Convert image to base64
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    img_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

    # Send image and prompt to Hugging Face API
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Tell a story from this image."},
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{img_base64}"}}
            ]
        }
    ]

    try:
        completion = client.chat.completions.create(
            model="meta-llama/Llama-3.2-11B-Vision-Instruct", 
            messages=messages, 
            max_tokens=500
        )
        description = completion.choices[0].message["content"]
    except Exception as e:
        description = f"Error generating description: {str(e)}"

    return {"description": description}
