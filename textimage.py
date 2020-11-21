from PIL import Image, ImageDraw, ImageFont

image = Image.open('cat4.jpg')

font = ImageFont.truetype('Lobster.ttf', 30)  # Загрузка шрифта и установка размера
font_color = (256, 256, 256)  # Цвет шрифта
signature_pos = (50, image.height - 80)  # Координаты первой буквы подписи на загруженной картинке
print(signature_pos)
drawing = ImageDraw.Draw(image)
drawing.text(signature_pos, 'мы всех уронили ыпывап ыва пвыа ', font=font, fill=font_color, stroke_width=2, stroke_fill=(0, 0, 0))

image.show()