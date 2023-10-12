# Dicionário de Cores
cores = {
    "azul_claro": "#ADD8E6",
    "marrom": "#8B4513",
    "verde_escuro": "#006400",
    "cinza": "#808080",
    "grid": "#00000080"
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
        "cor": cores["marrom"]
    },
    "grama": {
        "passavel": True,
        "cor": cores["verde_escuro"]
    },
    "rocha": {
        "passavel": False,
        "cor": cores["cinza"]
    }
    # Adicione mais tipos de terreno conforme necessário
}