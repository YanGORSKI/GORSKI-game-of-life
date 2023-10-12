import tkinter as tk
from tkinter import Scale

from mundo import Mundo
from lugar import Lugar
from referencias import terrenos
from config import largura_janela, altura_janela, tamanho_minimo_mapa, tamanho_maximo_mapa, proporcao_barra_lateral

class GraficoJanela:
    def __init__(self, janela, proporcao_barra_lateral):
        self.janela = janela
        
        # Obtenha o tamanho da janela
        largura, altura = largura_janela, altura_janela
        
        # Calcule o tamanho do lado do quadrado (Canvas)
        lado_quadrado = altura
        
        # Calcule a largura da barra lateral com base na proporção
        largura_barra_lateral = largura * proporcao_barra_lateral
        
        # Calcule a largura do Canvas com base nas dimensões da janela
        largura_canvas = largura - largura_barra_lateral

        self.janela.geometry(f"{largura}x{altura}")
        self.janela.title("Simulador de Vida")
        self.criar_interface(largura_barra_lateral)

    def criar_interface(self, largura_barra_lateral):
        largura_barra_lateral = largura_janela * proporcao_barra_lateral
        # Crie o frame da barra lateral
        self.barra_lateral = tk.Frame(self.janela, width=largura_barra_lateral, height=altura_janela, bg="lightgray")
        self.barra_lateral.grid(row=0, column=0, rowspan=2)

        # Crie o botão 'Iniciar' na barra lateral
        self.botao_iniciar = tk.Button(self.barra_lateral, text="Iniciar", command=self.iniciar_simulador)
        self.botao_iniciar.pack(side="bottom", pady=20)

        # Crie o Canvas como um quadrado com o lado igual à altura da janela
        self.canvas = tk.Canvas(self.janela, width=altura_janela, height=altura_janela, bg="white")
        self.canvas.grid(row=0, column=1)
    
        # Crie um slider para definir o tamanho do mundo
        self.tamanho_mundo_label = tk.Label(self.barra_lateral, text="Tamanho do Mundo:")
        self.tamanho_mundo_label.pack()

        self.tamanho_mundo_slider = Scale(self.barra_lateral, from_=tamanho_minimo_mapa, to=tamanho_maximo_mapa, orient="horizontal", length=largura_barra_lateral, resolution=altura_janela/30, showvalue=1)
        self.tamanho_mundo_slider.set(30)  # Valor inicial
        self.tamanho_mundo_slider.pack()
        
        # Crie o botão 'Gerar Terreno' na barra lateral
        self.botao_gerar_terreno = tk.Button(self.barra_lateral, text="Gerar Terreno", command=self.gerar_terreno)
        self.botao_gerar_terreno.pack(side="top", padx=20)
        
        

    def iniciar_simulador(self):
        # Adicione a lógica para iniciar o simulador aqui
        pass

    def gerar_terreno(self):
        # Obtenha o tamanho do mundo do slider
        tamanho_mundo = int(self.tamanho_mundo_slider.get())

        # Crie uma instância de Mundo com o tamanho escolhido
        mundo = Mundo(tamanho_mundo, tamanho_mundo)

        # Limpe o canvas para remover desenhos anteriores
        self.canvas.delete("all")

        # Calcula o tamanho do quadrado com base no tamanho do mundo
        tamanho_quadrado = 900 / tamanho_mundo

        # Percorra todos os lugares do mundo
        for y in range(tamanho_mundo):
            for x in range(tamanho_mundo):
                lugar = mundo.obter_lugar(x, y)
                tipo_terreno = lugar.terreno
                cor = terrenos[tipo_terreno]["cor"]

                # Calcule as coordenadas do retângulo
                x1 = x * tamanho_quadrado
                y1 = y * tamanho_quadrado
                x2 = (x + 1) * tamanho_quadrado
                y2 = (y + 1) * tamanho_quadrado

                # Desenhe o retângulo no canvas com a cor do terreno
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=cor, outline="gray50")
    