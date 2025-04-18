import tkinter as tk
from tkinter import filedialog, scrolledtext
import os
from utils import centralizar_janela, criar_botao_estilizado

# Parte 1: Gerador de Lista de Tarefas
def criar_gerador_tarefas():
    janela = tk.Tk()
    janela.title("Gerador de Lista de Tarefas")
    janela.geometry("500x500")
    
    # Frame principal
    frame = tk.Frame(janela, padx=20, pady=20)
    frame.pack(fill=tk.BOTH, expand=True)
    
    # Rótulo de título
    label_titulo = tk.Label(frame, text="Lista de Tarefas", font=("Arial", 16, "bold"))
    label_titulo.pack(pady=(0, 20))
    
    # Frame para entrada e botão de adicionar
    frame_entrada = tk.Frame(frame)
    frame_entrada.pack(fill=tk.X, pady=(0, 10))
    
    # Entrada para nova tarefa
    label_nova_tarefa = tk.Label(frame_entrada, text="Nova tarefa:", font=("Arial", 12))
    label_nova_tarefa.pack(side=tk.LEFT, padx=(0, 10))
    
    entrada_tarefa = tk.Entry(frame_entrada, font=("Arial", 12), width=30)
    entrada_tarefa.pack(side=tk.LEFT, fill=tk.X, expand=True)
    
    # Área de texto para exibir as tarefas
    label_tarefas = tk.Label(frame, text="Tarefas:", font=("Arial", 12))
    label_tarefas.pack(anchor=tk.W, pady=(10, 5))
    
    texto_tarefas = scrolledtext.ScrolledText(frame, width=50, height=10, font=("Arial", 12))
    texto_tarefas.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
    
    # Frame para os botões
    frame_botoes = tk.Frame(frame)
    frame_botoes.pack(fill=tk.X, pady=10)
    
    # Funções para manipular as tarefas
    def adicionar_tarefa():
        tarefa = entrada_tarefa.get()
        if tarefa:
            texto_tarefas.insert(tk.END, f"• {tarefa}\n")
            entrada_tarefa.delete(0, tk.END)
            entrada_tarefa.focus()
    
    def salvar_tarefas():
        conteudo = texto_tarefas.get(1.0, tk.END)
        if conteudo.strip():
            arquivo = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Arquivos de Texto", "*.txt"), ("Todos os Arquivos", "*.*")],
                title="Salvar Lista de Tarefas"
            )
            if arquivo:
                with open(arquivo, "w", encoding="utf-8") as f:
                    f.write(conteudo)
                label_status.config(text=f"Lista salva em: {os.path.basename(arquivo)}", fg="green")
    
    def carregar_tarefas():
        arquivo = filedialog.askopenfilename(
            filetypes=[("Arquivos de Texto", "*.txt"), ("Todos os Arquivos", "*.*")],
            title="Carregar Lista de Tarefas"
        )
        if arquivo:
            try:
                with open(arquivo, "r", encoding="utf-8") as f:
                    conteudo = f.read()
                texto_tarefas.delete(1.0, tk.END)
                texto_tarefas.insert(tk.END, conteudo)
                label_status.config(text=f"Lista carregada de: {os.path.basename(arquivo)}", fg="green")
            except Exception as e:
                label_status.config(text=f"Erro ao carregar o arquivo: {str(e)}", fg="red")
    
    def limpar_tarefas():
        texto_tarefas.delete(1.0, tk.END)
        label_status.config(text="Lista limpa", fg="blue")
    
    # Botão para adicionar tarefa
    botao_adicionar = criar_botao_estilizado(frame_entrada, "Adicionar", adicionar_tarefa)
    botao_adicionar.pack(side=tk.LEFT, padx=(10, 0))
    
    # Botões para salvar, carregar e limpar
    botao_salvar = criar_botao_estilizado(frame_botoes, "Salvar", salvar_tarefas)
    botao_carregar = criar_botao_estilizado(frame_botoes, "Carregar", carregar_tarefas)
    botao_limpar = criar_botao_estilizado(frame_botoes, "Limpar", limpar_tarefas)
    
    botao_salvar.pack(side=tk.LEFT, padx=(0, 10))
    botao_carregar.pack(side=tk.LEFT, padx=(0, 10))
    botao_limpar.pack(side=tk.LEFT)
    
    # Rótulo de status
    label_status = tk.Label(frame, text="", font=("Arial", 12))
    label_status.pack(pady=10)
    
    # Vincular a tecla Enter para adicionar tarefa
    entrada_tarefa.bind("<Return>", lambda event: adicionar_tarefa())
    
    # Centraliza a janela
    centralizar_janela(janela)
    
    # Foco na entrada de tarefa
    entrada_tarefa.focus()
    
    return janela

