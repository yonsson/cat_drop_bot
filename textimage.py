from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import os

def text_to_image(image_name, text):
    image = Image.open(image_name)

    font = ImageFont.truetype('Lobster.ttf', 30)
    font_color = (256, 256, 256)
    signature_pos = (50, image.height - 80)
    
    drawing = ImageDraw.Draw(image)
    drawing.text(signature_pos, text, font=font, fill=font_color, stroke_width=2, stroke_fill=(0, 0, 0))

    image_path = f"pics/pic{datetime.strftime(datetime.now(), '%H-%M-%S')}.png"
    image.save(image_path, format='PNG')

    return(image_path)

if __name__ == '__main__':
    testim = Image.open(text_to_image('cat1.jpg', 'тест'))
    testim.show()