# Importei as bibliotecas
import threading
from tkinter import *
from tkinter import ttk
import tkinter
from tkinter.ttk import Button, Progressbar, Style
from funcoes.por import porcentagem
from  ttkthemes import ThemedTk
from funcoes.rot import roteirizacao


def interface():
    window = ThemedTk(theme="equilux")
    window.geometry("341x332")
    window.resizable(False, False)
    window.configure(background = 'grey14')
    style = Style()
    window.title("Bot1A")
    window.iconbitmap('./assets/teclado.ico')

    # Definindo estilos dos botões
    style.configure("TButton", font=("Helvetica", 16), borderwidth=3, height=2, width=10)
    style.configure("Titulo.TLabel", background = 'grey', font = ("Calibre", 20))
    style.configure("Subt.TLabel",font=("Arial", 10) )

    #escolhendo qual script rodar

    container = Frame(window)
    container.configure(background = 'grey13')
    container.pack(pady=(50))
    ttk.Label(container, text="Bem Vindo(a)", style="Titulo.TLabel").pack()

    label = Frame(window)
    label.pack()
    label.configure(background="white", width=100)
    ttk.Label(label,text="O que gostaria de fazer agora?", style="Subt.TLabel").pack()

    # Criando o ttk.Progressbarwidget
    body = Frame(window)
    body.pack(pady=40)
    body.configure(background='grey14')

    container2 = Frame(body)
    container2.pack(side='right', padx=10)
    container2.configure(background='grey14')
    progress = Progressbar(container2, orient='horizontal', length=145, mode='determinate')
    progress.pack()

    container3 = Frame(body)
    container3.pack(side='left', padx=10)
    container3.configure(background='grey14')
    progress2 = Progressbar(container3, orient='horizontal', length=145, mode='determinate')
    progress2.pack()

    # window.columnconfigure(0, weight=1)
    # window.columnconfigure(1, weight=1)

    # Executando a função roteirizacao em uma thread separada
    def run_roteirizacao():
        roteirizacao(progress)
    def run_porcentagem():
        porcentagem(progress)

    Button(container2, text="roteirizações", command=lambda: threading.Thread(target=run_roteirizacao).start()).pack()
    Button(container3, text="porcetagens", command=lambda: threading.Thread(target=run_porcentagem).start()).pack()

    window.mainloop()
interface()