import pygame
import janela
import config
from janela import JanelaPrincipal

def main():
    pygame.init()

    largura_janela = config.largura_janela
    altura_janela = config.altura_janela

    # Crie a janela com as dimensões definidas no config.py
    screen = pygame.display.set_mode((largura_janela, altura_janela))
    pygame.display.set_caption("Life Simulator")

    # Inicialize a janela e comece a execução do jogo
    janela = JanelaPrincipal()
    janela.run()

if __name__ == "__main__":
    main()