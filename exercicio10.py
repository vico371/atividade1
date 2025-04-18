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

# Interface principal para listagem e consulta de produtos
def criar_interface_listagem():
    janela = tk.Tk()
    janela.title("Listagens e Consulta de Dados")
    janela.geometry("700x550")
    
    # Frame principal
    frame = tk.Frame(janela, padx=20, pady=20)
    frame.pack(fill=tk.BOTH, expand=True)
    
    # Rótulo de título
    label_titulo = tk.Label(frame, text="Listagens e Consulta de Produtos", font=("Arial", 16, "bold"))
    label_titulo.pack(pady=(0, 20))
    
    # Frame para pesquisa
    frame_pesquisa = tk.Frame(frame)
    frame_pesquisa.pack(fill=tk.X, pady=(0, 10))
    
    # Campo de pesquisa
    label_pesquisa = tk.Label(frame_pesquisa, text="Pesquisar:", font=("Arial", 12))
    label_pesquisa.pack(side=tk.LEFT, padx=(0, 10))
    
    entrada_pesquisa = tk.Entry(frame_pesquisa, font=("Arial", 12), width=20)
    entrada_pesquisa.pack(side=tk.LEFT, padx=(0, 10))
    
    # Combobox para filtrar por categoria
    label_categoria = tk.Label(frame_pesquisa, text="Categoria:", font=("Arial", 12))
    label_categoria.pack(side=tk.LEFT, padx=(10, 10))
    
    combo_categoria = ttk.Combobox(frame_pesquisa, font=("Arial", 12), width=15)
    combo_categoria.pack(side=tk.LEFT, padx=(0, 10))
    
    # Área para exibir os produtos
    frame_produtos = tk.Frame(frame)
    frame_produtos.pack(fill=tk.BOTH, expand=True, pady=(10, 10))
    
    # Treeview para exibir os produtos
    colunas = ("id", "nome", "quantidade", "preco", "categoria")
    tree = ttk.Treeview(frame_produtos, columns=colunas, show="headings", height=10)
    
    tree.heading("id", text="ID")
    tree.heading("nome", text="Nome")
    tree.heading("quantidade", text="Qtd")
    tree.heading("preco", text="Preço")
    tree.heading("categoria", text="Categoria")
    
    tree.column("id", width=40)
    tree.column("nome", width=200)
    tree.column("quantidade", width=60)
    tree.column("preco", width=80)
    tree.column("categoria", width=120)
    
    # Configuração de cores para produtos com quantidade baixa
    tree.tag_configure('baixo_estoque', background='#ffcccc')
    
    # Adicionar scrollbar
    scrollbar = ttk.Scrollbar(frame_produtos, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    # Frame para paginação
    frame_paginacao = tk.Frame(frame)
    frame_paginacao.pack(fill=tk.X, pady=(10, 10))
    
    # Variáveis para paginação
    pagina_atual = tk.IntVar(value=1)
    total_paginas = tk.IntVar(value=1)
    produtos_por_pagina = 10
    
    # Rótulos para paginação
    label_pagina = tk.Label(frame_paginacao, text="Página:", font=("Arial", 12))
    label_pagina.pack(side=tk.LEFT, padx=(0, 5))
    
    label_pagina_atual = tk.Label(frame_paginacao, textvariable=pagina_atual, font=("Arial", 12))
    label_pagina_atual.pack(side=tk.LEFT, padx=(0, 5))
    
    label_de = tk.Label(frame_paginacao, text="de", font=("Arial", 12))
    label_de.pack(side=tk.LEFT, padx=(0, 5))
    
    label_total_paginas = tk.Label(frame_paginacao, textvariable=total_paginas, font=("Arial", 12))
    label_total_paginas.pack(side=tk.LEFT, padx=(0, 10))
    
    # Frame para os botões
    frame_botoes = tk.Frame(frame)
    frame_botoes.pack(fill=tk.X, pady=10)
    
    # Funções para manipular os produtos
    def carregar_categorias():
        # Buscar categorias no banco de dados
        conn = sqlite3.connect('produtos.db')
        cursor = conn.cursor()
        
        cursor.execute('SELECT DISTINCT categoria FROM produtos WHERE categoria IS NOT NULL AND categoria != ""')
        categorias = cursor.fetchall()
        
        conn.close()
        
        # Adicionar categorias ao combobox
        combo_categoria.set("")
        combo_categoria['values'] = ["Todas"] + [cat[0] for cat in categorias]
        combo_categoria.current(0)
    
    def calcular_total_paginas(filtro="", categoria=""):
        # Calcular o total de páginas com base no filtro
        conn = sqlite3.connect('produtos.db')
        cursor = conn.cursor()
        
        if categoria and categoria != "Todas":
            if filtro:
                cursor.execute('''
                SELECT COUNT(*) FROM produtos 
                WHERE (nome LIKE ? OR descricao LIKE ?) AND categoria = ?
                ''', (f'%{filtro}%', f'%{filtro}%', categoria))
            else:
                cursor.execute('SELECT COUNT(*) FROM produtos WHERE categoria = ?', (categoria,))
        else:
            if filtro:
                cursor.execute('''
                SELECT COUNT(*) FROM produtos 
                WHERE nome LIKE ? OR descricao LIKE ?
                ''', (f'%{filtro}%', f'%{filtro}%'))
            else:
                cursor.execute('SELECT COUNT(*) FROM produtos')
        
        total = cursor.fetchone()[0]
        conn.close()
        
        # Calcular total de páginas
        total_pag = (total + produtos_por_pagina - 1) // produtos_por_pagina
        if total_pag < 1:
            total_pag = 1
        
        total_paginas.set(total_pag)
        
        # Ajustar página atual se necessário
        if pagina_atual.get() > total_pag:
            pagina_atual.set(total_pag)
    
    def carregar_produtos(pagina=1, filtro="", categoria=""):
        # Limpar a lista atual
        for item in tree.get_children():
            tree.delete(item)
        
        # Calcular offset para paginação
        offset = (pagina - 1) * produtos_por_pagina
        
        # Buscar produtos no banco de dados
        conn = sqlite3.connect('produtos.db')
        cursor = conn.cursor()
        
        if categoria and categoria != "Todas":
            if filtro:
                cursor.execute('''
                SELECT id, nome, quantidade, preco, categoria FROM produtos 
                WHERE (nome LIKE ? OR descricao LIKE ?) AND categoria = ?
                ORDER BY id DESC LIMIT ? OFFSET ?
                ''', (f'%{filtro}%', f'%{filtro}%', categoria, produtos_por_pagina, offset))
            else:
                cursor.execute('''
                SELECT id, nome, quantidade, preco, categoria FROM produtos 
                WHERE categoria = ?
                ORDER BY id DESC LIMIT ? OFFSET ?
                ''', (categoria, produtos_por_pagina, offset))
        else:
            if filtro:
                cursor.execute('''
                SELECT id, nome, quantidade, preco, categoria FROM produtos 
                WHERE nome LIKE ? OR descricao LIKE ?
                ORDER BY id DESC LIMIT ? OFFSET ?
                ''', (f'%{filtro}%', f'%{filtro}%', produtos_por_pagina, offset))
            else:
                cursor.execute('''
                SELECT id, nome, quantidade, preco, categoria FROM produtos 
                ORDER BY id DESC LIMIT ? OFFSET ?
                ''', (produtos_por_pagina, offset))
        
        produtos = cursor.fetchall()
        
        conn.close()
        
        # Adicionar produtos à lista
        for produto in produtos:
            # Verificar se a quantidade está abaixo de 5
            if produto[2] < 5:
                tree.insert("", tk.END, values=produto, tags=('baixo_estoque',))
            else:
                tree.insert("", tk.END, values=produto)
    
    def pesquisar():
        filtro = entrada_pesquisa.get()
        categoria = combo_categoria.get()
        
        # Resetar para a primeira página
        pagina_atual.set(1)
        
        # Calcular total de páginas
        calcular_total_paginas(filtro, categoria)
        
        # Carregar produtos
        carregar_produtos(1, filtro, categoria)
    
    def pagina_anterior():
        if pagina_atual.get() > 1:
            nova_pagina = pagina_atual.get() - 1
            pagina_atual.set(nova_pagina)
            carregar_produtos(nova_pagina, entrada_pesquisa.get(), combo_categoria.get())
    
    def proxima_pagina():
        if pagina_atual.get() < total_paginas.get():
            nova_pagina = pagina_atual.get() + 1
            pagina_atual.set(nova_pagina)
            carregar_produtos(nova_pagina, entrada_pesquisa.get(), combo_categoria.get())
    
    # Botão de pesquisa
    botao_pesquisar = criar_botao_estilizado(frame_pesquisa, "Pesquisar", pesquisar)
    botao_pesquisar.pack(side=tk.LEFT)
    
    # Botões de paginação
    botao_anterior = criar_botao_estilizado(frame_paginacao, "Anterior", pagina_anterior)
    botao_proximo = criar_botao_estilizado(frame_paginacao, "Próximo", proxima_pagina)
    
    botao_anterior.pack(side=tk.LEFT, padx=(10, 5))
    botao_proximo.pack(side=tk.LEFT, padx=(5, 0))
    
    # Botão para atualizar
    botao_atualizar = criar_botao_estilizado(frame_botoes, "Atualizar Lista", lambda: carregar_produtos(pagina_atual.get(), entrada_pesquisa.get(), combo_categoria.get()))
    botao_atualizar.pack(side=tk.LEFT)
    
    # Criar banco de dados se não existir
    criar_banco_dados()
    
    # Carregar categorias
    carregar_categorias()
    
    # Calcular total de páginas
    calcular_total_paginas()
    
    # Carregar produtos iniciais
    carregar_produtos()
    
    # Centraliza a janela
    centralizar_janela(janela)
    
    # Foco no campo de pesquisa
    entrada_pesquisa.focus()
    
    return janela

# Função principal
def main():
    janela = criar_interface_listagem()
    janela.mainloop()

if __name__ == "__main__":
    main()
