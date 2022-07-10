from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.bcb.gov.br/estabilidadefinanceira/buscanormas?tipoDocumento=Todos")
bsObj = BeautifulSoup(html.read(), "html.parser")

print(bsObj.title)