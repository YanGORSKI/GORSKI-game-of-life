import pygame
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
        # Adicione a lógica para desenhar o mundo no "canvas" aqui
        if self.mundo:
            # Itere sobre o mundo e desenhe os elementos gráficos na tela
            for y in range(self.mundo.altura):
                for x in range(self.mundo.largura):
                    lugar = self.mundo.obter_lugar(x, y)
                    # Desenhe a célula com base no terreno, posição e outros parâmetros
                    # Use pygame.draw.rect para desenhar os terrenos no "canvas"
                    # Por exemplo: pygame.draw.rect(self.screen, lugar.terreno, (x * tamanho_celula, y * tamanho_celula, tamanho_celula, tamanho_celula))

    def criar_mundo(self, largura, altura):
        # Crie o mundo com as dimensões desejadas
        self.mundo = Mundo(largura, altura)
        # Adicione a lógica para gerar o terreno no mundo conforme necessário

    # Outros métodos para manipular elementos gráficos no "canvas"

# ...