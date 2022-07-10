from types import NoneType
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

def getTitulo(url):
    try:
        html = urlopen(url)
    except HTTPError as erro:
        print("Ocorreu um erro HTTP: {erro}")
        return None
    except URLError as erro:
        print("Ocorreu um erro de URL: {erro}")
        return None
    except:
        print("Ocorreu um erro na página.: {erro}")
        return None

    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        titulo = bsObj.body.h1
    except AttributeError as erro:
        print("Ocorreu um erro ao acessar a tag h1: {erro}")
        return None

    return titulo

titulo = getTitulo(input("Informe a url completa:"))

if titulo is not None:
    print(titulo)
else:
    print("Titulo não encontrado.")





