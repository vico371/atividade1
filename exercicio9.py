import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from utils import centralizar_janela, criar_botao_estilizado

def criar_banco_dados():
    conn = sqlite3.connect('produtos.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        preco REAL NOT NULL,
        categoria TEXT,
        descricao TEXT
    )
    ''')
    
    conn.commit()
    conn.close()

def criar_interface_cadastro():
    janela = tk.Tk()
    janela.title("Cadastro de Produtos")
    
    janela.geometry("800x650") 
    janela.minsize(700, 600)   
    janela.grid_rowconfigure(0, weight=1)
    janela.grid_columnconfigure(0, weight=1)
    
    frame_principal = tk.Frame(janela, padx=20, pady=20)
    frame_principal.pack(fill=tk.BOTH, expand=True)
    
    frame_campos = tk.LabelFrame(frame_principal, text="Dados do Produto", padx=10, pady=10)
    frame_campos.pack(fill=tk.X, pady=(0, 10))
    
    frame_campos.grid_columnconfigure(1, weight=1)
    
    campos = [
        ("Nome:", tk.Entry, {"width": 40}),
        ("Quantidade:", tk.Entry, {"width": 10}),
        ("Preço:", tk.Entry, {"width": 10}),
        ("Categoria:", tk.Entry, {"width": 20}),
        ("Descrição:", tk.Text, {"width": 40, "height": 3})
    ]
    
    entradas = {}
    for i, (label_text, widget, config) in enumerate(campos):
        tk.Label(frame_campos, text=label_text, font=("Arial", 11)).grid(row=i, column=0, sticky=tk.W, pady=5)
        if widget == tk.Text:
            entrada = widget(frame_campos, font=("Arial", 11), **config)
            entrada.grid(row=i, column=1, sticky=tk.W+tk.E, pady=5)
        else:
            entrada = widget(frame_campos, font=("Arial", 11), **config)
            entrada.grid(row=i, column=1, sticky=tk.W, pady=5)
        entradas[label_text.lower().replace(":", "")] = entrada
    
    frame_lista = tk.LabelFrame(frame_principal, text="Produtos Cadastrados", padx=10, pady=10)
    frame_lista.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
    
    colunas = ("id", "nome", "quantidade", "preco", "categoria", "descricao")
    tree = ttk.Treeview(frame_lista, columns=colunas, show="headings", height=10)
    
    tree.heading("id", text="ID")
    tree.heading("nome", text="Nome")
    tree.heading("quantidade", text="Qtd")
    tree.heading("preco", text="Preço")
    tree.heading("categoria", text="Categoria")
    tree.heading("descricao", text="Descrição")
    
    tree.column("id", width=50, anchor=tk.CENTER)
    tree.column("nome", width=150)
    tree.column("quantidade", width=60, anchor=tk.CENTER)
    tree.column("preco", width=80, anchor=tk.CENTER)
    tree.column("categoria", width=120)
    tree.column("descricao", width=200)
    
    scrollbar = ttk.Scrollbar(frame_lista, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    frame_botoes = tk.Frame(frame_principal)
    frame_botoes.pack(fill=tk.X, pady=(10, 0))
    
    def validar_entradas():
  
        pass
    
    def inserir_produto():
   
        pass
    
    def atualizar_lista():
      
        pass
    
    def limpar_campos():
       
        pass
    
    botoes = [
        ("Inserir Produto", inserir_produto),
        ("Atualizar Lista", atualizar_lista),
        ("Limpar Campos", limpar_campos)
    ]
    
    for i, (texto, comando) in enumerate(botoes):
        botao = criar_botao_estilizado(frame_botoes, texto, comando)
        botao.pack(side=tk.LEFT, padx=(0, 10) if i < len(botoes)-1 else (0, 0))
    
    criar_banco_dados()
    atualizar_lista()
    centralizar_janela(janela)
    entradas["nome"].focus()
    
    return janela

def main():
    janela = criar_interface_cadastro()
    janela.mainloop()

if __name__ == "__main__":
    main()