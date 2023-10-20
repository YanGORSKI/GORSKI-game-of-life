import pygame
import config
import referencias
from janela_canvas import Canvas

# Defina algumas cores para uso
preto = referencias.cores["preto"]
branco = referencias.cores["branco"]
cinza = referencias.cores["cinza"]
cinza_claro = referencias.cores["cinza_claro"]

# Outras constantes relacionadas à barra lateral
largura_barra_lateral = config.largura_janela * config.proporcao_barra_lateral

class BarraLateral:
    def __init__(self, screen, canvas):
        self.screen = screen
        self.canvas = canvas
        self.botao_gerar_terreno = pygame.Rect(20, 120, 200, 50)  # Ajuste a posição do botão

    def atualizar(self):
        # Código relacionado à barra lateral
        self.criar_barra_lateral()
        
    def processar_clique(self, posicao):
        if self.botao_gerar_terreno.collidepoint(posicao):
            self.canvas.criar_mundo(24, 24)

    def criar_barra_lateral(self):
        largura_janela = config.largura_janela
        altura_janela = config.altura_janela

        # Tamanho da barra lateral em relação à largura da janela
        largura_barra_lateral = largura_janela * config.proporcao_barra_lateral

        # Tipos de Texto
        titulo = pygame.font.Font(referencias.fonte_lucidaConsole, 30)
        textoPadrao = pygame.font.Font(referencias.fonte_lucidaConsole, 20)
        textoBotao = pygame.font.Font(referencias.fonte_lucidaConsole, 20)
        
        # Desenhe a barra lateral
        barra_lateral = pygame.Rect(0, 0, largura_barra_lateral, altura_janela)
        pygame.draw.rect(self.screen, branco, barra_lateral)

        # Crie uma "frame" para os elementos superiores (informações de tempo)
        frame_tempo = pygame.Rect(10, 10, largura_barra_lateral - 20, 70)
        pygame.draw.rect(self.screen, cinza_claro, frame_tempo)
        
        # Exiba o texto "Tempo Decorrido" e as informações de tempo e dia na "frame" superior
        texto_tempo_decorrido = textoPadrao.render("Elapsed Time: 00:00:00", True, preto)
        texto_tempo_decorrido_rect = texto_tempo_decorrido.get_rect(center=(largura_barra_lateral / 2, 30))

        texto_info_dia = textoPadrao.render("Day 0 | 0.0", True, preto)
        texto_info_dia_rect = texto_info_dia.get_rect(center=(largura_barra_lateral / 2, 60))

        self.screen.blit(texto_tempo_decorrido, texto_tempo_decorrido_rect)
        self.screen.blit(texto_info_dia, texto_info_dia_rect)

        # Crie uma "frame" para configurações de Terreno
        frame_terreno = pygame.Rect(10, 90, largura_barra_lateral - 20, 150)
        pygame.draw.rect(self.screen, cinza, frame_terreno)
        
        # Crie o botão dentro da "frame" de terreno
        botao_gerar_terreno = pygame.Rect(20, 120, 200, 50)
        pygame.draw.rect(self.screen, cinza_claro, botao_gerar_terreno)
        texto_botao_gerar_terreno = textoBotao.render("Generate Terrain", True, preto)
        texto_botao_gerar_terreno_rect = texto_botao_gerar_terreno.get_rect(center=botao_gerar_terreno.center)
        self.screen.blit(texto_botao_gerar_terreno, texto_botao_gerar_terreno_rect)

        # Crie uma "frame" para as configurações de Simulação
        frame_simulacao = pygame.Rect(10, 260, largura_barra_lateral - 20, 250)
        pygame.draw.rect(self.screen, cinza, frame_simulacao)

        # Crie os botões dentro da "frame" de simulação
        botao_iniciar_pausar = pygame.Rect(20, 290, 200, 50)
        pygame.draw.rect(self.screen, cinza_claro, botao_iniciar_pausar)
        texto_botao_iniciar_pausar = textoBotao.render("Start/Pause", True, preto)
        texto_botao_iniciar_pausar_rect = texto_botao_iniciar_pausar.get_rect(center=botao_iniciar_pausar.center)
        self.screen.blit(texto_botao_iniciar_pausar, texto_botao_iniciar_pausar_rect)

        botao_zerar_simulacao = pygame.Rect(20, 360, 200, 50)
        pygame.draw.rect(self.screen, cinza_claro, botao_zerar_simulacao)
        texto_botao_zerar_simulacao = textoBotao.render("Reset", True, preto)
        texto_botao_zerar_simulacao_rect = texto_botao_zerar_simulacao.get_rect(center=botao_zerar_simulacao.center)
        self.screen.blit(texto_botao_zerar_simulacao, texto_botao_zerar_simulacao_rect)