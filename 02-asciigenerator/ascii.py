import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image
from pathlib import Path
import time

rampa =  "   .~>>>O$%@"

def imagem():   
    explorer_path = Path(__file__).parent / "explorer.ico"

    janela = tk.Tk()
    janela.withdraw()
    janela.attributes("-topmost", True)
    janela.iconbitmap(explorer_path)

    caminho = filedialog.askopenfilename(
        title="Escolha uma imagem",
        initialdir="~/Downloads",
        filetypes=[("Imagens", "*.png *.jpg *.jpeg")],
    )
    janela.destroy()

    if not caminho:
        exit()

    img = Image.open(caminho)

    colunas, linhas = os.get_terminal_size()
    altura = linhas - 2
    largura = int(altura * img.width / img.height * 2)
    margem = " " * ((colunas - largura) // 2)

    try:
        img = img.resize((largura, altura))
    except ValueError:
        exit()

    img = img.convert("L")

    os.system("cls" if os.name == "nt" else "clear")

    for y in range(img.height):
        linha = margem
        for x in range(img.width):
            pixel = img.getpixel((x, y))
            linha += rampa[pixel * len(rampa) // 256]
        print(linha)

try:
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("######## Gerador de ASCII Art by rato ########")
        print("Por favor maximize o terminal para melhor visualização da imagem")
        print("Escolha uma imagem")
        time.sleep(1)

        imagem()
        input("Pressione Enter para escolher outra imagem ou Ctrl+C para sair...")

except KeyboardInterrupt:
    exit()