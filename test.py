import threading
import time
import tkinter as tk
from tkinter import simpledialog
from tkinter import ttk
from ttkthemes import ThemedTk

from funcoes.por import porcentagem

class ProgressDialog(simpledialog.Dialog):
    def __init__(self, parent, title, message):
        self.message = message
        super().__init__(parent, title)

    def body(self, frame):
        tk.Label(frame, text=self.message).pack()
        self.progress = ttk.Progressbar(frame, orient='horizontal', length=200, mode='determinate')
        self.progress.pack()
        return frame

    def set_progress(self, value):
        self.progress['value'] = value
        self.progress.update_idletasks()

def roteirizacao():
    # Criando a caixa de diálogo com a barra de progresso
    dialog = ProgressDialog(window, "Progress", "Processing...")
    # Simulando uma tarefa de longa duração
    for i in range(100):
        dialog.set_progress(i)
        time.sleep(0.1)

def interface():
    global window
    window = ThemedTk(theme="equilux")
    window.geometry("800x600")
    window.configure(background = 'grey14')
    style = ttk.Style()
    window.title("Bot1A")
    window.iconbitmap()

    # Definindo estilos dos botões
    style.configure("TButton", font=("Helvetica", 16), borderwidth=3, height=2, width=10)
    style.configure("Titulo.TLabel", background = 'grey', font = ("Calibre", 20))
    background_image = tk.PhotoImage()

    #escolhendo qual script rodar

    container = tk.Frame(window)
    container.pack()
    ttk.Label(container, text="Bem Vindo(a)", style="Titulo.TLabel").pack()

    # Executando a função roteirizacao em uma thread separada
    def run_roteirizacao():
        roteirizacao()

    ttk.Button(window, text="roteirizações", command=lambda: threading.Thread(target=run_roteirizacao).start()).pack()
    ttk.Button(window, text="porcetagens", command=porcentagem).pack()

    window.mainloop()

interface()