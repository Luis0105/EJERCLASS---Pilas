class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

# Ejemplo de uso: invertir una lista
def invertir_lista(lista):
    pila = Pila()
    for elemento in lista:
        pila.apilar(elemento)
    lista_invertida = []
    while not pila.esta_vacia():
        lista_invertida.append(pila.desapilar())
    return lista_invertida

# Prueba
mi_lista = [1, 2, 3, 4, 5]
lista_invertida = invertir_lista(mi_lista)
print(lista_invertida)  # Salida: [5, 4, 3, 2, 1]