from typing_extensions import override
from auto_builder import AutoBuilder
from auto import Auto

class FordBuilder(AutoBuilder):
    def set_marca(self):
        self.auto.marca = "Ford"
        print(f"Construyendo auto marca: {self.auto.marca}")

    
    def set_modelo(self):
        self.auto.modelo = "Fiesta"
        print(f"Construyendo auto modelo: {self.auto.modelo}")

    