# Parte 2: Cadastro de Usuários
def criar_cadastro_usuarios():
    janela = tk.Tk()
    janela.title("Cadastro de Usuários")
    janela.geometry("500x500")
    
    # Frame principal
    frame = tk.Frame(janela, padx=20, pady=20)
    frame.pack(fill=tk.BOTH, expand=True)
    
    # Rótulo de título
    label_titulo = tk.Label(frame, text="Cadastro de Usuários", font=("Arial", 16, "bold"))
    label_titulo.pack(pady=(0, 20))
    
    # Frame para os campos de entrada
    frame_campos = tk.Frame(frame)
    frame_campos.pack(fill=tk.X, pady=(0, 10))
    
    # Campos de entrada
    label_nome = tk.Label(frame_campos, text="Nome:", font=("Arial", 12))
    label_nome.grid(row=0, column=0, sticky=tk.W, pady=5)
    entrada_nome = tk.Entry(frame_campos, font=("Arial", 12), width=30)
    entrada_nome.grid(row=0, column=1, sticky=tk.W, pady=5)
    
    label_idade = tk.Label(frame_campos, text="Idade:", font=("Arial", 12))
    label_idade.grid(row=1, column=0, sticky=tk.W, pady=5)
    entrada_idade = tk.Entry(frame_campos, font=("Arial", 12), width=10)
    entrada_idade.grid(row=1, column=1, sticky=tk.W, pady=5)
    
    label_email = tk.Label(frame_campos, text="E-mail:", font=("Arial", 12))
    label_email.grid(row=2, column=0, sticky=tk.W, pady=5)
    entrada_email = tk.Entry(frame_campos, font=("Arial", 12), width=30)
    entrada_email.grid(row=2, column=1, sticky=tk.W, pady=5)
    
    # Área de texto para exibir os usuários cadastrados
    label_usuarios = tk.Label(frame, text="Usuários Cadastrados:", font=("Arial", 12))
    label_usuarios.pack(anchor=tk.W, pady=(10, 5))
    
    texto_usuarios = scrolledtext.ScrolledText(frame, width=50, height=10, font=("Arial", 12))
    texto_usuarios.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
    
    # Frame para os botões
    frame_botoes = tk.Frame(frame)
    frame_botoes.pack(fill=tk.X, pady=10)
    
    # Funções para manipular os usuários
    def adicionar_usuario():
        nome = entrada_nome.get()
        idade = entrada_idade.get()
        email = entrada_email.get()
        
        # Validação básica
        if not nome or not idade or not email:
            label_status.config(text="Todos os campos são obrigatórios", fg="red")
            return
        
        try:
            idade_int = int(idade)
            if idade_int <= 0:
                label_status.config(text="A idade deve ser um número positivo", fg="red")
                return
        except ValueError:
            label_status.config(text="A idade deve ser um número válido", fg="red")
            return
        
        if "@" not in email or "." not in email:
            label_status.config(text="E-mail inválido", fg="red")
            return
        
        # Adiciona o usuário à lista
        texto_usuarios.insert(tk.END, f"Nome: {nome}, Idade: {idade}, E-mail: {email}\n")
        
        # Limpa os campos
        entrada_nome.delete(0, tk.END)
        entrada_idade.delete(0, tk.END)
        entrada_email.delete(0, tk.END)
        entrada_nome.focus()
        
        label_status.config(text="Usuário adicionado com sucesso", fg="green")
    
    def salvar_usuarios():
        conteudo = texto_usuarios.get(1.0, tk.END)
        if conteudo.strip():
            arquivo = filedialog.asksaveasfilename(
                defaultextension=".csv",
                filetypes=[("Arquivos CSV", "*.csv"), ("Todos os Arquivos", "*.*")],
                title="Salvar Cadastro de Usuários"
            )
            if arquivo:
                try:
                    # Converte o formato de exibição para CSV
                    linhas = conteudo.strip().split("\n")
                    with open(arquivo, "w", encoding="utf-8") as f:
                        f.write("Nome,Idade,Email\n")  # Cabeçalho
                        for linha in linhas:
                            if linha:
                                # Extrai os dados da linha
                                partes = linha.split(", ")
                                nome = partes[0].replace("Nome: ", "")
                                idade = partes[1].replace("Idade: ", "")
                                email = partes[2].replace("E-mail: ", "")
                                f.write(f"{nome},{idade},{email}\n")
                    
                    label_status.config(text=f"Cadastro salvo em: {os.path.basename(arquivo)}", fg="green")
                except Exception as e:
                    label_status.config(text=f"Erro ao salvar o arquivo: {str(e)}", fg="red")
    
    def limpar_campos():
        entrada_nome.delete(0, tk.END)
        entrada_idade.delete(0, tk.END)
        entrada_email.delete(0, tk.END)
        entrada_nome.focus()
        label_status.config(text="Campos limpos", fg="blue")
    
    # Botões
    botao_adicionar = criar_botao_estilizado(frame_botoes, "Adicionar", adicionar_usuario)
    botao_salvar = criar_botao_estilizado(frame_botoes, "Salvar CSV", salvar_usuarios)
    botao_limpar = criar_botao_estilizado(frame_botoes, "Limpar Campos", limpar_campos)
    
    botao_adicionar.pack(side=tk.LEFT, padx=(0, 10))
    botao_salvar.pack(side=tk.LEFT, padx=(0, 10))
    botao_limpar.pack(side=tk.LEFT)
    
    # Rótulo de status
    label_status = tk.Label(frame, text="", font=("Arial", 12))
    label_status.pack(pady=10)
    
    # Centraliza a janela
    centralizar_janela(janela)
    
    # Foco no primeiro campo
    entrada_nome.focus()
    
    return janela

