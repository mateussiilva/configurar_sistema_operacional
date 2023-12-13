#!/usr/bin/env python3

import sys
import shutil
import os
from os.path import isfile, join, splitext, exists, isdir, split


NOME_PASTAS = {
    "ArquivosDebian": ("deb",),
    "ArquivosPDF": ("pdf",),
    "Musicas": ("mp3", "wav"),
    "ArquivosFontes": ("gz", "xz"),
    "ArquivosTorrents": ("torrent",),

}


def pegar_extensao(caminho_arquivo: str) -> str:
    return splitext(caminho_arquivo)[1].strip(".").lower()


def extensoes_identificadas(lista_arquivos):
    for arquivo in lista_arquivos:
        print(pegar_extensao(arquivo))


def pasta_existe(caminho_pasta: str) -> bool:
    if exists(caminho_pasta) and isdir(caminho_pasta):
        return True
    return False


def criar_pasta(root, nome_pasta):
    caminho_pasta = join(root, nome_pasta)
    if pasta_existe(caminho_pasta) == False:
        os.mkdir(caminho_pasta)
        print("Vou criar a pasta: %s" % caminho_pasta)
    # print("Pasta Já existe")


def listar_arquivos(caminho: str) -> list:
    return list(map(lambda f: join(caminho, f), filter(lambda p: isfile(join(caminho, p)) and ".py" not in p, os.listdir(caminho))))


if __name__ == "__main__":
    caminho = join(os.getenv("HOME"), "Downloads")
    for pasta in NOME_PASTAS:
        criar_pasta(caminho, pasta)
    lista_arquivos = listar_arquivos(caminho)
    for arquivo in lista_arquivos:
        extensao = pegar_extensao(arquivo)

        if extensao in NOME_PASTAS["ArquivosDebian"]:
            caminho_destino = join(caminho, "ArquivosDebian")
            novo_caminho = join(caminho_destino, split(arquivo)[1])
            shutil.move(arquivo, novo_caminho)
        if extensao in NOME_PASTAS["ArquivosFontes"]:
            caminho_destino = join(caminho, "ArquivosFontes")
            novo_caminho = join(caminho_destino, split(arquivo)[1])
            shutil.move(arquivo, novo_caminho)
        if extensao in NOME_PASTAS["ArquivosPDF"]:
            caminho_destino = join(caminho, "ArquivosPDF")
            novo_caminho = join(caminho_destino, split(arquivo)[1])
            shutil.move(arquivo, novo_caminho)

        if extensao in NOME_PASTAS["Musicas"]:
            caminho_destino = join(caminho, "Musicas")
            novo_caminho = join(caminho_destino, split(arquivo)[1])
            shutil.move(arquivo, novo_caminho)

        if extensao in NOME_PASTAS["ArquivosTorrents"]:
            caminho_destino = join(caminho, "ArquivosTorrents")
            novo_caminho = join(caminho_destino, split(arquivo)[1])
            shutil.move(arquivo, novo_caminho)
    # for pasta,extensoes in NOME_PASTAS.items():
    #     print(extensoes)

    # extensoes_identificadas(lista_arquivos)
    # criar_pasta(caminho,tuple(NOME_PASTAS.keys())[0])
    # print(list(NOME_PASTAS.keys()))
