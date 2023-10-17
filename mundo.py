from lugar import Lugar
import random
import noise


class Mundo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.mapa = [[Lugar(x, y, conteudo=None) for x in range(largura)] for y in range(altura)]

    def obter_lugar(self, x, y):
        return self.mapa[y][x]

    def definir_conteudo_lugar(self, x, y, conteudo):
        self.mapa[y][x].definir_conteudo(conteudo)

    def tornar_passavel_lugar(self, x, y):
        self.mapa[y][x].tornar_passavel()

    def tornar_impassavel_lugar(self, x, y):
        self.mapa[y][x].tornar_impassavel()
    
    def gerar_ruido(self, x, y, scale, octaves, persistence, lacunarity, min_value, max_value, repeatx, repeaty, base):
        # Use noise.snoise2 para gerar ruído em 2D
        value = noise.snoise2(x / scale, y / scale, octaves=octaves, persistence=persistence, lacunarity=lacunarity, repeatx=repeatx, repeaty=repeaty, base=base)

        # Mapeie o valor do ruído para o intervalo desejado (por exemplo, entre min_value e max_value)
        return (value - min_value) / (max_value - min_value)
        
    def gerar_terrenos_base(self, scale, octaves, persistence, lacunarity, min_value, max_value, repeatx, repeaty, base, altura_agua, altura_terra, altura_grama):
        for y in range(self.altura):
            for x in range(self.largura):
                ruido = self.gerar_ruido(x, y, scale, octaves, persistence, lacunarity, min_value, max_value, repeatx, repeaty, base)
                # Mapeie o valor do ruído para os tipos de terreno desejados com base em thresholds
                # Por exemplo, se ruido < 0.2, é água; se ruido < 0.6, é terra; etc.
                if ruido < altura_agua:
                    self.mapa[y][x].terreno = "agua"
                elif ruido < altura_terra:
                    self.mapa[y][x].terreno = "terra"
                elif ruido < altura_grama:
                    self.mapa[y][x].terreno = "grama"
                else:
                    self.mapa[y][x].terreno = "rocha"