# Parte 3: Validação de Dados em Arquivos
def criar_validador_dados():
    janela = tk.Tk()
    janela.title("Validação de Dados em Arquivos")
    janela.geometry("500x500")
    
    # Frame principal
    frame = tk.Frame(janela, padx=20, pady=20)
    frame.pack(fill=tk.BOTH, expand=True)
    
    # Rótulo de título
    label_titulo = tk.Label(frame, text="Validação de Dados", font=("Arial", 16, "bold"))
    label_titulo.pack(pady=(0, 20))
    
    # Frame para os campos de entrada
    frame_campos = tk.Frame(frame)
    frame_campos.pack(fill=tk.X, pady=(0, 10))
    
    # Campos de entrada
    label_nome = tk.Label(frame_campos, text="Nome:", font=("Arial", 12))
    label_nome.grid(row=0, column=0, sticky=tk.W, pady=5)
    entrada_nome = tk.Entry(frame_campos, font=("Arial", 12), width=30)
    entrada_nome.grid(row=0, column=1, sticky=tk.W, pady=5)
    
    label_idade = tk.Label(frame_campos, text="Idade:", font=("Arial", 12))
    label_idade.grid(row=1, column=0, sticky=tk.W, pady=5)
    entrada_idade = tk.Entry(frame_campos, font=("Arial", 12), width=10)
    entrada_idade.grid(row=1, column=1, sticky=tk.W, pady=5)
    
    label_email = tk.Label(frame_campos, text="E-mail:", font=("Arial", 12))
    label_email.grid(row=2, column=0, sticky=tk.W, pady=5)
    entrada_email = tk.Entry(frame_campos, font=("Arial", 12), width=30)
    entrada_email.grid(row=2, column=1, sticky=tk.W, pady=5)
    
    # Área de texto para exibir os dados validados
    label_dados = tk.Label(frame, text="Dados Validados:", font=("Arial", 12))
    label_dados.pack(anchor=tk.W, pady=(10, 5))
    
    texto_dados = scrolledtext.ScrolledText(frame, width=50, height=10, font=("Arial", 12))
    texto_dados.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
    
    # Frame para os botões
    frame_botoes = tk.Frame(frame)
    frame_botoes.pack(fill=tk.X, pady=10)
    
    # Funções para validar e manipular os dados
    def validar_dados():
        nome = entrada_nome.get()
        idade = entrada_idade.get()
        email = entrada_email.get()
        
        erros = []
        
        # Validação do nome
        if not nome:
            erros.append("O nome não pode estar vazio")
        
        # Validação da idade
        try:
            idade_int = int(idade)
            if idade_int <= 0:
                erros.append("A idade deve ser um número positivo")
        except ValueError:
            erros.append("A idade deve ser um número válido")
        
        # Validação do e-mail
        if "@" not in email or "." not in email:
            erros.append("O e-mail deve conter '@' e '.'")
        
        # Exibe o resultado da validação
        if erros:
            label_status.config(text="Erros de validação encontrados", fg="red")
            texto_dados.insert(tk.END, "ERROS DE VALIDAÇÃO:\n")
            for erro in erros:
                texto_dados.insert(tk.END, f"- {erro}\n")
            texto_dados.insert(tk.END, "\n")
        else:
            label_status.config(text="Dados validados com sucesso", fg="green")
            texto_dados.insert(tk.END, f"DADOS VÁLIDOS:\nNome: {nome}\nIdade: {idade}\nE-mail: {email}\n\n")
            
            # Limpa os campos após validação bem-sucedida
            entrada_nome.delete(0, tk.END)
            entrada_idade.delete(0, tk.END)
            entrada_email.delete(0, tk.END)
            entrada_nome.focus()
    
    def salvar_dados():
        conteudo = texto_dados.get(1.0, tk.END)
        if conteudo.strip():
            arquivo = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Arquivos de Texto", "*.txt"), ("Todos os Arquivos", "*.*")],
                title="Salvar Dados Validados"
            )
            if arquivo:
                with open(arquivo, "w", encoding="utf-8") as f:
                    f.write(conteudo)
                label_status.config(text=f"Dados salvos em: {os.path.basename(arquivo)}", fg="green")
    
    def limpar_tudo():
        entrada_nome.delete(0, tk.END)
        entrada_idade.delete(0, tk.END)
        entrada_email.delete(0, tk.END)
        texto_dados.delete(1.0, tk.END)
        label_status.config(text="Todos os campos foram limpos", fg="blue")
        entrada_nome.focus()
    
    # Botões
    botao_validar = criar_botao_estilizado(frame_botoes, "Validar", validar_dados)
    botao_salvar = criar_botao_estilizado(frame_botoes, "Salvar", salvar_dados)
    botao_limpar = criar_botao_estilizado(frame_botoes, "Limpar Tudo", limpar_tudo)
    
    botao_validar.pack(side=tk.LEFT, padx=(0, 10))
    botao_salvar.pack(side=tk.LEFT, padx=(0, 10))
    botao_limpar.pack(side=tk.LEFT)
    
    # Rótulo de status
    label_status = tk.Label(frame, text="", font=("Arial", 12))
    label_status.pack(pady=10)
    
    # Centraliza a janela
    centralizar_janela(janela)
    
    # Foco no primeiro campo
    entrada_nome.focus()
    
    return janela

