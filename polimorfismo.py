def sumar(x, y):
    if isinstance(x, list) and isinstance(y, (int, float)):
        return sum(x) + y  # Suma todos los elementos de la lista y luego añade el número
    elif isinstance(y, list) and isinstance(x, (int, float)):
        return x + sum(y)  # Suma el número y todos los elementos de la lista
    elif isinstance(x, str) or isinstance(y, str):
        return str(x) + str(y)  # Convierte ambos a cadena y concatena
    else:
        return x + y  # Suma numérica

# Ejemplo de uso
print(sumar(20, 30))  # Salida: 50
print(sumar("Días", 20))  # Salida: "Días20"
print(sumar([20, 30, 56, 70], 70))  # Salida: 176 (20 + 30 + 56 + 70 + 70)
print(sumar(70, [20, 30, 56, 70]))  # Salida: 176 (70 + 20 + 30 + 56 + 70)