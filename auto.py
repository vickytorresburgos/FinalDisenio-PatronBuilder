class Auto:
    def __init__(self):
        self.marca = None
        self.modelo = None

    def __str__(self):
        return f"Auto: {self.marca} {self.modelo}"