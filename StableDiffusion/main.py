import os
import torch
from diffusers import StableDiffusionImg2ImgPipeline
from diffusers import StableDiffusionPipeline
from PIL import Image
from torch import autocast


TOKEN = os.environ["AI_TOKEN"]
# StableDiffusionImg2Imgパイプラインの準備
def make_from_text(TOKEN, text, output_img = "output_img/text_output.png"):
    pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", use_auth_token=TOKEN)

    image = pipe(
            prompt = text,              # プロンプト
            height=512,                 # 生成する画像の幅
            width=512,                  # 生成する画像の高さ
            guidance_scale=7.5,         # 画像とプロンプトの類似度 (0〜20)
            num_inference_steps=50,     # 画像生成に費やすステップ数
            generator=torch.Generator().manual_seed(0), # 乱数シードジェネレータ
            )["sample"][0]
    image.save(output_img)

def make_from_text_img(TOKEN, text, img_path, output_img = "output_img/text_img_output.png"):
    
    pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
        "CompVis/stable-diffusion-v1-4",
        revision="fp16", 
        torch_dtype=torch.float16,
        use_auth_token=TOKEN)

    # 画像生成
    prompt = text
    init_image = Image.open("").convert("RGB")
    init_image = init_image.resize((512, 512))
    with autocast("cuda"):
        images = pipe(
            prompt=prompt,          # プロンプト
            init_image=init_image,  # 入力画像
            strength=0.75,          # 入力画像と出力画像と相違度 (0.0〜1.0)
            guidance_scale=7.5,     # プロンプトと出力画像の類似度　(0〜20)
            num_inference_steps=50, # 画像生成に費やすステップ数
            generator=torch.Generator().manual_seed(0), # 乱数シードジェネレータ
            )["sample"][0]
    images.save(output_img)


make_from_text(TOKEN,text = "cat of ukiyoe style")