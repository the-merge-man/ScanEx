from pdf2image import convert_from_path
from PIL import Image
import os

def pdf_to_images(path: str) -> list[Image.Image]:
    return convert_from_path(path)

def save_images(img_lst: list[Image.Image], output_dir: str) -> list[str]:
    path_list = []
    os.makedirs(output_dir, exist_ok=True)
    for index, img in enumerate(img_lst):
        filename = f"page_{index}.png"
        filepath = os.path.join(output_dir, filename)
        path_list.append(filepath)
        img.save(filepath)
    return path_list