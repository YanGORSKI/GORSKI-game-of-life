import tkinter as tk
from tkinter import Scale, Checkbutton, IntVar
from mundo import Mundo
from referencias import terrenos
from config import (
    largura_janela,
    altura_janela,
    tamanho_minimo_mapa,
    tamanho_maximo_mapa,
    proporcao_barra_lateral,
    microticks_por_tick,
    ticks_por_dia,
    taxa_att
)

import time

class JanelaApp:
    def __init__(self, janela):
        self.janela = janela
        self.iniciado = False
        self.tempo_inicial = 0
        self.tempo_pausado = 0
        self.tempo_total = 0
        self.tick_atual = 0
        self.microtick_atual = 0
        self.dias_passados = 0

        # Obtenha o tamanho da janela
        largura, altura = largura_janela, altura_janela

        # Calcule a largura da barra lateral com base na proporção
        largura_barra_lateral = largura * proporcao_barra_lateral

        self.janela.geometry(f"{largura}x{altura}")
        self.janela.title("Simulador de Vida")
        self.criar_interface(largura_barra_lateral)

    def criar_interface(self, largura_barra_lateral):
        largura_barra_lateral = largura_janela * proporcao_barra_lateral
        # Crie o frame da barra lateral
        self.barra_lateral = tk.Frame(self.janela, width=largura_barra_lateral, height=altura_janela, bg="lightgray")
        self.barra_lateral.grid(row=0, column=0, rowspan=2)

        self.botao_iniciar = tk.Button(self.barra_lateral, text="Iniciar", command=self.alternar_iniciar_pausar)
        self.botao_iniciar.pack(side="bottom", pady=20)

        # Crie o Canvas como um quadrado com o lado igual à altura da janela
        self.canvas = tk.Canvas(self.janela, width=altura_janela, height=altura_janela, bg="white")
        self.canvas.grid(row=0, column=1)
    
        # Crie um slider para definir o tamanho do mundo
        self.tamanho_mundo_label = tk.Label(self.barra_lateral, text="Tamanho do Mundo:")
        self.tamanho_mundo_label.pack()

        self.tamanho_mundo_slider = Scale(self.barra_lateral, from_=tamanho_minimo_mapa, to=tamanho_maximo_mapa, orient="horizontal", length=largura_barra_lateral, resolution=altura_janela/30, showvalue=1)
        self.tamanho_mundo_slider.set(30)  # Valor inicial
        self.tamanho_mundo_slider.pack()
        
        # Crie os campos de entrada para os parâmetros
        self.scale_label = tk.Label(self.barra_lateral, text="Scale:")
        self.scale_label.pack()
        self.scale_entry = tk.Entry(self.barra_lateral)
        self.scale_entry.insert(0, "100.0")  # Valor padrão
        self.scale_entry.pack()

        self.octaves_label = tk.Label(self.barra_lateral, text="Octaves:")
        self.octaves_label.pack()
        self.octaves_entry = tk.Entry(self.barra_lateral)
        self.octaves_entry.insert(0, "6")  # Valor padrão
        self.octaves_entry.pack()

        self.persistence_label = tk.Label(self.barra_lateral, text="Persistence:")
        self.persistence_label.pack()
        self.persistence_entry = tk.Entry(self.barra_lateral)
        self.persistence_entry.insert(0, "0.5")  # Valor padrão
        self.persistence_entry.pack()

        self.lacunarity_label = tk.Label(self.barra_lateral, text="Lacunarity:")
        self.lacunarity_label.pack()
        self.lacunarity_entry = tk.Entry(self.barra_lateral)
        self.lacunarity_entry.insert(0, "2.0")  # Valor padrão
        self.lacunarity_entry.pack()

        self.min_value_label = tk.Label(self.barra_lateral, text="Min Value:")
        self.min_value_label.pack()
        self.min_value_entry = tk.Entry(self.barra_lateral)
        self.min_value_entry.insert(0, "-1.0")  # Valor padrão
        self.min_value_entry.pack()

        self.max_value_label = tk.Label(self.barra_lateral, text="Max Value:")
        self.max_value_label.pack()
        self.max_value_entry = tk.Entry(self.barra_lateral)
        self.max_value_entry.insert(0, "1.0")  # Valor padrão
        self.max_value_entry.pack()
        
        # Adicione a Checkbox para definir o contorno
        self.checkbox_contorno_var = tk.IntVar()
        self.checkbox_contorno = tk.Checkbutton(self.barra_lateral, text="Exibir Grid", variable=self.checkbox_contorno_var)
        self.checkbox_contorno.pack()
        
        # Crie o botão 'Gerar Terreno' na barra lateral
        self.botao_gerar_terreno = tk.Button(self.barra_lateral, text="Gerar Terreno", command=self.gerar_terreno)
        self.botao_gerar_terreno.pack(side="top", padx=20)
        
        # Crie os rótulos para os contadores
        self.label_tempo = tk.Label(self.barra_lateral, text="Tempo Decorrido: 00:00:00")
        self.label_contadores = tk.Label(self.barra_lateral, text="Dia 1 | 0.0")
        
        # Adicione os rótulos à barra lateral
        self.label_tempo.pack()
        self.label_contadores.pack()

    def iniciar_simulador(self):
        # Adicione a lógica para iniciar o simulador aqui
        pass

    def gerar_terreno(self):
        # Obtenha o tamanho do mundo do slider
        tamanho_mundo = int(self.tamanho_mundo_slider.get())
        
        # Verifique se a Checkbox de contorno está marcada
        exibir_contorno = self.checkbox_contorno_var.get() == 1
        
        # Obtenha os valores dos parâmetros da entrada do usuário
        scale = float(self.scale_entry.get())
        octaves = int(self.octaves_entry.get())
        persistence = float(self.persistence_entry.get())
        lacunarity = float(self.lacunarity_entry.get())
        min_value = float(self.min_value_entry.get())
        max_value = float(self.max_value_entry.get())

        # Crie uma instância de Mundo com o tamanho escolhido
        mundo = Mundo(tamanho_mundo, tamanho_mundo)
        
        # Chame o método para gerar o terreno com base nos parâmetros
        mundo.gerar_terrenos_base(scale, octaves, persistence, lacunarity, min_value, max_value)

        # Limpe o canvas para remover desenhos anteriores
        self.canvas.delete("all")

        # Calcula o tamanho do quadrado com base no tamanho do mundo
        tamanho_quadrado = altura_janela / tamanho_mundo

        # Percorra todos os lugares do mundo
        for y in range(tamanho_mundo):
            for x in range(tamanho_mundo):
                lugar = mundo.obter_lugar(x, y)
                tipo_terreno = lugar.terreno
                cor = terrenos[tipo_terreno]["cor"]

                # Calcule as coordenadas do retângulo
                x1 = x * tamanho_quadrado
                y1 = y * tamanho_quadrado
                x2 = (x + 1) * tamanho_quadrado
                y2 = (y + 1) * tamanho_quadrado

                # Se a Checkbox de contorno estiver marcada, desenhe o retângulo com outline
                if exibir_contorno:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill=cor, outline="gray50")
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill=cor, outline="")

    def alternar_iniciar_pausar(self):
        if self.iniciado:
            # Pausar
            self.iniciado = False
            self.botao_iniciar.config(text="Iniciar")
            # Chame o método na instância de ControleJanela
            self.iniciar_tempo(False)
        else:
            # Iniciar
            self.iniciado = True
            self.botao_iniciar.config(text="Pausar")
            # Chame o método na instância de ControleJanela
            self.iniciar_tempo(True)

    def atualizar_contadores_continuamente(self):
        # Atualize os contadores aqui
        self.atualizar_contadores()

        # Chame a função update para atualizar a interface
        self.janela.update()

        # Agende a próxima chamada para continuar atualizando os contadores
        self.janela.after(taxa_att, self.atualizar_contadores_continuamente)

    def iniciar(self):
        self.janela.mainloop()
        
    def iniciar_tempo(self, iniciar):
        if iniciar:
            self.iniciado = True
            self.atualizar_contadores_continuamente()
        else:
            self.iniciado = False
            
    def pausar_tempo(self):
        if self.iniciado:
            self.tempo_pausado = time.time() - self.tempo_inicial
            self.iniciado = False
    
    def continuar_tempo(self):
        if not self.iniciado:
            self.iniciado = True
            self.tempo_inicial = time.time() - self.tempo_pausado
            
    def atualizar_contadores(self):
        if self.iniciado:
            self.tempo_decorrido = time.time() - self.tempo_inicial
            self.microticks_decorridos = int(self.tempo_decorrido * microticks_por_tick)
            self.ticks_decorridos = self.microticks_decorridos // microticks_por_tick
            self.microtick_atual = self.microticks_decorridos % microticks_por_tick
            self.dias_passados = self.ticks_decorridos // ticks_por_dia
            segundos = int(self.tempo_decorrido)
            minutos, segundos = divmod(segundos, 60)
            horas, minutos = divmod(minutos, 60)
            tempo_formatado = f"{horas:02d}:{minutos:02d}:{segundos:02d}"
            contadores = f"Dia {self.dias_passados} | {self.ticks_decorridos}.{self.microtick_atual}"
            self.label_tempo.config(text=f"Tempo Decorrido: {tempo_formatado}")
            self.label_contadores.config(text=contadores)
    
if __name__ == "__main__":
    janela = JanelaApp(tk.Tk())
    janela.iniciar()