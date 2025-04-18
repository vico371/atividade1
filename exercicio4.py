import tkinter as tk
from utils import centralizar_janela, criar_botao_estilizado

# Parte 1: Formulário Simples com Grid
def criar_formulario_grid():
    janela = tk.Tk()
    janela.title("Formulário com Grid")
    janela.geometry("400x300")
    
    # Criação dos widgets
    label_nome = tk.Label(janela, text="Nome:", font=("Arial", 12))
    label_idade = tk.Label(janela, text="Idade:", font=("Arial", 12))
    label_genero = tk.Label(janela, text="Gênero:", font=("Arial", 12))
    
    entrada_nome = tk.Entry(janela, font=("Arial", 12))
    entrada_idade = tk.Entry(janela, font=("Arial", 12))
    
    var_genero = tk.StringVar(value="Masculino")
    rb_masculino = tk.Radiobutton(janela, text="Masculino", variable=var_genero, value="Masculino", font=("Arial", 12))
    rb_feminino = tk.Radiobutton(janela, text="Feminino", variable=var_genero, value="Feminino", font=("Arial", 12))
    rb_outro = tk.Radiobutton(janela, text="Outro", variable=var_genero, value="Outro", font=("Arial", 12))
    
    def enviar():
        print(f"Nome: {entrada_nome.get()}")
        print(f"Idade: {entrada_idade.get()}")
        print(f"Gênero: {var_genero.get()}")
        resultado.config(text=f"Dados enviados:\nNome: {entrada_nome.get()}\nIdade: {entrada_idade.get()}\nGênero: {var_genero.get()}")
    
    def limpar():
        entrada_nome.delete(0, tk.END)
        entrada_idade.delete(0, tk.END)
        var_genero.set("Masculino")
        resultado.config(text="")
        entrada_nome.focus()
    
    botao_enviar = criar_botao_estilizado(janela, "Enviar", enviar)
    botao_limpar = criar_botao_estilizado(janela, "Limpar", limpar)
    
    resultado = tk.Label(janela, text="", font=("Arial", 12), justify=tk.LEFT)
    
    # Posicionamento com Grid
    label_nome.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
    entrada_nome.grid(row=0, column=1, padx=10, pady=10)
    
    label_idade.grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)
    entrada_idade.grid(row=1, column=1, padx=10, pady=10)
    
    label_genero.grid(row=2, column=0, sticky=tk.W, padx=10, pady=10)
    rb_masculino.grid(row=2, column=1, sticky=tk.W, padx=10, pady=2)
    rb_feminino.grid(row=3, column=1, sticky=tk.W, padx=10, pady=2)
    rb_outro.grid(row=4, column=1, sticky=tk.W, padx=10, pady=2)
    
    botao_enviar.grid(row=5, column=0, padx=10, pady=20)
    botao_limpar.grid(row=5, column=1, padx=10, pady=20)
    
    resultado.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
    
    # Centraliza a janela
    centralizar_janela(janela)
    
    return janela

# Parte 2: Layout com Pack
def criar_layout_pack():
    janela = tk.Tk()
    janela.title("Layout com Pack")
    janela.geometry("300x250")
    
    # Frame para centralizar os botões
    frame = tk.Frame(janela)
    frame.pack(expand=True)
    
    # Criação dos botões
    botao1 = criar_botao_estilizado(frame, "Botão 1", lambda: print("Botão 1 clicado"))
    botao2 = criar_botao_estilizado(frame, "Botão 2", lambda: print("Botão 2 clicado"))
    botao3 = criar_botao_estilizado(frame, "Botão 3", lambda: print("Botão 3 clicado"))
    
    # Posicionamento com Pack
    botao1.pack(pady=10)
    botao2.pack(pady=10)
    botao3.pack(pady=10)
    
    # Centraliza a janela
    centralizar_janela(janela)
    
    return janela

# Parte 3: Posicionamento com Place
def criar_layout_place():
    janela = tk.Tk()
    janela.title("Posicionamento com Place")
    janela.geometry("400x300")
    
    # Criação dos rótulos
    label1 = tk.Label(janela, text="Rótulo Superior Esquerdo", font=("Arial", 10))
    label2 = tk.Label(janela, text="Rótulo Centro", font=("Arial", 10))
    label3 = tk.Label(janela, text="Rótulo Inferior Direito", font=("Arial", 10))
    
    # Criação dos botões
    botao1 = criar_botao_estilizado(janela, "Botão 1", lambda: print("Botão 1 clicado"))
    botao2 = criar_botao_estilizado(janela, "Botão 2", lambda: print("Botão 2 clicado"))
    botao3 = criar_botao_estilizado(janela, "Botão 3", lambda: print("Botão 3 clicado"))
    
    # Posicionamento com Place
    label1.place(x=20, y=20)
    label2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    label3.place(x=280, y=250)
    
    botao1.place(x=50, y=50)
    botao2.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
    botao3.place(x=250, y=200)
    
    # Centraliza a janela
    centralizar_janela(janela)
    
    return janela

# Função para escolher qual layout exibir
def main():
    janela_escolha = tk.Tk()
    janela_escolha.title("Escolha de Layout")
    janela_escolha.geometry("400x200")
    
    label = tk.Label(janela_escolha, text="Escolha um layout para visualizar:", font=("Arial", 14))
    label.pack(pady=20)
    
    frame_botoes = tk.Frame(janela_escolha)
    frame_botoes.pack()
    
    def abrir_grid():
        janela_escolha.destroy()
        janela = criar_formulario_grid()
        janela.mainloop()
    
    def abrir_pack():
        janela_escolha.destroy()
        janela = criar_layout_pack()
        janela.mainloop()
    
    def abrir_place():
        janela_escolha.destroy()
        janela = criar_layout_place()
        janela.mainloop()
    
    botao_grid = criar_botao_estilizado(frame_botoes, "Formulário com Grid", abrir_grid)
    botao_pack = criar_botao_estilizado(frame_botoes, "Layout com Pack", abrir_pack)
    botao_place = criar_botao_estilizado(frame_botoes, "Posicionamento com Place", abrir_place)
    
    botao_grid.pack(side=tk.LEFT, padx=10)
    botao_pack.pack(side=tk.LEFT, padx=10)
    botao_place.pack(side=tk.LEFT, padx=10)
    
    # Centraliza a janela
    centralizar_janela(janela_escolha)
    
    janela_escolha.mainloop()

if __name__ == "__main__":
    main()
