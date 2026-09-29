#Ejercicio 3:
class Biblioteca:
    def __init__(self):
        self.libros = [] # Creo una lista vacia para almacenar los libros

    def esta_vacia(self):
        return len(self.libros) == 0 # Si la lista esta vacia, retorna True

    def agregar_libro(self, libro):
        self.libros.append(libro) # Agrega un libro a la lista

    def remover_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro) # Remueve un libro (si existe)
        else:
            print("El libro no está en la biblioteca")

#nuevos metodos:
    def leer_primer_libro(self):
        if not self.esta_vacia():
            return self.libros[0]
        return None

    def leer_ultimo_libro(self):
        if not self.esta_vacia():
            return self.libros[-1]
        return None

    def insertar_al_principio(self, libro):
        self.libros.insert(0, libro)

    def agregar_al_final(self, libro):
        self.libros.append(libro)

