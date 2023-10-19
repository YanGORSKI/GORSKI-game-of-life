import random

class Lugar:
    def __init__(self, x, y, conteudo=None, passavel=True):
        self.x = x
        self.y = y
        self.terreno = None
        self.conteudo = conteudo
        self.passavel = passavel
        self.vizinho_norte = None
        self.vizinho_nordeste = None
        self.vizinho_leste = None
        self.vizinho_sudeste = None
        self.vizinho_sul = None
        self.vizinho_sudoeste = None
        self.vizinho_oeste = None
        self.vizinho_noroeste = None
        self.vizinhos = [self.vizinho_norte,
                        self.vizinho_nordeste,
                        self.vizinho_leste,
                        self.vizinho_sudeste,
                        self.vizinho_sul,
                        self.vizinho_sudoeste,
                        self.vizinho_oeste,
                        self.vizinho_noroeste]

    def definir_conteudo(self, conteudo):
        self.conteudo = conteudo
        
    def gerar_terreno(self):
        # Probabilidades para cada tipo de terreno
        terrenos = ["agua", "terra", "grama", "rocha"]
        chances = [0.10, 0.30, 0.40, 0.20]
        terreno_escolhido = random.choices(terrenos, chances)[0]
        return terreno_escolhido

    def tornar_passavel(self):
        self.passavel = True

    def tornar_impassavel(self):
        self.passavel = False
        