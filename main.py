import tkinter as tk
from config import largura_janela, altura_janela, proporcao_barra_lateral
from janela_grafico import GraficoJanela
from janela_controlador import ControleJanela
from referencias import terrenos

if __name__ == "__main__":
    janela = tk.Tk()
    
    # Obtenha as configurações de tamanho da janela
    janela.geometry(f"{largura_janela}x{altura_janela}")

    # Crie a instância da classe GraficoJanela
    janela_grafica = GraficoJanela(janela, proporcao_barra_lateral)

    # Crie a instância da classe ControleJanela e passe a instância da janela gráfica
    janela_controlador = ControleJanela(janela_grafica)

    janela.mainloop()