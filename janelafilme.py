import tkinter as tk
import subprocess 

def abrir_janeladecadastro():
    subprocess.Popen(["python", "janelacadastro.py"])

def sair():
    janela.destroy()

janela = tk.Tk()
janela.title ("Novalynx")
nome = tk.Label(janela, text = "Tela de cadastro de novos usuários", bg = "#a8a6b3", font =("Comic Sans MS", 20))
nome.pack(pady=5)
janela.geometry("600x600")
janela.configure(bg="#a8a6b3")



botao_cadastro = tk.Button(janela, bg="#a3a0b0", text="Fazer Cadastro/Ver usuários cadastrados", font=("Times New Roman",20), command = abrir_janeladecadastro)
botao_cadastro.pack(pady=108)

botao_fechar = tk.Button(janela, text = "Sair", command = sair, bg = "#a8a6b3", font = ("Times New Romam", 15))
botao_fechar.pack(pady=1)



janela.mainloop()