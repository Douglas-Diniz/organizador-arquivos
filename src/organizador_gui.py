import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# Dicionário com extensões e categorias
tipos_arquivos = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Vídeos": [".mp4", ".mkv", ".mov"],
    "Áudios": [".mp3", ".wav"],
    "Compactados": [".zip", ".rar"],
    "Outros": []
}

def organizar_pasta(pasta_origem):
    if not os.path.exists(pasta_origem):
        messagebox.showerror("Erro", "A pasta selecionada não existe!")
        return

    # Criar as pastas de destino (se não existirem)
    for categoria in tipos_arquivos.keys():
        pasta_destino = os.path.join(pasta_origem, categoria)
        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)

    # Organizar arquivos
    for arquivo in os.listdir(pasta_origem):
        caminho_arquivo = os.path.join(pasta_origem, arquivo)

        if os.path.isfile(caminho_arquivo):
            movido = False
            for categoria, extensoes in tipos_arquivos.items():
                if any(arquivo.lower().endswith(ext) for ext in extensoes):
                    shutil.move(caminho_arquivo, os.path.join(pasta_origem, categoria, arquivo))
                    movido = True
                    break
            if not movido:  # Se não bateu com nenhuma extensão, vai para "Outros"
                shutil.move(caminho_arquivo, os.path.join(pasta_origem, "Outros", arquivo))

    messagebox.showinfo("Concluído", "Arquivos organizados com sucesso!")

def selecionar_pasta():
    pasta = filedialog.askdirectory()
    if pasta:
        organizar_pasta(pasta)

# Interface Tkinter
janela = tk.Tk()
janela.title("Organizador de Arquivos")
janela.geometry("300x150")

label = tk.Label(janela, text="Selecione uma pasta para organizar:")
label.pack(pady=10)

botao = tk.Button(janela, text="Selecionar Pasta", command=selecionar_pasta)
botao.pack(pady=20)

janela.mainloop()