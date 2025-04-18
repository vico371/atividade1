import tkinter as tk
from utils import centralizar_janela, criar_botao_estilizado

def exibir_dados():
    # Obtém os dados do formulário
    nome = entrada_nome.get()
    email = entrada_email.get()
    preferencia = var_preferencia.get()
    
    # Exibe os dados no terminal
    print("Dados do formulário:")
    print(f"Nome: {nome}")
    print(f"E-mail: {email}")
    print(f"Preferência de contato: {preferencia}")
    
    # Também exibe na interface para feedback ao usuário
    resultado = f"Nome: {nome}\nE-mail: {email}\nPreferência: {preferencia}"
    label_resultado.config(text=resultado)

# Criar a janela principal
janela = tk.Tk()
janela.title("Mini-Formulário")
janela.geometry("400x350")

# Frame principal
frame_principal = tk.Frame(janela, padx=20, pady=20)
frame_principal.pack(fill=tk.BOTH, expand=True)

# Rótulo e entrada para o nome
label_nome = tk.Label(frame_principal, text="Nome:", font=("Arial", 12))
label_nome.pack(anchor=tk.W, pady=(0, 5))
entrada_nome = tk.Entry(frame_principal, font=("Arial", 12), width=30)
entrada_nome.pack(fill=tk.X, pady=(0, 10))

# Rótulo e entrada para o e-mail
label_email = tk.Label(frame_principal, text="E-mail:", font=("Arial", 12))
label_email.pack(anchor=tk.W, pady=(0, 5))
entrada_email = tk.Entry(frame_principal, font=("Arial", 12), width=30)
entrada_email.pack(fill=tk.X, pady=(0, 10))

# Rótulo e opções para preferência de contato
label_preferencia = tk.Label(frame_principal, text="Preferência de contato:", font=("Arial", 12))
label_preferencia.pack(anchor=tk.W, pady=(0, 5))

# Variável para armazenar a preferência
var_preferencia = tk.StringVar(value="E-mail")

# Frame para os radio buttons
frame_radio = tk.Frame(frame_principal)
frame_radio.pack(fill=tk.X, pady=(0, 10))

# Radio buttons para preferência
rb_email = tk.Radiobutton(frame_radio, text="E-mail", variable=var_preferencia, value="E-mail", font=("Arial", 12))
rb_email.pack(side=tk.LEFT, padx=(0, 10))
rb_telefone = tk.Radiobutton(frame_radio, text="Telefone", variable=var_preferencia, value="Telefone", font=("Arial", 12))
rb_telefone.pack(side=tk.LEFT)

# Botão para exibir os dados
botao_exibir = criar_botao_estilizado(frame_principal, "Exibir Dados", exibir_dados)
botao_exibir.pack(pady=15)

# Rótulo para exibir o resultado
label_resultado = tk.Label(frame_principal, text="", font=("Arial", 12), justify=tk.LEFT)
label_resultado.pack(pady=10, fill=tk.X)

# Centraliza a janela na tela
centralizar_janela(janela)

# Iniciar a interface
janela.mainloop()
