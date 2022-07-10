from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.bcb.gov.br/estabilidadefinanceira/buscanormas?tipoDocumento=Todos")
print (html.read())