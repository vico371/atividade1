import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from utils import centralizar_janela, criar_botao_estilizado

# Criação do banco de dados e tabela
def criar_banco_dados():
    conn = sqlite3.connect('produtos.db')
    cursor = conn.cursor()
    
    # Criação da tabela de produtos com campos adicionais
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

# Interface principal para cadastro de produtos
def criar_interface_cadastro():
    janela = tk.Tk()
    janela.title("Cadastro de Produtos")
    janela.geometry("600x550")
    
    # Frame principal
    frame = tk.Frame(janela, padx=20, pady=20)
    frame.pack(fill=tk.BOTH, expand=True)
    
    # Rótulo de título
    label_titulo = tk.Label(frame, text="Cadastro de Produtos", font=("Arial", 16, "bold"))
    label_titulo.pack(pady=(0, 20))
    
    # Frame para os campos de entrada
    frame_campos = tk.Frame(frame)
    frame_campos.pack(fill=tk.X, pady=(0, 10))
    
    # Campos de entrada
    label_nome = tk.Label(frame_campos, text="Nome:", font=("Arial", 12))
    label_nome.grid(row=0, column=0, sticky=tk.W, pady=5)
    entrada_nome = tk.Entry(frame_campos, font=("Arial", 12), width=30)
    entrada_nome.grid(row=0, column=1, sticky=tk.W, pady=5)
    
    label_quantidade = tk.Label(frame_campos, text="Quantidade:", font=("Arial", 12))
    label_quantidade.grid(row=1, column=0, sticky=tk.W, pady=5)
    entrada_quantidade = tk.Entry(frame_campos, font=("Arial", 12), width=10)
    entrada_quantidade.grid(row=1, column=1, sticky=tk.W, pady=5)
    
    label_preco = tk.Label(frame_campos, text="Preço:", font=("Arial", 12))
    label_preco.grid(row=2, column=0, sticky=tk.W, pady=5)
    entrada_preco = tk.Entry(frame_campos, font=("Arial", 12), width=10)
    entrada_preco.grid(row=2, column=1, sticky=tk.W, pady=5)
    
    # Novos campos: Categoria e Descrição
    label_categoria = tk.Label(frame_campos, text="Categoria:", font=("Arial", 12))
    label_categoria.grid(row=3, column=0, sticky=tk.W, pady=5)
    entrada_categoria = tk.Entry(frame_campos, font=("Arial", 12), width=20)
    entrada_categoria.grid(row=3, column=1, sticky=tk.W, pady=5)
    
    label_descricao = tk.Label(frame_campos, text="Descrição:", font=("Arial", 12))
    label_descricao.grid(row=4, column=0, sticky=tk.W, pady=5)
    entrada_descricao = tk.Text(frame_campos, font=("Arial", 12), width=30, height=3)
    entrada_descricao.grid(row=4, column=1, sticky=tk.W, pady=5)
    
    # Área para exibir os produtos
    label_produtos = tk.Label(frame, text="Produtos Cadastrados:", font=("Arial", 12))
    label_produtos.pack(anchor=tk.W, pady=(10, 5))
    
    # Treeview para exibir os produtos
    colunas = ("id", "nome", "quantidade", "preco", "categoria", "descricao")
    tree = ttk.Treeview(frame, columns=colunas, show="headings", height=8)
    
    tree.heading("id", text="ID")
    tree.heading("nome", text="Nome")
    tree.heading("quantidade", text="Qtd")
    tree.heading("preco", text="Preço")
    tree.heading("categoria", text="Categoria")
    tree.heading("descricao", text="Descrição")
    
    tree.column("id", width=40)
    tree.column("nome", width=150)
    tree.column("quantidade", width=50)
    tree.column("preco", width=70)
    tree.column("categoria", width=100)
    tree.column("descricao", width=150)
    
    tree.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
    
    # Frame para os botões
    frame_botoes = tk.Frame(frame)
    frame_botoes.pack(fill=tk.X, pady=10)
    
    # Funções para manipular os produtos
    def validar_entradas():
        nome = entrada_nome.get()
        quantidade = entrada_quantidade.get()
        preco = entrada_preco.get()
        
        # Validação do nome
        if not nome:
            messagebox.showerror("Erro", "O nome do produto não pode estar vazio")
            return False
        
        # Validação da quantidade
        try:
            quantidade_int = int(quantidade)
            if quantidade_int <= 0:
                messagebox.showerror("Erro", "A quantidade deve ser um número inteiro positivo")
                return False
        except ValueError:
            messagebox.showerror("Erro", "A quantidade deve ser um número inteiro válido")
            return False
        
        # Validação do preço
        try:
            preco_float = float(preco)
            if preco_float <= 0:
                messagebox.showerror("Erro", "O preço deve ser um número decimal positivo")
                return False
        except ValueError:
            messagebox.showerror("Erro", "O preço deve ser um número válido")
            return False
        
        return True
    
    def inserir_produto():
        if validar_entradas():
            nome = entrada_nome.get()
            quantidade = int(entrada_quantidade.get())
            preco = float(entrada_preco.get())
            categoria = entrada_categoria.get()
            descricao = entrada_descricao.get("1.0", tk.END).strip()
            
            # Inserir no banco de dados
            conn = sqlite3.connect('produtos.db')
            cursor = conn.cursor()
            
            cursor.execute('''
            INSERT INTO produtos (nome, quantidade, preco, categoria, descricao)
            VALUES (?, ?, ?, ?, ?)
            ''', (nome, quantidade, preco, categoria, descricao))
            
            conn.commit()
            conn.close()
            
            # Limpar campos
            entrada_nome.delete(0, tk.END)
            entrada_quantidade.delete(0, tk.END)
            entrada_preco.delete(0, tk.END)
            entrada_categoria.delete(0, tk.END)
            entrada_descricao.delete("1.0", tk.END)
            entrada_nome.focus()
            
            # Atualizar a lista de produtos
            atualizar_lista()
            
            messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
    
    def atualizar_lista():
        # Limpar a lista atual
        for item in tree.get_children():
            tree.delete(item)
        
        # Buscar produtos no banco de dados
        conn = sqlite3.connect('produtos.db')
        cursor = conn.cursor()
        
        cursor.execute('SELECT id, nome, quantidade, preco, categoria, descricao FROM produtos')
        produtos = cursor.fetchall()
        
        conn.close()
        
        # Adicionar produtos à lista
        for produto in produtos:
            # Limitar o tamanho da descrição para exibição
            descricao_curta = produto[5][:30] + "..." if len(produto[5]) > 30 else produto[5]
            valores = produto[:5] + (descricao_curta,)
            tree.insert("", tk.END, values=valores)
    
    def limpar_campos():
        entrada_nome.delete(0, tk.END)
        entrada_quantidade.delete(0, tk.END)
        entrada_preco.delete(0, tk.END)
        entrada_categoria.delete(0, tk.END)
        entrada_descricao.delete("1.0", tk.END)
        entrada_nome.focus()
    
    # Botões
    botao_inserir = criar_botao_estilizado(frame_botoes, "Inserir Produto", inserir_produto)
    botao_atualizar = criar_botao_estilizado(frame_botoes, "Atualizar Lista", atualizar_lista)
    botao_limpar = criar_botao_estilizado(frame_botoes, "Limpar Campos", limpar_campos)
    
    botao_inserir.pack(side=tk.LEFT, padx=(0, 10))
    botao_atualizar.pack(side=tk.LEFT, padx=(0, 10))
    botao_limpar.pack(side=tk.LEFT)
    
    # Criar banco de dados se não existir
    criar_banco_dados()
    
    # Atualizar a lista de produtos
    atualizar_lista()
    
    # Centraliza a janela
    centralizar_janela(janela)
    
    # Foco no primeiro campo
    entrada_nome.focus()
    
    return janela

# Função principal
def main():
    janela = criar_interface_cadastro()
    janela.mainloop()

if __name__ == "__main__":
    main()
