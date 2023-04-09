from cmath import e
import time
from tkinter import Tk, messagebox
from tkinter.filedialog import askopenfilename
import pandas as pd
import pyautogui as py

# 
def new_func(progress):
    progress['value'] += 1
    progress.update_idletasks()

def roteirizacao(progress):
    Tk().withdraw() 
    while True:
        try:
            NomeArquivo = askopenfilename()
            df = pd.DataFrame(pd.read_csv(NomeArquivo))
            ordem = df.sort_values(by='UC')
            df = ordem.applymap(str)
            lista = df['NCT'].tolist()
        except:
            messagebox.showerror(title='Erro' ,message = f"Erro ao ler o arquivo")
            result = messagebox.askyesno(title="Pergunta", message="deseja tentar novamente?")
            if result:
                continue
            else:
                break
        # Indicando valores maximo e minimo da barra
        progress["value"] = 0
        progress["maximum"] = len(lista)

        QuantidadeFeita = len(lista)
        resposta = messagebox.askyesno('Você tem certeza que deseja realizar toda a digitação desse aquivo?')

        if resposta:
            messagebox.showinfo('Você tem 5 segundos para colocar no local em quer realizar a digitação')
            time.sleep(5)
            
            start_time = time.time()
            for item in lista:
                py.write(item)
                py.press('enter')
                # chama a função progresso para inicar a barra de progresso
                new_func(progress)
            end_time = time.time()
            elapsed_time = end_time - start_time
            messagebox.showinfo(message =f'finalizado! Foram Realizadas:{QuantidadeFeita},preenchimentos ')
            messagebox.showinfo(message =f'Tempo de execução: {elapsed_time:.2f} segundos')
            time.sleep(5)

        else:
            exit()
        contiuar = messagebox.askyesno(message='Deseja continuar?')
        if contiuar:
            continue
        else:
            break


            