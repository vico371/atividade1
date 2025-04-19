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
        preco REAL NOT NULL
    )
    ''')
    
    conn.commit()
    conn.close()

def criar_interface_validacao():
    janela = tk.Tk()
    janela.title("Cadastro de Produtos com Validação")
    janela.geometry("500x400")
    
    frame = tk.Frame(janela, padx=20, pady=20)
    frame.pack(fill=tk.BOTH, expand=True)
    
    label_titulo = tk.Label(frame, text="Cadastro de Produtos", font=("Arial", 16, "bold"))
    label_titulo.pack(pady=(0, 20))
    
    frame_campos = tk.Frame(frame)
    frame_campos.pack(fill=tk.X, pady=(0, 10))
    
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
    
    label_produtos = tk.Label(frame, text="Produtos Cadastrados:", font=("Arial", 12))
    label_produtos.pack(anchor=tk.W, pady=(10, 5))
    
    colunas = ("id", "nome", "quantidade", "preco")
    tree = ttk.Treeview(frame, columns=colunas, show="headings", height=8)
    
    tree.heading("id", text="ID")
    tree.heading("nome", text="Nome")
    tree.heading("quantidade", text="Quantidade")
    tree.heading("preco", text="Preço")
    
    tree.column("id", width=50)
    tree.column("nome", width=200)
    tree.column("quantidade", width=100)
    tree.column("preco", width=100)
    
    tree.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
    
    frame_botoes = tk.Frame(frame)
    frame_botoes.pack(fill=tk.X, pady=10)
    
    def validar_entradas():
        nome = entrada_nome.get()
        quantidade = entrada_quantidade.get()
        preco = entrada_preco.get()
        
        if not nome:
            messagebox.showerror("Erro", "O nome do produto não pode estar vazio")
            return False
        
        try:
            quantidade_int = int(quantidade)
            if quantidade_int <= 0:
                messagebox.showerror("Erro", "A quantidade deve ser um número inteiro positivo")
                return False
        except ValueError:
            messagebox.showerror("Erro", "A quantidade deve ser um número inteiro válido")
            return False
        
        try:
            preco_float = float(preco)
            if preco_float <= 0:
                messagebox.showerror("Erro", "O preço deve ser maior que zero")
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
            
            conn = sqlite3.connect('produtos.db')
            cursor = conn.cursor()
            
            cursor.execute('''
            INSERT INTO produtos (nome, quantidade, preco)
            VALUES (?, ?, ?)
            ''', (nome, quantidade, preco))
            
            conn.commit()
            conn.close()
            
            entrada_nome.delete(0, tk.END)
            entrada_quantidade.delete(0, tk.END)
            entrada_preco.delete(0, tk.END)
            entrada_nome.focus()
            
            atualizar_lista()
            
            messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
    
    def atualizar_lista():
       
        for item in tree.get_children():
            tree.delete(item)
        
        conn = sqlite3.connect('produtos.db')
        cursor = conn.cursor()
        
        cursor.execute('SELECT id, nome, quantidade, preco FROM produtos')
        produtos = cursor.fetchall()
        
        conn.close()
        
        for produto in produtos:
            tree.insert("", tk.END, values=produto)
    
    def limpar_campos():
        entrada_nome.delete(0, tk.END)
        entrada_quantidade.delete(0, tk.END)
        entrada_preco.delete(0, tk.END)
        entrada_nome.focus()
    
    botao_inserir = criar_botao_estilizado(frame_botoes, "Inserir Produto", inserir_produto)
    botao_atualizar = criar_botao_estilizado(frame_botoes, "Atualizar Lista", atualizar_lista)
    botao_limpar = criar_botao_estilizado(frame_botoes, "Limpar Campos", limpar_campos)
    
    botao_inserir.pack(side=tk.LEFT, padx=(0, 10))
    botao_atualizar.pack(side=tk.LEFT, padx=(0, 10))
    botao_limpar.pack(side=tk.LEFT)
    
    criar_banco_dados()
    
    atualizar_lista()
    
    centralizar_janela(janela)
    
    entrada_nome.focus()
    
    return janela

def criar_interface_atualizacao():
    janela = tk.Tk()
    janela.title("Atualização de Produtos")
    janela.geometry("500x450")
    
    frame = tk.Frame(janela, padx=20, pady=20)
    frame.pack(fill=tk.BOTH, expand=True)
    
    label_titulo = tk.Label(frame, text="Atualização de Produtos", font=("Arial", 16, "bold"))
    label_titulo.pack(pady=(0, 20))
    
    frame_busca = tk.Frame(frame)
    frame_busca.pack(fill=tk.X, pady=(0, 10))
    
    label_id = tk.Label(frame_busca, text="ID do Produto:", font=("Arial", 12))
    label_id.pack(side=tk.LEFT, padx=(0, 10))
    
    entrada_id = tk.Entry(frame_busca, font=("Arial", 12), width=10)
    entrada_id.pack(side=tk.LEFT, padx=(0, 10))
    
    frame_campos = tk.Frame(frame)
    frame_campos.pack(fill=tk.X, pady=(10, 10))
    
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
    
    label_produtos = tk.Label(frame, text="Produtos Cadastrados:", font=("Arial", 12))
    label_produtos.pack(anchor=tk.W, pady=(10, 5))
    
    colunas = ("id", "nome", "quantidade", "preco")
    tree = ttk.Treeview(frame, columns=colunas, show="headings", height=8)
    
    tree.heading("id", text="ID")
    tree.heading("nome", text="Nome")
    tree.heading("quantidade", text="Quantidade")
    tree.heading("preco", text="Preço")
    
    tree.column("id", width=50)
    tree.column("nome", width=200)
    tree.column("quantidade", width=100)
    tree.column("preco", width=100)
    
    tree.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
    
    frame_botoes = tk.Frame(frame)
    frame_botoes.pack(fill=tk.X, pady=10)
    
    def buscar_produto():
        id_produto = entrada_id.get()
        
        if not id_produto:
            messagebox.showerror("Erro", "Digite o ID do produto")
            return
        
        try:
            id_int = int(id_produto)
        except ValueError:
            messagebox.showerror("Erro", "O ID deve ser um número inteiro")
            return
        
        conn = sqlite3.connect('produtos.db')
        cursor = conn.cursor()
        
        cursor.execute('SELECT nome, quantidade, preco FROM produtos WHERE id = ?', (id_int,))
        produto = cursor.fetchone()
        
        conn.close()
        
        if produto:
            entrada_nome.delete(0, tk.END)
            entrada_quantidade.delete(0, tk.END)
            entrada_preco.delete(0, tk.END)
            
            entrada_nome.insert(0, produto[0])
            entrada_quantidade.insert(0, produto[1])
            entrada_preco.insert(0, produto[2])
        else:
            messagebox.showerror("Erro", f"Produto com ID {id_int} não encontrado")
    
    def validar_entradas():
        nome = entrada_nome.get()
        quantidade = entrada_quantidade.get()
        preco = entrada_preco.get()
        
        if not nome:
            messagebox.showerror("Erro", "O nome do produto não pode estar vazio")
            return False
        
        try:
            quantidade_int = int(quantidade)
            if quantidade_int <= 0:
                messagebox.showerror("Erro", "A quantidade deve ser um número inteiro positivo")
                return False
        except ValueError:
            messagebox.showerror("Erro", "A quantidade deve ser um número inteiro válido")
            return False
        
        try:
            preco_float = float(preco)
            if preco_float <= 0:
                messagebox.showerror("Erro", "O preço deve ser maior que zero")
                return False
        except ValueError:
            messagebox.showerror("Erro", "O preço deve ser um número válido")
            return False
        
        return True
    
    def atualizar_produto():
        id_produto = entrada_id.get()
        
        if not id_produto:
            messagebox.showerror("Erro", "Digite o ID do produto")
            return
        
        try:
            id_int = int(id_produto)
        except ValueError:
            messagebox.showerror("Erro", "O ID deve ser um número inteiro")
            return
        
        if validar_entradas():
            nome = entrada_nome.get()
            quantidade = int(entrada_quantidade.get())
            preco = float(entrada_preco.get())
            
            conn = sqlite3.connect('produtos.db')
            cursor = conn.cursor()
            
            cursor.execute('''
            UPDATE produtos
            SET nome = ?, quantidade = ?, preco = ?
            WHERE id = ?
            ''', (nome, quantidade, preco, id_int))
            
            if cursor.rowcount == 0:
                messagebox.showerror("Erro", f"Produto com ID {id_int} não encontrado")
                conn.close()
                return
            
            conn.commit()
            conn.close()
            
            entrada_id.delete(0, tk.END)
            entrada_nome.delete(0, tk.END)
            entrada_quantidade.delete(0, tk.END)
            entrada_preco.delete(0, tk.END)
            entrada_id.focus()
            
            atualizar_lista()
            
            messagebox.showinfo("Sucesso", "Produto atualizado com sucesso!")
    
    def atualizar_lista():

        for item in tree.get_children():
            tree.delete(item)
        
        conn = sqlite3.connect('produtos.db')
        cursor = conn.cursor()
        
        cursor.execute('SELECT id, nome, quantidade, preco FROM produtos')
        produtos = cursor.fetchall()
        
        conn.close()
        
        for produto in produtos:
            tree.insert("", tk.END, values=produto)
    
    def limpar_campos():
        entrada_id.delete(0, tk.END)
        entrada_nome.delete(0, tk.END)
        entrada_quantidade.delete(0, tk.END)
        entrada_preco.delete(0, tk.END)
        entrada_id.focus()

    botao_buscar = criar_botao_estilizado(frame_busca, "Buscar", buscar_produto)
    botao_buscar.pack(side=tk.LEFT)
    
    botao_atualizar = criar_botao_estilizado(frame_botoes, "Atualizar Produto", atualizar_produto)
    botao_listar = criar_botao_estilizado(frame_botoes, "Atualizar Lista", atualizar_lista)
    botao_limpar = criar_botao_estilizado(frame_botoes, "Limpar Campos", limpar_campos)
    
    botao_atualizar.pack(side=tk.LEFT, padx=(0, 10))
    botao_listar.pack(side=tk.LEFT, padx=(0, 10))
    botao_limpar.pack(side=tk.LEFT)
    
    criar_banco_dados()
    
    atualizar_lista()
    
    centralizar_janela(janela)
    
    entrada_id.focus()
    
    return janela

def criar_interface_exclusao():
    janela = tk.Tk()
    janela.title("Exclusão de Produtos")
    janela.geometry("500x400")
    
    frame = tk.Frame(janela, padx=20, pady=20)
    frame.pack(fill=tk.BOTH, expand=True)
    
    label_titulo = tk.Label(frame, text="Exclusão de Produtos", font=("Arial", 16, "bold"))
    label_titulo.pack(pady=(0, 20))
    
    frame_busca = tk.Frame(frame)
    frame_busca.pack(fill=tk.X, pady=(0, 10))
    
    label_id = tk.Label(frame_busca, text="ID do Produto:", font=("Arial", 12))
    label_id.pack(side=tk.LEFT, padx=(0, 10))
    
    entrada_id = tk.Entry(frame_busca, font=("Arial", 12), width=10)
    entrada_id.pack(side=tk.LEFT, padx=(0, 10))
    
    label_produtos = tk.Label(frame, text="Produtos Cadastrados:", font=("Arial", 12))
    label_produtos.pack(anchor=tk.W, pady=(10, 5))
    
    colunas = ("id", "nome", "quantidade", "preco")
    tree = ttk.Treeview(frame, columns=colunas, show="headings", height=10)
    
    tree.heading("id", text="ID")
    tree.heading("nome", text="Nome")
    tree.heading("quantidade", text="Quantidade")
    tree.heading("preco", text="Preço")
    
    tree.column("id", width=50)
    tree.column("nome", width=200)
    tree.column("quantidade", width=100)

(Content truncated due to size limit. Use line ranges to read in chunks)
