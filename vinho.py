
from dataclasses import dataclass
@dataclass
class vinho:
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
            'subcategoria': self.subcategoria,
        }
    

    


