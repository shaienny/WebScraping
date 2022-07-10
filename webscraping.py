from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

html = urlopen("https://www.bcb.gov.br/estabilidadefinanceira/buscanormas?tipoDocumento=Todos")
bsObj = BeautifulSoup(html.read(), "html.parser")

for link in bsObj.find_all("a"):
    print(link.get("href"))