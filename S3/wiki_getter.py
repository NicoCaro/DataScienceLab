'''Wiki intro getter:
   
   Este modulo proporciona 2 funciones:

   wiki_intro_getter: Permite obtener la intro de un articulo de wikipedia.
   to_txt: Permite guardar un texto archivo txt en la carpeta de trabajo actual. 

Autor: NicoCaro
'''

import requests
import re
from lxml import html
from functools import reduce

print('Cargando módulo Wiki intro getter')


def wiki_intro_getter(page='https://en.wikipedia.org/wiki/Computer_file'):
    '''Recibe una pagina de wikipedia y entrega su intro en texto.
    
    Recibe una página de Wikipedia, accede a su contenido por medio 
    de una get request y transforma su introduccion a texto plano.
    
    Args:
    
        page : Dirección https al articulo de wikipedia
    
    Returns:
    
        texto del articulo en formato string.
    '''
    '''
    Usa expresiones regulares para extraer el articulo:
    1. Busca por posibles mayusculas : [A-Z]?
    2. Posteriormente, busca por posibles minusculas : [a-z]?
    3. Luego busca posibles caracteres especiales: .?
    4. Repite los pasos 1 y 2: [A-Z]?[a-z]?
    5. Hace la busqueda tantas veces como sea necesario:
       ([A-Z]?[a-z]?.?[A-Z]?[a-z]?)*
    '''
    x = re.search(r"wiki/([A-Z]?[a-z]?.?[A-Z]?[a-z]?)*", page)

    # Obtiene el articulo extraido
    request_page = page[x.span()[0]:x.span()[1]]
    request_page = request_page.replace(
        'wiki/',
        '',
    )

    # Se comunica con la API de wikipedia
    response = requests.get('https://en.wikipedia.org/w/api.php',
                            params={
                                'action': 'parse',
                                'page': request_page,
                                'format': 'json',
                            }).json()

    # Obtiene la respuesta como un archivo html puro
    raw_html = response['parse']['text']['*']
    document = html.document_fromstring(raw_html)

    # Obtiene la introduccion
    first_p = document.xpath('//p')[0]
    return first_p.text_content()


def to_txt(text, name=None):
    ''' Guarda un texto con el nombre name en formato txt.
    
    Toma un string de Python y lo almacena en el directorio de trabajo 
    actual. Si el nombre no es proporcionado, construye uno a partir
    de las tres primeas palabras en el texto.
    
    Args:
        text: string de Python.
    
    Return:
        None, se guarda u archivo de texto en la carpeta de trabajo actual.
    '''
    
    # Define la funcion que guarda el archivo
    def write_file(name, text):
        print('Guardando archivo ...')
        file = open(name + '.txt', 'w')
        file.write(text)
        file.close()
        print('Archivo guardado con el nombre: ', name +'.txt')

    '''
    Si hay un nombre definido, lo guarda de inmediato, en caso contrario 
    intenta construir un nombre con las primeras 3 palabras del texto.
    '''
    if name:
        write_file(name, text)
    else:
        try:
            splitd = text.split()[0:4]
            name = reduce(lambda x, y: x + '_' + y, splitd)

        except:
            print('Titulo por defecto, no hay suficientes palabras!')
            name = 'default'

        finally:
            write_file(name, text)
