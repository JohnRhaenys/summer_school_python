import os


def criar_pasta(caminho):
    try:
        os.mkdir(caminho)
    except Exception:
        return False
    return True
