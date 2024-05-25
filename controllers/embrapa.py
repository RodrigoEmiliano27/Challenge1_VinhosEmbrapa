import requests
from bs4 import BeautifulSoup
from models import vinho
from models import uva
from controllers import Comercializacao
from models import importacao   
from utils import processaQuantidade,getTipoProcessamento,getTipoImportacao



baseUrl = 'http://vitibrasil.cnpuv.embrapa.br/index.php?'
producaoOption='opcao=opt_02'
processamentoOption='opcao=opt_03'
comercializacaoOption='opcao=opt_04'
importacaoOption='opcao=opt_05'
exportacaoOption='opcao=opt_06'

class Embrapa():

    def getHtmlPage(self,option):
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


        
    def VerificarTipoUva(self,tipo):
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

    def VerificarTipoComercializacao(self,tipo):
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
        
    def processaRawDataProcessamento(self,rawData,ano,tipo):
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
                    if(self.VerificarTipoUva(rawData[contador][0])):
                        if rawData[contador][0] != categoriaAnalisada:
                            if _uva is not None:
                                dados.append(_uva)
                            categoriaAnalisada=rawData[contador][0]
                            _uva = uva(categoriaAnalisada,getTipoProcessamento(tipo),processaQuantidade(rawData[contador][1]),ano)

                    elif rawData[contador][0].upper() !='TOTAL':
                        _uva.addSubcategoria(rawData[contador][0],processaQuantidade(rawData[contador][1]))
            contador+=1
        return dados
    
    def processamentoRawDataComercializacao(self, rawData,ano):
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
                        if(self.VerificarTipoComercializacao(rawData[contador][0])):
                            if rawData[contador][0] != categoriaAnalisada:
                                if _comercializacao is not None:
                                    dados.append(_comercializacao)
                                categoriaAnalisada=rawData[contador][0]
                                _comercializacao = Comercializacao(categoriaAnalisada,processaQuantidade(rawData[contador][1]),ano)

                        elif rawData[contador][0].upper() !='TOTAL':
                            _comercializacao.addSubcategoria(rawData[contador][0],processaQuantidade(rawData[contador][1]))

                            
                
                contador+=1

            if _comercializacao is not None:
                dados.append(_comercializacao)
            
            return dados


    def processaRawDataProducao(self,rawData,ano):
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

    def processaRawDataImportacao(self,rawData,ano,tipo):
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
        


    def getProductionDados(self,ano):
        option = producaoOption+f'&ano={ano}'
        rawData = self.getHtmlPage(option)
        processedData = self.processaRawDataProducao(rawData,ano)   
        return processedData

    def getProcessamentoDados(self,ano,tipo):
        option = processamentoOption+f'&ano={ano}&subopcao=subopt_0{tipo}'
        rawData = self.getHtmlPage(option)
        processedData = self.processaRawDataProcessamento(rawData,ano,tipo)   
        return processedData

    def getComercializacaoDados(self,ano):
        option = comercializacaoOption+f'&ano={ano}'
        rawData = self.getHtmlPage(option)
        processedData = self.processamentoRawDataComercializacao(rawData,ano)   
        return processedData

    def getImportacaoDados(self,ano,tipo):
        option = importacaoOption+f'&ano={ano}&subopcao=subopt_0{tipo}'
        rawData = self.getHtmlPage(option)
        processedData = self.processaRawDataImportacao(rawData,ano,tipo)   
        return processedData

    def getExportacaoDados(self,ano,tipo):
        option = exportacaoOption+f'&ano={ano}&subopcao=subopt_0{tipo}'
        rawData = self.getHtmlPage(option)
        processedData = self.processaRawDataImportacao(rawData,ano,tipo)   
        return processedData











