import requests
from xml.etree import ElementTree
import smtplib
from email.message import EmailMessage
from senha import senha
import os

pesquisa = 'brasil'
print('\n>>>>>>>>>>>>>>>>> Extraindo notícias para a string {0}'.format(pesquisa))
url = 'https://news.google.com/rss/search?q='
parametros = '&hl=pt-BR&gl=BR&ceid=BR%3Apt-419'
url_final = url + pesquisa + parametros
response = requests.get(url_final)

if response.status_code == 200:
    
    noticias = ElementTree.fromstring(response.content).find('channel')
    noticias = list(noticias) 
    
    noticias = noticias[8:] 
    
    print('Foram encontrados {0} resultados'.format(len(noticias)))

    with open('noticias.txt', 'w', encoding="utf-8") as arquivo:
        for noticia in noticias:
            titulo = "\nTitulo: " + noticia.findtext('title')
            data = "\nData da Publicação: " + noticia.findtext('pubDate')
            link = "\nLink: " + noticia.findtext('link')
            noticia = "\nCanal: " + noticia.findtext('source')
            noticiass = (f"\n {titulo + data + link + noticia}")
            print(noticiass, file=arquivo)
            print(noticiass)

   

EMAIL_ADDRESS = 'noticiadodiapython@gmail.com'
EMAIL_PASSWORD = senha

# Abrir arquivo com as nptícias
mensagem = open("noticias.txt","r",encoding="utf-8" )

# Corpo do e-mail
msg = EmailMessage()
msg['Subject'] = 'Notícia do dia'
msg['From'] = 'noticiadodiapython'
msg['To'] = 'email@email.com', 'email@email.com', 'email@email.com'
msg.set_content(mensagem.read()) 
mensagem.close() # Fechar arquivo.
os.remove("noticias.txt") # Apagador o arquivo notícias

# Enviar e-mail

with smtplib.SMTP_SSL('smtp.gmail.com' ,465) as smtp:
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)

print('Foram encontrados {0} resultados'.format(len(noticias)))
print('E-mail enviando com sucesso')

