import tkinter as tk #apelido

#para ser uma lista
lista = []

#criar uma função para add os intens na lista
def adicionar_item():
    #vai receber o que escreve na caixinha
    item = entrada.get()
    if item:
        lista.append(item)
        entrada.delete(0, tk.END)#limpar o campo que escreve de add os itens 
        atualizar_lista()

#comando para atualizar a lista
def atualizar_lista():
  texto_lista = "\n".join(f"{i}-{item}" for i, item in enumerate(lista)) if lista else "nenhum item  ser adicionado" 
  rlista.config(text=texto_lista) 

janela = tk.Tk()

janela.title("Tela de cadastro de novos usuários")
janela.geometry("500x500")

#mudar a cor da janela 
janela.configure(bg="#c6b3ff")


ritem = tk.Label(janela, bg="#c6b3ff", text="Digite seu nome inteiro: ", font=("Times New Roman",20))
ritem.pack(pady=6) #onde escrevemos 
entrada = tk.Entry(janela, bg="#8770cf", width=20, font=("Times New Roman",14))
entrada.pack(pady=12)             

ritem = tk.Label(janela, bg="#c6b3ff", text="Digite seu email: ", font=("Times New Roman",20))
ritem.pack(pady=6) #onde escrevemos 
entrada = tk.Entry(janela, bg="#8770cf", width=20, font=("Times New Roman",14))
entrada.pack(pady=12)             
                        
ritem = tk.Label(janela, bg="#c6b3ff", text="Digite seu telefone: ", font=("Times New Roman",20))
ritem.pack(pady=6) #onde escrevemos 
entrada = tk.Entry(janela, bg="#8770cf", width=20, font=("Times New Roman",14))
entrada.pack(pady=12)      
                                     

botao_adicionar = tk.Button(janela, bg="#a99ad6", text="Adicionar item:", font=("Times New Roman",14), command = adicionar_item)
botao_adicionar.pack(pady=6, anchor="e", padx=10)


                                    
rlista = tk.Label(janela, bg="#896dde", text="", width=50, height=10, anchor="nw" , justify="left", font=("Times New Roman", 14), relief="solid") 
rlista.pack(pady=10)

janela.mainloop()
