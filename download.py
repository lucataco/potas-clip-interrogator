# This file runs during contain
import torch
from clip_interrogator import Config, Interrogator

def download_model():
    ci = Interrogator(
        Config(   
            clip_model_name="ViT-bigG-14/laion2b_s39b_b160k",
        )
    )

if __name__ == "__main__":
    download_model()