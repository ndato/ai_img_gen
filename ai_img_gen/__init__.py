import os
import openai
from dotenv import load_dotenv

load_dotenv('.env')

openai.api_key = os.environ.get('SECRET_KEY')

def show_model()-> None:
    openai.Model.list()

def create_images(prompt: str, img_size: str, num_images: int) -> list:
    """Create Image from a Prompt using the OpenAI DALL-E model.

    Args:
        prompt (str): Message prompt to be used to generate the image.
        img_size (str): Image pixel size. Accepts the following inputs: ["256x256", "512x512, "1024x1024"]
        num_images (int): Number of images to request.

    Returns:
        list: List of URL of all the Generated Images.
    """
    try:
        response = openai.Image.create(
            prompt=prompt,
            n=num_images,
            size=img_size
        )
    except openai.error.OpenAIError as e:
        print(e.http_status)
        print(e.error)
        return []

    image_urls = list()
    for data in response.get('data', []):
        image_urls.append(data['url'])

    return image_urls
