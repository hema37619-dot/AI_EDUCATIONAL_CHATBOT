import requests
from PIL import Image
from io import BytesIO

def generate_image(prompt):
    url = f"https://image.pollinations.ai/prompt/{requests.utils.quote(prompt)}"
    response = requests.get(url, timeout=60)
    image = Image.open(BytesIO(response.content))
    return image
