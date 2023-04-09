import time
from tkinter import Tk, messagebox
from tkinter.filedialog import askopenfilename
import pyautogui as py
import pandas as pd


def porcentagem(progress):
    # para esconder a janela principal
    Tk().withdraw() 
    while True:
        try:
    # mostra uma caixa de diálogo para o usuário selecionar um arquivo
            NomeArquivo = askopenfilename()
            # Pegando uma tebela, transformando tudo em string para poder digitar e colocar todos os itens de uma coluna em uma lista
            df = pd.DataFrame(pd.read_csv(NomeArquivo))
            ordem = df.sort_values(by='UC')
            df = ordem.applymap(str)
            lista = df['UC'].tolist()
            lista2 = df['%'].tolist()
        except:
            messagebox.showerror(title='Erro' ,message = f"Erro ao ler o arquivo")
            result = messagebox.askyesno(title="Pergunta", message="deseja tentar novamente?")
            if result:
                continue
            else:
                break
        progress["value"] = 0
        progress["maximum"] = len(lista)

        # Obtendo a quantidade de repetição com base na quantidade de itens
        QuantidadeFeita = len(lista)
        resposta = messagebox.askyesno(title='AVISO',message="Você tem certeza que deseja realizar toda a digitação desse aquivo?(Lembre-se de mudar o nome da coluna para %)")

        if resposta:
            messagebox.showinfo(message='Você tem 5 segundos para colocar no local em quer realizar a digitação')
            time.sleep(5)
            
            start_time = time.time()
            # Loop para realizar a digitação
            for a,b in zip(lista,lista2):
                py.write(a)
                py.press('tab')
                py.write(b)
                py.press('down')
                progress['value'] += 1
                progress.update_idletasks()
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