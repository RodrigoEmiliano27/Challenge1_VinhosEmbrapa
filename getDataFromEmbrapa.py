import requests
from bs4 import BeautifulSoup
from vinho import vinho


baseUrl = 'http://vitibrasil.cnpuv.embrapa.br/index.php?'
producaoOption='opcao=opt_02'
processamentoOption='opcao=opt_03'
comercializacaoOption='opcao=opt_04'
importacaoOption='opcao=opt_05'
exportacaoOption='opcao=opt_06'


def getHtmlPage(option):
    # Send an HTTP GET request to the URL
    response = requests.get(baseUrl+option)
    # Parse the HTML response using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find the HTML table on the page
    table = soup.find('table', attrs={'class': 'tb_base tb_dados'})
    # Extract data from the table
    data = []
    for row in table.find_all('tr'):
        row_data = [cell.text for cell in row.find_all('td')]
        data.append(row_data)

    return data

def getProductionDados(ano):
    option = producaoOption+f'&ano={ano}'
    rawData = getHtmlPage(option)
    processedData = processaRawDataMaisculas(rawData,ano)   
    return processedData

def processaQuantidade(rawData):
    number = 0.0
    aux = rawData.strip()
    aux = aux.replace('.','')   

    if rawData=='-':
        return 0.0
    
    try:
        number = float(aux)
    except:
         print(f"Could not convert {aux} to a float.")
    
    return number

    
    
    



def processaRawDataMaisculas(rawData,ano):
    contador=0
    categoriaAnalisada=''
    dados = []
    _vinho=None
    while contador<len(rawData):
        if len(rawData[contador])>0:
            if len(rawData[contador])==2:               
                rawData[contador][0]=rawData[contador][0].strip()    
                rawData[contador][1]=rawData[contador][1].strip() 
                #novas categorias começam com letra maiuscula
                if(rawData[contador][0].isupper()):
                    if rawData[contador][0] != categoriaAnalisada:
                        if _vinho is not None:
                            dados.append(_vinho)
                        categoriaAnalisada=rawData[contador][0]
                        _vinho = vinho(categoriaAnalisada,processaQuantidade(rawData[contador][1]),ano)

                else:
                    _vinho.addSubcategoria(rawData[contador][0],processaQuantidade(rawData[contador][1]))

                    
        
        contador+=1

    if _vinho is not None:
        dados.append(_vinho)
    
    return dados
    

#getProductionDados(2021)











