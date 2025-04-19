import tkinter as tk
from utils import centralizar_janela, criar_botao_estilizado

def exibir_dados():
   
    nome = entrada_nome.get()
    email = entrada_email.get()
    preferencia = var_preferencia.get()
    
    print("Dados do formulário:")
    print(f"Nome: {nome}")
    print(f"E-mail: {email}")
    print(f"Preferência de contato: {preferencia}")
    
    resultado = f"Nome: {nome}\nE-mail: {email}\nPreferência: {preferencia}"
    label_resultado.config(text=resultado)

janela = tk.Tk()
janela.title("Mini-Formulário")
janela.geometry("400x350")

frame_principal = tk.Frame(janela, padx=20, pady=20)
frame_principal.pack(fill=tk.BOTH, expand=True)

label_nome = tk.Label(frame_principal, text="Nome:", font=("Arial", 12))
label_nome.pack(anchor=tk.W, pady=(0, 5))
entrada_nome = tk.Entry(frame_principal, font=("Arial", 12), width=30)
entrada_nome.pack(fill=tk.X, pady=(0, 10))

label_email = tk.Label(frame_principal, text="E-mail:", font=("Arial", 12))
label_email.pack(anchor=tk.W, pady=(0, 5))
entrada_email = tk.Entry(frame_principal, font=("Arial", 12), width=30)
entrada_email.pack(fill=tk.X, pady=(0, 10))

label_preferencia = tk.Label(frame_principal, text="Preferência de contato:", font=("Arial", 12))
label_preferencia.pack(anchor=tk.W, pady=(0, 5))

var_preferencia = tk.StringVar(value="E-mail")

frame_radio = tk.Frame(frame_principal)
frame_radio.pack(fill=tk.X, pady=(0, 10))

rb_email = tk.Radiobutton(frame_radio, text="E-mail", variable=var_preferencia, value="E-mail", font=("Arial", 12))
rb_email.pack(side=tk.LEFT, padx=(0, 10))
rb_telefone = tk.Radiobutton(frame_radio, text="Telefone", variable=var_preferencia, value="Telefone", font=("Arial", 12))
rb_telefone.pack(side=tk.LEFT)

botao_exibir = criar_botao_estilizado(frame_principal, "Exibir Dados", exibir_dados)
botao_exibir.pack(pady=15)

label_resultado = tk.Label(frame_principal, text="", font=("Arial", 12), justify=tk.LEFT)
label_resultado.pack(pady=10, fill=tk.X)

centralizar_janela(janela)

janela.mainloop()
