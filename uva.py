class uva:
    def __init__(self,tipo, categoria, total,ano):
        self.tipo = tipo
        self.categoria = categoria
        self.total = total
        self.ano = ano
        self.subcategoria = {}

    
    def addSubcategoria(self,subcategoria,total):
        self.subcategoria[subcategoria]=total

    
    def serialize(self):
        return {
            'tipo': self.tipo,
            'categoria': self.categoria, 
            'ano': self.ano,
            'subcategoria': self.subcategoria,
        }
    

    