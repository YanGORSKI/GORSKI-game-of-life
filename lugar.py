class Lugar:
    def __init__(self, x, y, terreno, conteudo=None, passavel=True):
        self.x = x
        self.y = y
        self.terreno = terreno
        self.conteudo = conteudo
        self.passavel = passavel

    def definir_conteudo(self, conteudo):
        self.conteudo = conteudo

    def tornar_passavel(self):
        self.passavel = True

    def tornar_impassavel(self):
        self.passavel = False