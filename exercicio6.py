import tkinter as tk
import re
from utils import centralizar_janela, criar_botao_estilizado

def criar_validador_email():
    janela = tk.Tk()
    janela.title("Validador de E-mail")
    janela.geometry("400x250")
    
    label_instrucao = tk.Label(janela, text="Digite um endereço de e-mail:", font=("Arial", 12))
    label_instrucao.pack(pady=10)
    
    entrada_email = tk.Entry(janela, font=("Arial", 12), width=30)
    entrada_email.pack(pady=10)
    
    label_resultado = tk.Label(janela, text="", font=("Arial", 12))
    label_resultado.pack(pady=10)
    
    def validar_email():
        email = entrada_email.get()
        if "@" in email and "." in email:
            label_resultado.config(text="E-mail válido!", fg="green")
        else:
            label_resultado.config(text="E-mail inválido! Deve conter '@' e '.'", fg="red")
    
    botao_validar = criar_botao_estilizado(janela, "Validar E-mail", validar_email)
    botao_validar.pack(pady=20)
    
    centralizar_janela(janela)
    
    return janela

def criar_validador_faixa():
    janela = tk.Tk()
    janela.title("Validador de Faixa Numérica")
    janela.geometry("400x250")
    
    label_instrucao = tk.Label(janela, text="Digite um número entre 1 e 100:", font=("Arial", 12))
    label_instrucao.pack(pady=10)
    
    entrada_numero = tk.Entry(janela, font=("Arial", 12), width=10)
    entrada_numero.pack(pady=10)
    
    label_resultado = tk.Label(janela, text="", font=("Arial", 12))
    label_resultado.pack(pady=10)
    
    def validar_numero():
        try:
            numero = int(entrada_numero.get())
            if 1 <= numero <= 100:
                label_resultado.config(text=f"Número válido: {numero}", fg="green")
            else:
                label_resultado.config(text="Erro: O número deve estar entre 1 e 100", fg="red")
        except ValueError:
            label_resultado.config(text="Erro: Digite um número válido", fg="red")
    
    botao_validar = criar_botao_estilizado(janela, "Validar Número", validar_numero)
    botao_validar.pack(pady=20)
    
    centralizar_janela(janela)
    
    return janela

def criar_cadastro_simples():
    janela = tk.Tk()
    janela.title("Cadastro Simples")
    janela.geometry("400x300")
    
    frame = tk.Frame(janela, padx=20, pady=20)
    frame.pack(fill=tk.BOTH, expand=True)
    
    label_nome = tk.Label(frame, text="Nome:", font=("Arial", 12))
    label_nome.pack(anchor=tk.W, pady=(0, 5))
    entrada_nome = tk.Entry(frame, font=("Arial", 12), width=30)
    entrada_nome.pack(fill=tk.X, pady=(0, 10))
    
    label_idade = tk.Label(frame, text="Idade:", font=("Arial", 12))
    label_idade.pack(anchor=tk.W, pady=(0, 5))
    entrada_idade = tk.Entry(frame, font=("Arial", 12), width=10)
    entrada_idade.pack(anchor=tk.W, pady=(0, 10))
    
    label_resultado = tk.Label(frame, text="", font=("Arial", 12))
    label_resultado.pack(pady=10)
    
    def validar_cadastro():
        nome = entrada_nome.get()
        idade = entrada_idade.get()
        
        if not nome:
            label_resultado.config(text="Erro: O nome não pode estar vazio", fg="red")
            return
        
        try:
            idade_int = int(idade)
            if idade_int <= 0:
                label_resultado.config(text="Erro: A idade deve ser um número positivo", fg="red")
                return
        except ValueError:
            label_resultado.config(text="Erro: A idade deve ser um número válido", fg="red")
            return
        
        label_resultado.config(text=f"Cadastro válido!\nNome: {nome}\nIdade: {idade_int}", fg="green")
    
    botao_validar = criar_botao_estilizado(frame, "Validar Cadastro", validar_cadastro)
    botao_validar.pack(pady=10)
    
    centralizar_janela(janela)
    
    return janela

def main():
    janela_escolha = tk.Tk()
    janela_escolha.title("Validação de Entradas")
    janela_escolha.geometry("500x200")
    
    label = tk.Label(janela_escolha, text="Escolha um exemplo para visualizar:", font=("Arial", 14))
    label.pack(pady=20)
    
    frame_botoes = tk.Frame(janela_escolha)
    frame_botoes.pack()
    
    def abrir_email():
        janela_escolha.destroy()
        janela = criar_validador_email()
        janela.mainloop()
    
    def abrir_faixa():
        janela_escolha.destroy()
        janela = criar_validador_faixa()
        janela.mainloop()
    
    def abrir_cadastro():
        janela_escolha.destroy()
        janela = criar_cadastro_simples()
        janela.mainloop()
    
    botao_email = criar_botao_estilizado(frame_botoes, "Validar E-mail", abrir_email)
    botao_faixa = criar_botao_estilizado(frame_botoes, "Faixa Numérica", abrir_faixa)
    botao_cadastro = criar_botao_estilizado(frame_botoes, "Cadastro Simples", abrir_cadastro)
    
    botao_email.pack(side=tk.LEFT, padx=10)
    botao_faixa.pack(side=tk.LEFT, padx=10)
    botao_cadastro.pack(side=tk.LEFT, padx=10)
    
    centralizar_janela(janela_escolha)
    
    janela_escolha.mainloop()

if __name__ == "__main__":
    main()
