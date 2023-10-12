import tkinter as tk
from config import largura_janela, altura_janela, proporcao_barra_lateral
from janela_app import JanelaApp
from referencias import terrenos

if __name__ == "__main__":
    janela = tk.Tk()

    # Crie a instância da classe GraficoJanela
    janelaApp = JanelaApp(janela)
    
    # Obtenha as configurações de tamanho da janela
    janela.geometry(f"{largura_janela}x{altura_janela}")

    janela.mainloop()