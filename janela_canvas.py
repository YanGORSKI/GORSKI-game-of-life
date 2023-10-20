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
        exibir_contorno = False
        tamanho_mundo = 24
        tamanho_canvas = config.largura_janela - config.largura_barra_lateral

        tamanho_quadrado = tamanho_canvas / tamanho_mundo

        if self.mundo:
            for y in range(tamanho_mundo):
                for x in range(tamanho_mundo):
                    lugar = self.mundo.obter_lugar(x, y)
                    tipo_terreno = lugar.terreno
                    cor = referencias.terrenos[tipo_terreno]["cor"]

                    # Calcule as coordenadas do retângulo
                    x1 = x * tamanho_quadrado + config.largura_barra_lateral  # Adicione a largura da barra lateral ao X
                    y1 = y * tamanho_quadrado

                    # Crie um retângulo na tela usando pygame.draw.rect
                    pygame.draw.rect(self.screen, cor, (x1, y1, tamanho_quadrado, tamanho_quadrado))
                    
                    # Se a Checkbox de contorno estiver marcada, desenhe o retângulo com outline
                    if exibir_contorno:
                        pygame.draw.rect(self.screen, referencias.cores["cinza"], (x1, y1, tamanho_quadrado, tamanho_quadrado), 1)


    def criar_mundo(self, largura, altura):
        # Crie o mundo com as dimensões desejadas
        self.mundo = Mundo(largura, altura)
        
        # Adicione a lógica para gerar o terreno no mundo conforme necessário

    # Outros métodos para manipular elementos gráficos no "canvas"

# ...