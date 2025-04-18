import tkinter as tk
from utils import centralizar_janela, configurar_botao_amarelo_verde, criar_botao_estilizado

def calcular_media():
    try:
        # Obtém os valores digitados
        numero1 = float(entrada1.get())
        numero2 = float(entrada2.get())
        
        # Calcula a média em vez da soma
        media = (numero1 + numero2) / 2
        
        # Exibe o resultado
        label_resultado.config(text=f"A média de {numero1} e {numero2} é {media:.2f}")
    except ValueError:
        # Exibe mensagem de erro
        label_resultado.config(text="Por favor, insira números válidos.")

def limpar_campos():
    # Limpa as entradas e o resultado
    entrada1.delete(0, tk.END)
    entrada2.delete(0, tk.END)
    label_resultado.config(text="")
    # Coloca o foco no primeiro campo
    entrada1.focus()

# Cria a janela principal
janela = tk.Tk()
janela.title("Calculadora de Média")
janela.geometry("400x350")

# Rótulo e entrada para o primeiro número
label1 = tk.Label(janela, text="Digite o primeiro número:", font=("Arial", 12))
label1.pack(pady=5)
entrada1 = tk.Entry(janela, font=("Arial", 12))
entrada1.pack(pady=5)

# Rótulo e entrada para o segundo número
label2 = tk.Label(janela, text="Digite o segundo número:", font=("Arial", 12))
label2.pack(pady=5)
entrada2 = tk.Entry(janela, font=("Arial", 12))
entrada2.pack(pady=5)

# Frame para os botões (para organizá-los lado a lado)
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

# Botão para calcular
botao_calcular = criar_botao_estilizado(frame_botoes, "Calcular Média", calcular_media)
botao_calcular.pack(side=tk.LEFT, padx=10)

# Botão para limpar
botao_limpar = criar_botao_estilizado(frame_botoes, "Limpar", limpar_campos)
botao_limpar.pack(side=tk.LEFT, padx=10)

# Rótulo para exibir o resultado
label_resultado = tk.Label(janela, text="", font=("Arial", 14))
label_resultado.pack(pady=20)

# Centraliza a janela na tela
centralizar_janela(janela)

# Mantém a janela aberta
janela.mainloop()
