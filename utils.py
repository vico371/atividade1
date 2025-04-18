import tkinter as tk

def centralizar_janela(janela):
    """
    Centraliza a janela na tela do computador.
    
    Args:
        janela: Instância de tk.Tk ou tk.Toplevel a ser centralizada
    """
    # Atualiza a janela para garantir que as dimensões estejam corretas
    janela.update_idletasks()
    
    # Obtém a largura e altura da tela
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    
    # Obtém a largura e altura da janela
    largura_janela = janela.winfo_width()
    altura_janela = janela.winfo_height()
    
    # Calcula a posição x e y para centralizar a janela
    pos_x = (largura_tela - largura_janela) // 2
    pos_y = (altura_tela - altura_janela) // 2
    
    # Define a geometria da janela para centralizá-la
    janela.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

def configurar_botao_amarelo_verde(botao):
    """
    Configura um botão para ter cor amarela e mudar para verde quando selecionado.
    
    Args:
        botao: Instância de tk.Button a ser configurada
    """
    # Configura a cor de fundo amarela
    botao.config(bg="#FFFF00", activebackground="#00FF00")
    
    # Adiciona eventos para mudar a cor quando o botão é pressionado e liberado
    botao.bind("<ButtonPress-1>", lambda e: botao.config(bg="#00FF00"))
    botao.bind("<ButtonRelease-1>", lambda e: botao.config(bg="#FFFF00"))

def criar_botao_estilizado(master, texto, comando=None):
    """
    Cria um botão estilizado com cor amarela que muda para verde quando selecionado.
    
    Args:
        master: Widget pai onde o botão será criado
        texto: Texto a ser exibido no botão
        comando: Função a ser chamada quando o botão for clicado
        
    Returns:
        Instância de tk.Button configurada
    """
    botao = tk.Button(master, text=texto, command=comando, bg="#FFFF00", activebackground="#00FF00")
    
    # Adiciona eventos para mudar a cor quando o botão é pressionado e liberado
    botao.bind("<ButtonPress-1>", lambda e: botao.config(bg="#00FF00"))
    botao.bind("<ButtonRelease-1>", lambda e: botao.config(bg="#FFFF00"))
    
    return botao
