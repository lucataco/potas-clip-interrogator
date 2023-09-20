from potassium import Potassium, Request, Response

import torch
import base64
from PIL import Image
from io import BytesIO
from clip_interrogator import Config, Interrogator

app = Potassium("my_app")

# @app.init runs at startup, and loads models into the app's context
@app.init
def init():
    ci = Interrogator(
        Config(   
            clip_model_name="ViT-bigG-14/laion2b_s39b_b160k",
        )
    )
   
    context = {
        "ci": ci
    }
    return context

# @app.handler runs for every call
@app.handler("/")
def handler(context: dict, request: Request) -> Response:
    # models
    ci = context.get("ci")
    # Input parameters
    image = request.json.get("image")
    # Decode image
    img = image.encode('utf-8')
    img = BytesIO(base64.b64decode(img))
    img = Image.open(img)
    clip_txt = ci.interrogate(img)

    return Response(
        json = {"outputs": clip_txt}, 
        status=200
    )

if __name__ == "__main__":
    app.serve()