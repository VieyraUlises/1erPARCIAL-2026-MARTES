#Ejercicio 9
#Mismo codigo que Ejercicio 7 hasta linea 40
#Lo hice asi porque from Ejercicio7 import Comic me daba error
from datetime import date

class Comic:
    def __init__(self, titulo: str, id_comic: int, fecha_publicacion: date, precio: float, stock: int):
        self.titulo: str = titulo
        self.id_comic: int = id_comic
        self.fecha_publicacion: date = fecha_publicacion
        self.precio: float = precio
        self.stock: int = stock

    def modificar_datos(self, titulo=None, precio=None, stock=None):
        if titulo is not None:
            self.titulo = titulo
        if precio is not None:
            self.precio = precio
        if stock is not None:
            self.stock = stock

    def dias_desde_publicacion(self, fecha_referencia):
        if self.fecha_publicacion < fecha_referencia:
            print(f"El cómic '{self.titulo}' es más antiguo que la fecha de referencia.")
            self.stock = 0
            return None
        else:
            diferencia = (self.fecha_publicacion - fecha_referencia).days
            return diferencia

    def __str__(self):
        return f"Comic: {self.titulo} | ID: {self.id_comic} | Precio: ${self.precio:.2f} | Stock: {self.stock}"

    def __eq__(self, other):
        if isinstance(other, Comic):
            return self.id_comic == other.id_comic and self.titulo == other.titulo
        return False

# nueva clase Ejercicio 9:

class TiendaComics:
    def __init__(self):
        self.secciones = {
            "DC Comics": [],
            "Marvel": [],
            "Independientes": []
        }

    def agregar_comic(self, seccion, comic: Comic):
        if seccion in self.secciones:
            self.secciones[seccion].append(comic)
        else:
            print(f"La sección '{seccion}' no existe.")

    def remover_comic(self, seccion, id_comic):
        if seccion in self.secciones:
            self.secciones[seccion] = [c for c in self.secciones[seccion] if c.id_comic != id_comic]
        else:
            print(f"La sección '{seccion}' no existe.")

    def actualizar_stock(self, seccion, id_comic, nuevo_stock):
        if seccion in self.secciones:
            for c in self.secciones[seccion]:
                if c.id_comic == id_comic:
                    c.stock = nuevo_stock
                    return
            print("Comic no encontrado en la sección.")
        else:
            print(f"La sección '{seccion}' no existe.")

    def remover_stock_critico(self):
        for seccion, lista in self.secciones.items():
            self.secciones[seccion] = [c for c in lista if c.stock > 3]

            