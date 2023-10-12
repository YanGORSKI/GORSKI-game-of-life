from lugar import Lugar

class Mundo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.mapa = [[Lugar(x, y, terreno='agua', conteudo=None) for x in range(largura)] for y in range(altura)]

    def obter_lugar(self, x, y):
        return self.mapa[y][x]

    def definir_conteudo_lugar(self, x, y, conteudo):
        self.mapa[y][x].definir_conteudo(conteudo)

    def tornar_passavel_lugar(self, x, y):
        self.mapa[y][x].tornar_passavel()

    def tornar_impassavel_lugar(self, x, y):
        self.mapa[y][x].tornar_impassavel()