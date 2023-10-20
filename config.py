# Tamanho da janela
largura_janela = 1280
altura_janela = 650

# Proporção da barra lateral em relação à largura da janela
proporcao_barra_lateral = 0.3
largura_barra_lateral = int(largura_janela * proporcao_barra_lateral)

# Tamanho mínimo e máximo do mapa
tamanho_minimo_mapa = altura_janela/30
tamanho_maximo_mapa = altura_janela/5

# Configurações de velocidade
ticks_por_segundo = 1  # 1 segundo = 1 tick = 10 microticks

# Configurações de tempo e dia
microticks_por_tick = 10
ticks_por_dia = 15
taxa_att = int(((1/ticks_por_segundo)/microticks_por_tick)*1000)