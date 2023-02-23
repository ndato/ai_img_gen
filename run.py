import os
from ai_img_gen import create_images, init_openai
from dotenv import load_dotenv

load_dotenv('.env')
init_openai(os.environ.get('SECRET_KEY'))

while True:
    print("Press CTRL + C to exit.")
    img_size_str = input("Enter Image Size (Large, Medium, Small): ")
    img_size_dict = {"large": "1024x1024",
                     "medium": "512x512",
                     "small": "256x256"}
    img_size = img_size_dict.get(img_size_str.lower(), "1024x1024")
    num_images = int(input("Enter Number of Images: "))

    prompt = input("Enter Prompt: ")

    image_urls = create_images(
        prompt=prompt,
        img_size=img_size,
        num_images=num_images
    )

    for i, image_url in enumerate(image_urls):
        print(f'Image {i + 1}:\n{image_url}')
