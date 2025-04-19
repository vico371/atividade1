import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sqlite3
import csv
import datetime
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

def criar_interface_relatorios():
    janela = tk.Tk()
    janela.title("Relatórios e Exportação de Dados")
    janela.geometry("700x550")
    
    frame = tk.Frame(janela, padx=20, pady=20)
    frame.pack(fill=tk.BOTH, expand=True)
    
    label_titulo = tk.Label(frame, text="Relatórios e Exportação de Dados", font=("Arial", 16, "bold"))
    label_titulo.pack(pady=(0, 20))
    
    frame_filtros = tk.Frame(frame)
    frame_filtros.pack(fill=tk.X, pady=(0, 10))
    
    label_categoria = tk.Label(frame_filtros, text="Categoria:", font=("Arial", 12))
    label_categoria.pack(side=tk.LEFT, padx=(0, 10))
    
    combo_categoria = ttk.Combobox(frame_filtros, font=("Arial", 12), width=15)
    combo_categoria.pack(side=tk.LEFT, padx=(0, 10))
    
    label_produtos = tk.Label(frame, text="Produtos para Exportação:", font=("Arial", 12))
    label_produtos.pack(anchor=tk.W, pady=(10, 5))
    
    colunas = ("id", "nome", "quantidade", "preco", "categoria", "descricao")
    tree = ttk.Treeview(frame, columns=colunas, show="headings", height=10)
    
    tree.heading("id", text="ID")
    tree.heading("nome", text="Nome")
    tree.heading("quantidade", text="Qtd")
    tree.heading("preco", text="Preço")
    tree.heading("categoria", text="Categoria")
    tree.heading("descricao", text="Descrição")
    
    tree.column("id", width=40)
    tree.column("nome", width=150)
    tree.column("quantidade", width=60)
    tree.column("preco", width=80)
    tree.column("categoria", width=100)
    tree.column("descricao", width=200)
    
    scrollbar_y = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
    scrollbar_x = ttk.Scrollbar(frame, orient=tk.HORIZONTAL, command=tree.xview)
    tree.configure(yscroll=scrollbar_y.set, xscroll=scrollbar_x.set)
    
    tree.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
    scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
    scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
    
    frame_botoes = tk.Frame(frame)
    frame_botoes.pack(fill=tk.X, pady=10)
    
    def carregar_categorias():
      
        conn = sqlite3.connect('produtos.db')
        cursor = conn.cursor()
        
        cursor.execute('SELECT DISTINCT categoria FROM produtos WHERE categoria IS NOT NULL AND categoria != ""')
        categorias = cursor.fetchall()
        
        conn.close()
        
        combo_categoria.set("")
        combo_categoria['values'] = ["Todas"] + [cat[0] for cat in categorias]
        combo_categoria.current(0)
    
    def filtrar_produtos():
        for item in tree.get_children():
            tree.delete(item)
        
        conn = sqlite3.connect('produtos.db')
        cursor = conn.cursor()
        
        categoria = combo_categoria.get()
        
        if categoria and categoria != "Todas":
            cursor.execute('''
            SELECT id, nome, quantidade, preco, categoria, descricao FROM produtos 
            WHERE categoria = ?
            ORDER BY categoria, nome
            ''', (categoria,))
        else:
            cursor.execute('''
            SELECT id, nome, quantidade, preco, categoria, descricao FROM produtos 
            ORDER BY categoria, nome
            ''')
        
        produtos = cursor.fetchall()
        
        conn.close()
        
        for produto in produtos:
            descricao_curta = produto[5][:30] + "..." if produto[5] and len(produto[5]) > 30 else produto[5]
            valores = produto[:5] + (descricao_curta,)
            tree.insert("", tk.END, values=valores)
    
    def exportar_dados():
        if not tree.get_children():
            messagebox.showwarning("Aviso", "Não há produtos para exportar.")
            return
        
        agora = datetime.datetime.now()
        data_hora = agora.strftime("%Y-%m-%d_%H-%M")
        
        categoria = combo_categoria.get()
        if categoria and categoria != "Todas":
            nome_arquivo = f"relatorio_{categoria}_{data_hora}.csv"
        else:
            nome_arquivo = f"relatorio_{data_hora}.csv"
        
        arquivo = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("Arquivos CSV", "*.csv"), ("Todos os Arquivos", "*.*")],
            title="Exportar Relatório",
            initialfile=nome_arquivo
        )
        
        if not arquivo:
            return
        
        try:
            conn = sqlite3.connect('produtos.db')
            cursor = conn.cursor()
            
            if categoria and categoria != "Todas":
                cursor.execute('''
                SELECT id, nome, quantidade, preco, categoria, descricao FROM produtos 
                WHERE categoria = ?
                ORDER BY categoria, nome
                ''', (categoria,))
            else:
                cursor.execute('''
                SELECT id, nome, quantidade, preco, categoria, descricao FROM produtos 
                ORDER BY categoria, nome
                ''')
            
            produtos = cursor.fetchall()
            
            conn.close()
            
            with open(arquivo, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(["ID", "Nome", "Quantidade", "Preço", "Categoria", "Descrição"])
              
                for produto in produtos:
                    writer.writerow(produto)
            
            messagebox.showinfo("Sucesso", f"Relatório exportado com sucesso para:\n{arquivo}")
        
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao exportar relatório: {str(e)}")
    
    def exibir_relatorio():
        filtrar_produtos()
        messagebox.showinfo("Relatório", "Relatório gerado e exibido na tabela.")
    
    botao_filtrar = criar_botao_estilizado(frame_filtros, "Filtrar", filtrar_produtos)
    botao_filtrar.pack(side=tk.LEFT)
    
    botao_exibir = criar_botao_estilizado(frame_botoes, "Exibir Relatório", exibir_relatorio)
    botao_exportar = criar_botao_estilizado(frame_botoes, "Exportar para CSV", exportar_dados)
    
    botao_exibir.pack(side=tk.LEFT, padx=(0, 10))
    botao_exportar.pack(side=tk.LEFT)
    
    criar_banco_dados()
    
    carregar_categorias()
    
    centralizar_janela(janela)
    
    return janela

def main():
    janela = criar_interface_relatorios()
    janela.mainloop()

if __name__ == "__main__":
    main()
