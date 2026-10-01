#autoclicker simples em python, feio, mas completamente funcional
#um dos códigos mais limpos que eu já fiz


import sys
import tkinter as tk
import time
import keyboard
import threading
import pydirectinput
import winsound
from PIL import Image, ImageTk
from pathlib import Path
from win11toast import toast


###PATHS###

try:
    fundo_path = Path(sys._MEIPASS) / "gamingnigga.jpg"
    ico_path = Path(sys._MEIPASS) / "mouseico.ico"

except AttributeError:
    fundo_path = Path(__file__).parent / "gamingnigga.jpg"
    ico_path = Path(__file__).parent / "mouseico.ico"


###VARIÁVEIS###

velocidade = 0.1
ativo = threading.Event()
pydirectinput.PAUSE = 0


###TKINTER E ESTRUTURA###

janela = tk.Tk()
janela.geometry("500x400")
janela.resizable(False, False)
janela.title("Simple Autoclicker by rato")
janela.eval('tk::PlaceWindow . center')
janela.protocol("WM_DELETE_WINDOW", janela.destroy)
janela.iconbitmap(ico_path)


img = Image.open(fundo_path).resize((500, 400))
imagem_fundo = ImageTk.PhotoImage(img)

label_fundo = tk.Label(janela, image=imagem_fundo)
label_fundo.place(x=0, y=0, relwidth=1, relheight=1)
label_fundo.lower()


def definir_velocidade():
    global velocidade

    if entrada_segundos.get() == "":
        entrada_segundos.insert(0, "0")
    if entrada_milissegundos.get() == "":
        entrada_milissegundos.insert(0, "0")

    segundos = float(entrada_segundos.get())
    milissegundos = float(entrada_milissegundos.get())
    velocidade = segundos + (milissegundos / 1000)
    marcador.config(text=f"Velocidade: {velocidade}s")


def apenas_numeros(valor):
    if valor.isdigit() or valor == "":
        return True
    else: 
        return False


validacao = janela.register(apenas_numeros)


entrada_segundos = tk.Entry(
    janela,
    font=("Arial", 14), 
    bg="#272727",
    fg="white", 
    insertbackground="white",
    validate="key",
    validatecommand=(validacao, "%P"),
    bd=0
)
entrada_segundos.place(x=125, y=160, width=100, height=30)
entrada_segundos.insert(0, "0")

entrada_milissegundos = tk.Entry(
    janela,
    font=("Arial", 14), 
    bg="#272727",
    fg="white", 
    insertbackground="white",
    validate="key",
    validatecommand=(validacao, "%P"),
    bd=0
)
entrada_milissegundos.place(x=275, y=160, width=100, height=30)
entrada_milissegundos.insert(0, "100")

botao = tk.Button(
    janela, 
    text="Aplicar", 
    command=definir_velocidade, 
    font=("Arial", 12), 
    bg="#272727", 
    fg="white",
    bd=0,
)
botao.place(x=200, y=200, width=100, height=35)

vel_texto = tk.Label(
    janela, 
    text="segundos:", 
    font=("Arial", 12), 
    bg="#272727", 
    fg="white"
)
vel_texto.place(x=100, y=130)

vel_texto_ms = tk.Label(
    janela, 
    text="milissegundos:", 
    font=("Arial", 12), 
    bg="#272727", 
    fg="white"
)
vel_texto_ms.place(x=250, y=130)

marcador = tk.Label(
    janela,
    text=f"Velocidade: {velocidade}s", 
    font=("Arial", 12), 
    bg="#272727", 
    fg="white"
)
marcador.place(x=30, y=350)

tuto = tk.Label(
    janela, 
    text="F7 para ligar/desligar, ENTER para aplicar a velocidade.", 
    font=("Arial", 10), 
    bg="#272727", 
    fg="white"
)
tuto.place(x=80, y=80)


###SEILA###

def ligar():
    if ativo.is_set():
        return
    ativo.set()
    winsound.MessageBeep()
    threading.Thread(
        target=toast,
        args=("Autoclicker", "Ligado"), 
        kwargs={"tag": "status", 
        "app_id": "Simple Autoclicker",
        "icon": str(ico_path),
        "audio": {"silent": "true"}}, daemon=True).start()


def desligar():
    if not ativo.is_set():
        return
    ativo.clear()
    winsound.MessageBeep()
    threading.Thread(
        target=toast, 
        args=("Autoclicker", "Desligado"), 
        kwargs={"tag": "status", 
        "app_id": "Simple Autoclicker", 
        "icon": str(ico_path),
        "audio": {"silent": "true"}}, daemon=True).start()

def alternar():
    if ativo.is_set():
        desligar()
    else:
        ligar()

def clicking():
    while True:
        ativo.wait()
        pydirectinput.click()
        time.sleep(velocidade)


keyboard.add_hotkey("f7", alternar)
keyboard.add_hotkey("enter", definir_velocidade)

thread_click = threading.Thread(target=clicking, daemon=True)
thread_click.start()


janela.mainloop()