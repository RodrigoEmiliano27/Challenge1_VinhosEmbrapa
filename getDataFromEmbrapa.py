import requests
from bs4 import BeautifulSoup
from vinho import vinho
from uva import uva
from comercializacao import comercializacao
from importacao import importacao   
from utils import processaQuantidade,getTipoProcessamento,getTipoImportacao



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


    
def VerificarTipoUva(tipo):
    if tipo =='TINTAS':
        return True
    elif tipo =='BRANCAS E ROSADAS':
        return True
    elif tipo=='Sem classificação':
        return True
    elif tipo=='BRANCAS':
        return True
    else:
        return False

def VerificarTipoComercializacao(tipo):
    if tipo =='VINHO DE MESA':
        return True
    elif tipo =='VINHO FINO DE MESA':
        return True
    elif tipo=='VINHO FRIZANTE':
        return True
    elif tipo=='VINHO ORGÂNICO':
        return True
    elif tipo=='VINHO ESPECIAL':
        return True
    elif tipo=='ESPUMANTES':
        return True
    elif tipo=='SUCO DE UVAS':
        return True
    elif tipo=='SUCO DE UVAS CONCENTRADO':
        return True
    elif tipo=='OUTROS PRODUTOS COMERCIALIZADOS':
        return True
    else:
        return False
    
def processaRawDataProcessamento(rawData,ano,tipo):
    contador=0
    categoriaAnalisada=''
    dados = []
    _uva=None
    while contador<len(rawData):
        if len(rawData[contador])>0:
            if len(rawData[contador])==2:               
                rawData[contador][0]=rawData[contador][0].strip()    
                rawData[contador][1]=rawData[contador][1].strip() 
                #novas categorias começam com letra maiuscula
                if(VerificarTipoUva(rawData[contador][0])):
                    if rawData[contador][0] != categoriaAnalisada:
                        if _uva is not None:
                            dados.append(_uva)
                        categoriaAnalisada=rawData[contador][0]
                        _uva = uva(categoriaAnalisada,getTipoProcessamento(tipo),processaQuantidade(rawData[contador][1]),ano)

                elif rawData[contador][0].upper() !='TOTAL':
                    _uva.addSubcategoria(rawData[contador][0],processaQuantidade(rawData[contador][1]))
    
def processamentoRawDataComercializacao(rawData,ano):
        contador=0
        categoriaAnalisada=''
        dados = []
        _comercializacao=None
        while contador<len(rawData):
            if len(rawData[contador])>0:
                if len(rawData[contador])==2:               
                    rawData[contador][0]=rawData[contador][0].strip()    
                    rawData[contador][1]=rawData[contador][1].strip() 
                    #novas categorias começam com letra maiuscula
                    if(VerificarTipoComercializacao(rawData[contador][0])):
                        if rawData[contador][0] != categoriaAnalisada:
                            if _comercializacao is not None:
                                dados.append(_comercializacao)
                            categoriaAnalisada=rawData[contador][0]
                            _comercializacao = comercializacao(categoriaAnalisada,processaQuantidade(rawData[contador][1]),ano)

                    elif rawData[contador][0].upper() !='TOTAL':
                        _comercializacao.addSubcategoria(rawData[contador][0],processaQuantidade(rawData[contador][1]))

                        
            
            contador+=1

        if _comercializacao is not None:
            dados.append(_comercializacao)
        
        return dados


def processaRawDataProducao(rawData,ano):
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

                elif rawData[contador][0].upper() !='TOTAL':
                    _vinho.addSubcategoria(rawData[contador][0],processaQuantidade(rawData[contador][1]))

                    
        
        contador+=1

    if _vinho is not None:
        dados.append(_vinho)
    
    return dados

def processaRawDataImportacao(rawData,ano,tipo):
    contador=0
    dados = []
    while contador<len(rawData):
        if len(rawData[contador])>0:
            if len(rawData[contador])==3:               
                rawData[contador][0]=rawData[contador][0].strip()    
                rawData[contador][1]=rawData[contador][1].strip() 
                rawData[contador][2]=rawData[contador][2].strip() 
                #novas categorias começam com letra maiuscula
                if(rawData[contador][0].upper()!='TOTAL'):
                    _importacao = importacao(rawData[contador][0],processaQuantidade(rawData[contador][1]),
                                                 processaQuantidade(rawData[contador][2]),ano,getTipoImportacao(tipo))
                    
                    dados.append(_importacao)

                    
        
        contador+=1

    return dados
    

#getProductionDados(2021)

def getProductionDados(ano):
    option = producaoOption+f'&ano={ano}'
    rawData = getHtmlPage(option)
    processedData = processaRawDataProducao(rawData,ano)   
    return processedData

def getProcessamentoDados(ano,tipo):
    option = processamentoOption+f'&ano={ano}&subopcao=subopt_0{tipo}'
    rawData = getHtmlPage(option)
    processedData = processaRawDataProcessamento(rawData,ano,tipo)   
    return processedData

def getComercializacaoDados(ano):
    option = comercializacaoOption+f'&ano={ano}'
    rawData = getHtmlPage(option)
    processedData = processamentoRawDataComercializacao(rawData,ano)   
    return processedData

def getImportacaoDados(ano,tipo):
    option = importacaoOption+f'&ano={ano}&subopcao=subopt_0{tipo}'
    rawData = getHtmlPage(option)
    processedData = processaRawDataImportacao(rawData,ano,tipo)   
    return processedData











