import banana_dev as client
from io import BytesIO
from PIL import Image
import base64
import time

# Create a reference to your model on Banana
my_model = client.Client(
    api_key="",
    model_key="",
    url="http://localhost:8000",
)

# read input file
with open("puppy.jpg", "rb") as f:
    image_bytes = f.read()
image_encoded = base64.b64encode(image_bytes)
image = image_encoded.decode("utf-8")

# Specify the model's input JSON
inputs = {
    "image" : image,
}

# Call your model's inference endpoint on Banana.
t1 = time.time()
result, meta = my_model.call("/", inputs)
t2 = time.time()
print("Time to run: ", t2 - t1)

print(result)
