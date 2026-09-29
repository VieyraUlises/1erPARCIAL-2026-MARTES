# Ejercicio 7:
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