# Função para escolher qual exemplo exibir
def main():
    janela_escolha = tk.Tk()
    janela_escolha.title("Manipulação de Arquivos")
    janela_escolha.geometry("500x200")
    
    label = tk.Label(janela_escolha, text="Escolha um exemplo para visualizar:", font=("Arial", 14))
    label.pack(pady=20)
    
    frame_botoes = tk.Frame(janela_escolha)
    frame_botoes.pack()
    
    def abrir_tarefas():
        janela_escolha.destroy()
        janela = criar_gerador_tarefas()
        janela.mainloop()
    
    def abrir_cadastro():
        janela_escolha.destroy()
        janela = criar_cadastro_usuarios()
        janela.mainloop()
    
    def abrir_validador():
        janela_escolha.destroy()
        janela = criar_validador_dados()
        janela.mainloop()
    
    botao_tarefas = criar_botao_estilizado(frame_botoes, "Lista de Tarefas", abrir_tarefas)
    botao_cadastro = criar_botao_estilizado(frame_botoes, "Cadastro de Usuários", abrir_cadastro)
    botao_validador = criar_botao_estilizado(frame_botoes, "Validação de Dados", abrir_validador)
    
    botao_tarefas.pack(side=tk.LEFT, padx=10)
    botao_cadastro.pack(side=tk.LEFT, padx=10)
    botao_validador.pack(side=tk.LEFT, padx=10)
    
    # Centraliza a janela
    centralizar_janela(janela_escolha)
    
    janela_escolha.mainloop()

if __name__ == "__main__":
    main()
