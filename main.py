import os
import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from fastapi import status

load_dotenv()

app = FastAPI()


class TextRequest(BaseModel):
    prompt: str


# Checks if the API server is running
@app.get("/health", status_code=status.HTTP_200_OK)
async def health():
    try:
        return {"message": "API is running✅"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Something went wrong!",
        )


# Generates an image based on the provided prompt.
@app.post("/generate-image", status_code=status.HTTP_201_CREATED)
async def text_to_image(request: TextRequest):
    try:
        url = os.getenv("URL")
        token = os.getenv("TOKEN")

        payload = {"prompt": request.prompt, "aspect_ratio": "1:1"}

        headers = {
            "Content-Type": "application/json",
            "X-Api-Version": "v1",
            "Accept": "application/json",
            "Authorization": f"Bearer {token}",
        }

        response = requests.post(url, json=payload, headers=headers)

        data = response.json()
        return {"data": data}
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to generate image",
        )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
