import requests
from bs4 import BeautifulSoup
from time import sleep

compra = input('O que deseja cotar? ')

sleep(3)

url_base = 'https://lista.mercadolivre.com.br/'

url = (url_base+compra)

class Buscar():
    
    def get_text(valor_default=compra):
        
        #realizando o get da pagina
        resposta = requests.get(url)
    
        #ativando o BeautifulSoup, para "Arrumar" o codigo HTML
        site = BeautifulSoup(resposta.text, 'html.parser')
    
        #div com o produto
        produtos = site.findAll('div', attrs={'class': 'ui-search-result__wrapper shops__result-wrapper'})

        for produto in produtos:
        
            #titulo do produto, com o nome
            #erro ao imprimir
            titulo = produto.find('h2', attrs={'class': 'ui-search-item__title shops__item-title'})
            
            
            #selecionando apenas o valor em rais
            reais = produto.find('span', attrs={'class': 'price-tag-text-sr-only'})
            #centavos = produto.find('span', attrs={'class': ''})
        
            #selecionando o link em uma variavel(link)
            link = produto.find('a', attrs={'class':'ui-search-link'})
        
            print('Produto:', titulo.text)
            print('Valor do produto: R$',reais.text )
            print('Link da pagina:',link['href'])
            
            print('\n\n')
    
    get_text()
    

Buscar()