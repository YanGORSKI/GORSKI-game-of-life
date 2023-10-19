import pygame
import referencias
import config
from mundo import Mundo
from lugar import Lugar


# Defina algumas cores
# ...

class Canvas:
    def __init__(self, screen):
        self.screen = screen
        self.mundo = None  # Inicialize o mundo como None, ele será criado posteriormente

    def atualizar(self):
        self.criar_canvas()
        
    def criar_canvas(self):
        exibir_contorno = True
        tamanho_mundo = 24
        tamanho_quadrado = config.altura_janela / tamanho_mundo
        
        # Adicione a lógica para desenhar o mundo no "canvas" aqui
        if self.mundo:
           # Percorra todos os lugares do mundo
            for y in range(tamanho_mundo):
                for x in range(tamanho_mundo):
                    lugar = self.mundo.obter_lugar(x, y)
                    tipo_terreno = lugar.terreno
                    cor = referencias.terrenos[tipo_terreno]["cor"]

                    # Calcule as coordenadas do retângulo
                    x1 = x * tamanho_quadrado
                    y1 = y * tamanho_quadrado
                    x2 = (x + 1) * tamanho_quadrado
                    y2 = (y + 1) * tamanho_quadrado

                    # Se a Checkbox de contorno estiver marcada, desenhe o retângulo com outline
                    if exibir_contorno:
                        self.canvas.create_rectangle(x1, y1, x2, y2, fill=cor, outline=referencias.cores["cinza"])
                    else:
                        self.canvas.create_rectangle(x1, y1, x2, y2, fill=cor, outline="")

    def criar_mundo(self, largura, altura):
        # Crie o mundo com as dimensões desejadas
        self.mundo = Mundo(largura, altura)
        # Adicione a lógica para gerar o terreno no mundo conforme necessário

    # Outros métodos para manipular elementos gráficos no "canvas"

# ...