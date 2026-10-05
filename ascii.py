import os
from PIL import Image


rampa = "  .:+#@"

img = Image.open("lain.jpg")

colunas, linhas = os.get_terminal_size()
altura = linhas - 2
largura = int(altura * img.width / img.height * 2)
margem = " " * ((colunas - largura) // 2)

img = img.resize((largura, altura))
img = img.convert("L")

os.system("cls")

for y in range(img.height):
    linha = margem
    for x in range(img.width):
        pixel = img.getpixel((x, y))
        linha += rampa[pixel * len(rampa) // 256]
    print(linha)