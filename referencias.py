# Configurações de Fonte
fonte_lucidaConsole = "C:/00-DEV/Python Sandbox/game_of_life/app/Resources/lucon.ttf"
tamanho_fonte = 36

# Dicionário de Cores
cores = {
    "branco":       "#FFFFFF",
    "preto":        "#000000",
    "azul_claro":   "#5cdbd5",
    "marrom":       "#8B4513",
    "verde_escuro": "#006400",
    "cinza":        "#808080",
    "cinza_claro":  "#999999",
    "marrom_claro": "#827b56",
    "verde_musgo":  "#597d27",
    "grid":         "#00000080"
    # Adicione mais cores conforme necessário
}

# Dicionário de Tipos de Terreno
terrenos = {
    "agua": {
        "passavel": False,
        "nadavel": True,
        "cor": cores["azul_claro"]
    },
    "terra": {
        "passavel": True,
        "cor": cores["marrom_claro"]
    },
    "grama": {
        "passavel": True,
        "cor": cores["verde_musgo"]
    },
    "rocha": {
        "passavel": False,
        "cor": cores["cinza"]
    }
    # Adicione mais tipos de terreno conforme necessário
}