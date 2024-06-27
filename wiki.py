import requests 
from lxml import html
encabezado = { 
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Safari/537.36",
    
}
url = "https://www.wikipedia.org/"

respuesta = requests.get(url,headers =encabezado)

#print(respuesta.text)

parser = html.fromstring(respuesta.text)

#español = parser.get_element_by_id("js-link-box-es")
#print(español.text_content())

#español = parser.xpath("//a[@id='js-link-box-es']/strong/text()")
#print(español)

idiomas = parser.xpath("//div[contains(@class,'central-featured-lang')]//strong/text()")

for idioma in idiomas:
    print(idioma)