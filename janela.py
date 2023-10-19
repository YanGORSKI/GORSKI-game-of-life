import pygame
import config
import referencias
from janela_barraLateral import BarraLateral
from janela_canvas import Canvas

class JanelaPrincipal:
    def __init__(self):
        pygame.init()
        
        # CRIA A JANELA COM AS DIMENSÕES EM CONFIG.PY
        self.screen = pygame.display.set_mode((config.largura_janela, config.altura_janela))
        pygame.display.set_caption("Life Simulator")
        
        # INICIALIZA A BARRA LATERAL
        self.barra_lateral = BarraLateral(self.screen)
        
        # INICIALIZA O CANVAS
        self.canvas = Canvas(self.screen)
        

    def run(self):
        largura_janela = config.largura_janela
        altura_janela = config.altura_janela
        
        run = True
        clock = pygame.time.Clock()

        while run:
            clock.tick(config.taxa_att)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    

            self.screen.fill(referencias.cores["preto"])  # Preencha a tela com a cor de fundo

            # Desenhe a barra lateral com os componentes
            self.barra_lateral.atualizar()
            self.canvas.atualizar()

            # Aqui você pode adicionar a lógica do seu jogo na parte do "canvas"

            pygame.display.flip()

        pygame.quit()

# if __name__ == "__main__":
#     pygame.init()
#     largura_janela = config.largura_janela
#     altura_janela = config.altura_janela
#     screen = pygame.display.set_mode((largura_janela, altura_janela))
#     pygame.display.set_caption("Simulador de Vida")
#     run(screen)