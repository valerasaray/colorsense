import numpy as np
from PIL import Image

def image_to_rgb(image_path):
    input = Image.open(image_path)
    start_image = np.array(input)
    rgb = np.array([a for b in start_image for a in b])
    return rgb

# функция преобразования списка значений rgb в hex код
def rgb_to_hex(rgb):
    rgb = list(rgb)
    hex = []
    for i in rgb:
        now = f(int(i[0]))
        now += f(int(i[1]))
        now += f(int(i[2]))
        hex.append(f'#{now}')
    return hex

def f(x):
    y = hex(x)[2:]
    if int(y, 16) < 16:
        y = f'0{y}'
    return y