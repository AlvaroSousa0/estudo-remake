import requests
from bs4 import BeautifulSoup


url = 'https://pt.stackoverflow.com/questions/tagged/python'
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

for pergunta in html.select('.js-post-summary'):
    titulo = pergunta.select_one('.s-link')
    data = pergunta.select_one('.relativetime')
    votos = pergunta.select_one('.s-post-summary--stats-item-number')

    print(data.text, titulo.text, votos.text, sep='\t')


# Estudo de web Scraping adiado --> Notebook péssimo