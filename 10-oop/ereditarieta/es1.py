class Veicolo:
    def __init__(self, marca, velocita_max):
        self.marca = marca
        self.velocita_max = velocita_max
    
    def descrivi(self):
        print(f"marca: {self.marca}\nvelocità massima {self.velocita_max}")
    
class Auto(Veicolo):
    def __init__(self, marca, velocita_max):
        super().__init__(marca, velocita_max)
    
    def descrivi(self):
        print(f"auto\nmarca: {self.marca}\nvelocità massima: {self.velocita_max}")

class Moto(Veicolo):
    def __init__(self, marca, velocita_max):
        super().__init__(marca, velocita_max)
        
    def descrivi(self):
        print(f"moto\nmarca: {self.marca}\nvelocità massima: {self.velocita_max}")
        
class Bicicletta(Veicolo):
    def __init__(self, marca, velocita_max):
        super().__init__(marca, velocita_max)
    
    def descrivi(self):
        print(f"bicicletta\nmarca: {self.marca}\nvelocità massima: {self.velocita_max}")