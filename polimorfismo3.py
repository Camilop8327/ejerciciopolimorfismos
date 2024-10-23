class Punto:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, otro):
        return Punto(self.x - otro.x, self.y - otro.y, self.z - otro.z)

    def __repr__(self):
        return f"Punto({self.x}, {self.y}, {self.z})"

# Ejemplo
p1 = Punto(4, 6, 8)
p2 = Punto(3, 5, 7)
resultado = p1 - p2
print(resultado)  # Salida: Punto(2, 3, 4)