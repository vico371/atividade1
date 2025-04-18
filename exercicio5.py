import tkinter as tk
from utils import centralizar_janela, criar_botao_estilizado

# Parte 1: Cores Dinâmicas
def criar_cores_dinamicas():
    janela = tk.Tk()
    janela.title("Cores Dinâmicas")
    janela.geometry("500x300")
    
    # Rótulo de instrução
    label_instrucao = tk.Label(janela, text="Clique nos lados esquerdo ou direito da janela", font=("Arial", 14))
    label_instrucao.pack(pady=20)
    
    # Rótulo para mostrar qual lado foi clicado
    label_resultado = tk.Label(janela, text="", font=("Arial", 12))
    label_resultado.pack(pady=10)
    
    # Função para mudar a cor de fundo
    def mudar_cor(evento):
        largura = janela.winfo_width()
        if evento.x < largura / 2:
            janela.configure(bg="#FFD700")  # Amarelo para o lado esquerdo
            label_resultado.config(text="Lado Esquerdo Clicado", bg="#FFD700")
            label_instrucao.config(bg="#FFD700")
        else:
            janela.configure(bg="#00FF00")  # Verde para o lado direito
            label_resultado.config(text="Lado Direito Clicado", bg="#00FF00")
            label_instrucao.config(bg="#00FF00")
    
    # Vincular o evento de clique do mouse
    janela.bind("<Button-1>", mudar_cor)
    
    # Centraliza a janela
    centralizar_janela(janela)
    
    return janela

# Parte 2: Teclado Interativo
def criar_teclado_interativo():
    janela = tk.Tk()
    janela.title("Teclado Interativo")
    janela.geometry("400x250")
    
    # Rótulo de instrução
    label_instrucao = tk.Label(janela, text="Pressione qualquer tecla", font=("Arial", 14))
    label_instrucao.pack(pady=20)
    
    # Rótulo para mostrar a tecla pressionada
    label_tecla = tk.Label(janela, text="", font=("Arial", 24))
    label_tecla.pack(pady=20)
    
    # Função para mostrar a tecla pressionada
    def mostrar_tecla(evento):
        tecla = evento.keysym
        label_tecla.config(text=f"Tecla: {tecla}")
    
    # Vincular o evento de tecla pressionada
    janela.bind("<Key>", mostrar_tecla)
    
    # Botão para limpar
    botao_limpar = criar_botao_estilizado(janela, "Limpar", lambda: label_tecla.config(text=""))
    botao_limpar.pack(pady=20)
    
    # Centraliza a janela
    centralizar_janela(janela)
    
    # Foco na janela para capturar eventos de teclado
    janela.focus_set()
    
    return janela

# Parte 3: Jogo do Contador
def criar_jogo_contador():
    janela = tk.Tk()
    janela.title("Jogo do Contador")
    janela.geometry("400x300")
    
    # Variável para armazenar o contador
    contador = tk.IntVar(value=0)
    
    # Rótulo para mostrar o contador
    label_contador = tk.Label(janela, textvariable=contador, font=("Arial", 36))
    label_contador.pack(pady=20)
    
    # Frame para os botões
    frame_botoes = tk.Frame(janela)
    frame_botoes.pack(pady=20)
    
    # Funções para manipular o contador
    def incrementar():
        contador.set(contador.get() + 1)
    
    def decrementar():
        contador.set(contador.get() - 1)
    
    def resetar():
        contador.set(0)
    
    # Botões para incrementar, decrementar e resetar
    botao_incrementar = criar_botao_estilizado(frame_botoes, "+", incrementar)
    botao_decrementar = criar_botao_estilizado(frame_botoes, "-", decrementar)
    botao_resetar = criar_botao_estilizado(frame_botoes, "Resetar", resetar)
    
    botao_incrementar.pack(side=tk.LEFT, padx=10)
    botao_decrementar.pack(side=tk.LEFT, padx=10)
    botao_resetar.pack(side=tk.LEFT, padx=10)
    
    # Centraliza a janela
    centralizar_janela(janela)
    
    return janela

# Função para escolher qual exemplo exibir
def main():
    janela_escolha = tk.Tk()
    janela_escolha.title("Eventos e Manipulação")
    janela_escolha.geometry("500x200")
    
    label = tk.Label(janela_escolha, text="Escolha um exemplo para visualizar:", font=("Arial", 14))
    label.pack(pady=20)
    
    frame_botoes = tk.Frame(janela_escolha)
    frame_botoes.pack()
    
    def abrir_cores():
        janela_escolha.destroy()
        janela = criar_cores_dinamicas()
        janela.mainloop()
    
    def abrir_teclado():
        janela_escolha.destroy()
        janela = criar_teclado_interativo()
        janela.mainloop()
    
    def abrir_contador():
        janela_escolha.destroy()
        janela = criar_jogo_contador()
        janela.mainloop()
    
    botao_cores = criar_botao_estilizado(frame_botoes, "Cores Dinâmicas", abrir_cores)
    botao_teclado = criar_botao_estilizado(frame_botoes, "Teclado Interativo", abrir_teclado)
    botao_contador = criar_botao_estilizado(frame_botoes, "Jogo do Contador", abrir_contador)
    
    botao_cores.pack(side=tk.LEFT, padx=10)
    botao_teclado.pack(side=tk.LEFT, padx=10)
    botao_contador.pack(side=tk.LEFT, padx=10)
    
    # Centraliza a janela
    centralizar_janela(janela_escolha)
    
    janela_escolha.mainloop()

if __name__ == "__main__":
    main()
