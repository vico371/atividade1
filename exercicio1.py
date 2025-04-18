import tkinter as tk
from utils import centralizar_janela, configurar_botao_amarelo_verde

def calcular_triplo():
    try:
        numero = int(entrada.get())
        resultado = numero * 3  # Calcula o triplo em vez do dobro
        label_resultado.config(text=f"O triplo de {numero} é {resultado}")
    except ValueError:
        label_resultado.config(text="Por favor, insira um número válido.")

# Criar a janela principal
janela = tk.Tk()
janela.title("Calculadora de Triplo")
janela.geometry("400x200")

# Rótulo de instrução para o usuário
label_instrucao = tk.Label(janela, text="Digite um número:", font=("Arial", 14))
label_instrucao.pack(pady=10)

# Entrada de dados
entrada = tk.Entry(janela, font=("Arial", 14))
entrada.pack(pady=10)

# Botão para calcular
botao_calcular = tk.Button(janela, text="Calcular", command=calcular_triplo)
configurar_botao_amarelo_verde(botao_calcular)  # Aplica o estilo amarelo/verde
botao_calcular.pack(pady=10)

# Rótulo para exibir o resultado
label_resultado = tk.Label(janela, text="", font=("Arial", 14))
label_resultado.pack(pady=10)

# Centraliza a janela na tela
centralizar_janela(janela)

# Iniciar a interface
janela.mainloop()

