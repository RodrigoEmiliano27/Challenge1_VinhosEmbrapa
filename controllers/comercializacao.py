
class Comercializacao:
    def __init__(self, categoria, total,ano):
        self.categoria = categoria
        self.total = total
        self.ano = ano
        self.subcategoria = {}

    
    def addSubcategoria(self,subcategoria,total):
        self.subcategoria[subcategoria]=total

    
    def serialize(self):
        return {
            'categoria': self.categoria, 
            'ano': self.ano,
            'total': self.total,
            'subcategoria': self.subcategoria,
        }
    