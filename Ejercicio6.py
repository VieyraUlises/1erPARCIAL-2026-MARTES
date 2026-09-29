#Ejercicio 6:
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

    def __len__(self):
        return len(self.libros) 

    def __str__(self):
        return f"Biblioteca con {len(self.libros)} libros: {self.libros}"

    def __eq__(self, other):
        if isinstance(other, Biblioteca):
            return self.libros == other.libros
        return False

    def __add__(self, other):
        if isinstance(other, Biblioteca):
            nueva = Biblioteca()
            nueva.libros = self.libros + other.libros
            return nueva
        return NotImplemented

    def contar_libros(biblioteca):
        contador = 0
        for libro in biblioteca.libros:   # recorre la lista de libros
            contador += 1
        return contador

    def contar_libros_recursivo(self, libros=None):
        if libros is None:
            libros = self.libros
        if not libros:
            return 0
        return 1 + self.contar_libros_recursivo(libros[1:])
