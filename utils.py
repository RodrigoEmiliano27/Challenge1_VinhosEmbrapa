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

def getTipoProcessamento(tipo):
    if tipo == '1':
        return 'Viníferas'
    elif tipo == '2':
        return 'Americanas e híbridas'
    elif tipo == '3':
        return 'Uvas de mesa'
    elif tipo =='4':
        return 'Sem classificação'
    else:
        return 'erro'
    
def getTipoImportacao(tipo):
    if tipo == '1':
        return 'Vinhos de mesa'
    elif tipo == '2':
        return 'Espumantes'
    elif tipo == '3':
        return 'Uvas frescas'
    elif tipo =='4':
        return 'Suco de uva'
    else:
        return 'erro'
