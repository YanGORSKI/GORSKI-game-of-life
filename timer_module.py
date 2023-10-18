import time
from config import (
    microticks_por_tick,
    ticks_por_dia
)

class Timer:
    def __init__(self):
        self.tempo_inicial = None
        self.tempo_pausado = 0

    def iniciar(self):
        self.tempo_inicial = time.time()

    def pausar(self):
        if self.tempo_inicial:
            self.tempo_pausado = time.time() - self.tempo_inicial
            self.tempo_inicial = None

    def continuar(self):
        if self.tempo_inicial is None:
            self.tempo_inicial = time.time() - self.tempo_pausado

    def tempo_decorrido(self):
        if self.tempo_inicial is not None:
            return time.time() - self.tempo_inicial
        return self.tempo_pausado

    def obter_informacoes_tempo(self):
        tempo_decorrido = self.tempo_decorrido()
        microticks_decorridos = int(tempo_decorrido * microticks_por_tick)
        ticks_decorridos_total = microticks_decorridos // microticks_por_tick
        microtick_atual = microticks_decorridos % microticks_por_tick
        dias_passados = ticks_decorridos_total // ticks_por_dia
        
        # Aqui, fazemos o ajuste para que os ticks sejam zerados a cada dia
        ticks_decorridos = ticks_decorridos_total % ticks_por_dia

        return {
            'tempo_decorrido': tempo_decorrido,
            'microticks_decorridos': microticks_decorridos,
            'ticks_decorridos': ticks_decorridos,  # ticks ajustados
            'microtick_atual': microtick_atual,
            'dias_passados': dias_passados
        }


    def reiniciar(self):
        self.tempo_inicial = time.time()
        self.tempo_pausado = 0
