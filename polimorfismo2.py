# Clase padre
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def info(self):
        return f"Vehículo: {self.marca} {self.modelo}"

# Clase herencia para vehículos terrestres
class Terrestre(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo  # Tipo de vehículo terrestre (ej: coche, camión)

    def info(self):
        return f"Vehículo Terrestre: {self.marca} {self.modelo}, Tipo: {self.tipo}"

# Clase herencia para vehículos acuáticos
class Acuatico(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo  # Tipo de vehículo acuático (ej: barco, submarino)

    def info(self):
        return f"Vehículo Acuático: {self.marca} {self.modelo}, Tipo: {self.tipo}"

# Clase herencia para vehículos aéreos
class Aereo(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo  # Tipo de vehículo aéreo (ej: avión, helicóptero)

    def info(self):
        return f"Vehículo Aéreo: {self.marca} {self.modelo}, Tipo: {self.tipo}"

# Ejemplo de uso
def mostrar_info(vehiculos):
    for vehiculo in vehiculos:
        print(vehiculo.info())

# Creación de instancias de diferentes tipos de vehículos
vehiculos = [
    Terrestre("Toyota", "Auris", "Coche"),
    Acuatico("Maggazu", "MX-14 CLASSIC", "Barco"),
    Aereo("Boeing", "777", "Avión")
]

# Mostrar información de todos los vehículos
mostrar_info(vehiculos)