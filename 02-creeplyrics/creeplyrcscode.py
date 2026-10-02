#código simples, mas antigo e todo fudido que roda Creep do Radiohead e mostra a letra


import sys
import os
import tkinter as tk
import pygame
from PIL import Image, ImageTk
from pathlib import Path



# Caminhos da música e do fundo
try:
    musica_path = Path(sys._MEIPASS) / "Radiohead - Creep.mp3"
    fundo_path = Path(sys._MEIPASS) / "bocchi.jpg"
    icone_path = Path(sys._MEIPASS) / "engrenagem.png"
except AttributeError:
    musica_path = Path(__file__).parent / "Radiohead - Creep.mp3"
    fundo_path = Path(__file__).parent / "bocchi.jpg"
    icone_path = Path(__file__).parent / "engrenagem.png"


# Inicializar Pygame e tocar música
pygame.mixer.init()
pygame.mixer.music.load(musica_path)
pygame.mixer.music.play()


# Criar janela Tkinter
janela = tk.Tk()
janela.geometry("500x400")
janela.resizable(False, False)
janela.title("Creep - Radiohead")
icone = tk.PhotoImage(file=icone_path)
janela.iconphoto(True, icone)
janela.eval('tk::PlaceWindow . center')


# Carregar imagem de fundo no tamanho da janela
img_base = Image.open(fundo_path).resize((500, 400))
foto = ImageTk.PhotoImage(img_base)


# Fundo
label_fundo = tk.Label(janela, image=foto)
label_fundo.place(x=0, y=0, relwidth=1, relheight=1)


# Letra
label = tk.Label(
    janela,
    font=("Arial", 25, "italic"),
    fg="white",
    bg="black"
)
label.place(relx=0.5, rely=0.5, anchor="center")


# Mudar frase
def mudar(frase):
    label.config(text=frase)


# Tempos da música
letra = [
    (0, "♫"),
    (18600, "When you were here before"),
    (23500, "Couldn't look you in the eye"),
    (29000, "You're just like an angel"),
    (34000, "Your skin makes me cry"),
    (39000, "You float like a feather"),
    (44000, "In a beautiful world"),
    (49500, "I wish I was special"),
    (54500, "You're so fucking special"),
    (60000, "But I'm a creep"),
    (65000, "I'm a weirdo"),
    (70000, "What the hell am I doing here?"),
    (76000, "I don't belong here"),
    (81000, "I don't care if it hurts"),
    (86000, "I want to have control"),
    (91500, "I want a perfect body"),
    (96500, "I want a perfect soul"),
    (102000, "I want you to notice"),
    (107000, "When I'm not around"),
    (112000, "You're so fucking special"),
    (114500, "I wish I was special"),
    (123000, "But I'm a creep"),
    (128000, "I'm a weirdo"),
    (133000, "What the hell am I doing here?"),
    (139000, "I don't belong here"),
    (145000, "She's running out the door"),
    (155000, "She's running out"),
    (160500, "She run, run, run, run"),
    (164500, "Run"),
    (185000, "Whatever makes you happy"),
    (190500, "Whatever you want"),
    (195500, "You're so fucking special"),
    (200500, "I wish I was special"),
    (205500, "But I'm a creep"),
    (211000, "I'm a weirdo"),
    (216000, "What the hell am I doing here?"),
    (221500, "I don't belong here")
]


# Agendar letras
for tempo, frase in letra:
    janela.after(tempo, mudar, frase)


# Executar
janela.mainloop()
