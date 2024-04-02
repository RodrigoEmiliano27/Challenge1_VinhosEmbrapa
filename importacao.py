class importacao:
    def __init__(self, pais, quantidade,valor,ano,tipo):
        self.pais = pais
        self.quantidade = quantidade
        self.valor = valor
        self.ano = ano
        self.tipo=tipo  

    
    def addSubcategoria(self,subcategoria,total):
        self.subcategoria[subcategoria]=total

    
    def serialize(self):
        return {
            'pais': self.pais, 
            'quantidade': self.quantidade,
            'valor': self.valor,
            'ano': self.ano,
            'tipo': self.tipo
        }
    