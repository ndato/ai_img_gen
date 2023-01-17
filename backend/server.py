import os

from fastapi import FastAPI, Form
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

from ai_img_gen import create_images

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def get_root() -> str:
    """Return string on root address.

    Returns:
        str: "Hello World!"
    """
    return "Hello World!"


@app.get("/favicon.ico", include_in_schema=False)
async def get_favicon() -> FileResponse:
    """Return the Browser Icon.

    Returns:
        FileResponse: URL Path to the Browser Icon.
    """
    static_file_path = "static/images/pizza.png"
    return FileResponse(static_file_path)


@app.post("/images/")
async def get_image_requests(prompt: str = Form(default=""),
                             img_size: str = Form(default="large"),
                             num_images: int = Form(default=1))\
                                -> JSONResponse:
    """Endpoint for getting a list of Created Image from
       a Prompt using the OpenAI DALL-E model. 

    Args:
        prompt (str, optional): Message prompt to be used to generate
                                the image. Defaults to "".
        img_size (str, optional): Image pixel size. Accepts the following
                                  inputs: ["small", "medium", "large"].
                                  Defaults to "large".
        num_images (int, optional): Number of images to request.
                                    Defaults to 1.

    Returns:
        JSONResponse: JSON containing a list of URLs of the
                      Generated Images.
    """

    img_size_dict = {
        "large": "1024x1024",
        "medium": "512x512",
        "small": "256x256"
    }
    img_size = img_size_dict.get(img_size.lower(), "1024x1024")

    image_urls = create_images(
        prompt=prompt,
        img_size=img_size,
        num_images=num_images
    )

    content = {"images": image_urls}

    return JSONResponse(content=content)