from auto_builder import AutoBuilder

class FiatBuilder(AutoBuilder):
    def set_marca(self):
        self.auto.marca = "Fiat"
        print(f"Construyendo auto marca: {self.auto.marca}")
    
    def set_modelo(self):
        self.auto.modelo = "Cronos"
        print(f"Construyendo auto modelo: {self.auto.modelo}")


