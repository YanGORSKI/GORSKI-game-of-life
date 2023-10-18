import tkinter as tk
from tkinter import Scale, Checkbutton, IntVar
from mundo import Mundo
from referencias import terrenos
from timer_module import Timer
from config import (
    largura_janela,
    altura_janela,
    tamanho_minimo_mapa,
    tamanho_maximo_mapa,
    proporcao_barra_lateral,
    taxa_att
)

class JanelaApp:
    def __init__(self, janela):
        self.janela = janela
        self.iniciado = False
        self.tempo = Timer()


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
        
        # Crie o Canvas como um quadrado com o lado igual à altura da janela
        self.canvas = tk.Canvas(self.janela, width=altura_janela, height=altura_janela, bg="white")
        self.canvas.grid(row=0, column=1)
    
        # Crie um slider para definir o tamanho do mundo
        self.tamanho_mundo_label = tk.Label(self.barra_lateral, text="Tamanho do Mundo:")
        self.tamanho_mundo_label.pack()

        self.tamanho_mundo_slider = Scale(self.barra_lateral, from_=tamanho_minimo_mapa, to=tamanho_maximo_mapa, orient="horizontal", length=largura_barra_lateral, resolution=altura_janela/30, showvalue=1)
        self.tamanho_mundo_slider.set(30)  # Valor inicial
        self.tamanho_mundo_slider.pack()
        
        # Crie o LabelFrame para o grupo "Ruído"
        self.ruido_frame = tk.LabelFrame(self.barra_lateral, text="Ruído", padx=10, pady=10)
        self.ruido_frame.pack(side="left", padx=10)

        self.botao_iniciar = tk.Button(self.barra_lateral, text="Iniciar", command=self.alternar_iniciar_pausar)
        self.botao_iniciar.pack(side="bottom", pady=20)
        
        # Crie os campos de entrada para os parâmetros
        self.scale_label = tk.Label(self.ruido_frame, text="Scale:")
        self.scale_label.pack()
        self.scale_entry = tk.Entry(self.ruido_frame)
        self.scale_entry.insert(0, "100.0")  # Valor padrão
        self.scale_entry.pack()

        self.octaves_label = tk.Label(self.ruido_frame, text="Octaves:")
        self.octaves_label.pack()
        self.octaves_entry = tk.Entry(self.ruido_frame)
        self.octaves_entry.insert(0, "6")  # Valor padrão
        self.octaves_entry.pack()

        self.persistence_label = tk.Label(self.ruido_frame, text="Persistence:")
        self.persistence_label.pack()
        self.persistence_entry = tk.Entry(self.ruido_frame)
        self.persistence_entry.insert(0, "0.5")  # Valor padrão
        self.persistence_entry.pack()

        self.lacunarity_label = tk.Label(self.ruido_frame, text="Lacunarity:")
        self.lacunarity_label.pack()
        self.lacunarity_entry = tk.Entry(self.ruido_frame)
        self.lacunarity_entry.insert(0, "2.0")  # Valor padrão
        self.lacunarity_entry.pack()

        self.min_value_label = tk.Label(self.ruido_frame, text="Min Value:")
        self.min_value_label.pack()
        self.min_value_entry = tk.Entry(self.ruido_frame)
        self.min_value_entry.insert(0, "-1.0")  # Valor padrão
        self.min_value_entry.pack()

        self.max_value_label = tk.Label(self.ruido_frame, text="Max Value:")
        self.max_value_label.pack()
        self.max_value_entry = tk.Entry(self.ruido_frame)
        self.max_value_entry.insert(0, "1.0")  # Valor padrão
        self.max_value_entry.pack()
        
        self.repeatx_label = tk.Label(self.ruido_frame, text="Repeat X:")
        self.repeatx_label.pack()
        self.repeatx_entry = tk.Entry(self.ruido_frame)
        self.repeatx_entry.insert(0, "1024")
        self.repeatx_entry.pack()

        self.repeaty_label = tk.Label(self.ruido_frame, text="Repeat Y:")
        self.repeaty_label.pack()
        self.repeaty_entry = tk.Entry(self.ruido_frame)
        self.repeaty_entry.insert(0, "1024")
        self.repeaty_entry.pack()

        self.base_label = tk.Label(self.ruido_frame, text="Base:")
        self.base_label.pack()
        self.base_entry = tk.Entry(self.ruido_frame)
        self.base_entry.insert(0, "24")
        self.base_entry.pack()
        
        # Crie o LabelFrame para o grupo "Terreno"
        self.terreno_frame = tk.LabelFrame(self.barra_lateral, text="Terreno", padx=10, pady=10)
        self.terreno_frame.pack(side="right", padx=10)
        
        # Crie campos de entrada para os parâmetros de "Terreno" dentro do terreno_frame
        self.altura_agua_label = tk.Label(self.terreno_frame, text="Altura da Água:")
        self.altura_agua_label.pack()
        self.altura_agua_entry = tk.Entry(self.terreno_frame)
        self.altura_agua_entry.insert(0, "0.3")  # Valor padrão
        self.altura_agua_entry.pack()
        
        self.altura_terra_label = tk.Label(self.terreno_frame, text="Altura da Terra:")
        self.altura_terra_label.pack()
        self.altura_terra_entry = tk.Entry(self.terreno_frame)
        self.altura_terra_entry.insert(0, "0.5")  # Valor padrão
        self.altura_terra_entry.pack()
        
        self.altura_grama_label = tk.Label(self.terreno_frame, text="Altura da Grama:")
        self.altura_grama_label.pack()
        self.altura_grama_entry = tk.Entry(self.terreno_frame)
        self.altura_grama_entry.insert(0, "0.8")  # Valor padrão
        self.altura_grama_entry.pack()
        
                
        # Adicione a Checkbox para definir o contorno
        self.checkbox_contorno_var = tk.IntVar()
        self.checkbox_contorno = tk.Checkbutton(self.terreno_frame, text="Exibir Grid", variable=self.checkbox_contorno_var)
        self.checkbox_contorno.pack()
        
        # Crie o botão 'Gerar Terreno' na barra lateral
        self.botao_gerar_terreno = tk.Button(self.terreno_frame, text="Gerar Terreno", command=self.gerar_terreno)
        self.botao_gerar_terreno.pack(side="top", padx=20)
        
        # Crie os rótulos para os contadores
        self.label_tempo = tk.Label(self.barra_lateral, text="Tempo Decorrido: 00:00:00")
        self.label_contadores = tk.Label(self.barra_lateral, text="Dia 1 | 0.0")
        
        # Adicione os rótulos à barra lateral
        self.label_tempo.pack()
        self.label_contadores.pack()
        
        self.atualizar_tempo()

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
        repeatx = int(self.repeatx_entry.get())
        repeaty = int(self.repeaty_entry.get())
        base = int(self.base_entry.get())
        altura_agua = float(self.altura_agua_entry.get())
        altura_terra = float(self.altura_terra_entry.get())
        altura_grama = float(self.altura_grama_entry.get())

        # Crie uma instância de Mundo com o tamanho escolhido
        mundo = Mundo(tamanho_mundo, tamanho_mundo)
        
        # Chame o método para gerar o terreno com base nos parâmetros
        mundo.gerar_terrenos_base(scale,
                                  octaves,
                                  persistence,
                                  lacunarity,
                                  min_value,
                                  max_value,
                                  repeatx,
                                  repeaty,
                                  base,
                                  altura_agua,
                                  altura_terra,
                                  altura_grama)

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
            # PAUSA
            self.botao_iniciar.config(text="Iniciar")
            self.tempo.pausar()
        else:
            # INICIA
            self.botao_iniciar.config(text="Pausar")
            self.tempo.iniciar()
            informacoes_tempo = self.tempo.obter_informacoes_tempo()
            microticks_decorridos = informacoes_tempo['microticks_decorridos']
            self.janela.after(microticks_decorridos, self.atualizar_tempo)  
        self.iniciado = not self.iniciado
            
    def atualizar_tempo(self):
        if self.iniciado:
            # Atualize os rótulos
            self.atualizar_contadores()
            # Agende a próxima atualização após um curto intervalo
            informacoes_tempo = self.tempo.obter_informacoes_tempo()
            microticks_decorridos = informacoes_tempo['microticks_decorridos']
            self.janela.after(microticks_decorridos, self.atualizar_tempo)

    
    def atualizar_contadores(self):
        if self.iniciado:
            # Obtenha informações de tempo do objeto Timer
            informacoes_tempo = self.tempo.obter_informacoes_tempo()
            tempo_decorrido = informacoes_tempo['tempo_decorrido']
            microticks_decorridos = informacoes_tempo['microticks_decorridos']
            ticks_decorridos = informacoes_tempo['ticks_decorridos']
            microtick_atual = informacoes_tempo['microtick_atual']
            dias_passados = informacoes_tempo['dias_passados']

            # Converta o tempo decorrido para horas, minutos e segundos
            segundos = int(tempo_decorrido)
            minutos, segundos = divmod(segundos, 60)
            horas, minutos = divmod(minutos, 60)

            # Formate o tempo em uma string
            tempo_formatado = f"{horas:02d}:{minutos:02d}:{segundos:02d}"

            # Atualize os rótulos com as informações
            contadores = f"Dia {dias_passados} | {ticks_decorridos}.{microtick_atual}"
            self.label_tempo.config(text=f"Tempo Decorrido: {tempo_formatado}")
            self.label_contadores.config(text=contadores)
    
if __name__ == "__main__":
    janela = JanelaApp(tk.Tk())
    janela.iniciar()
