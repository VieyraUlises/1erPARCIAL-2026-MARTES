#Ejercicio 1: La serie de potencias de Sheldon.
serie_de_shelton = {1/(3**n) for n in range(10)}
# Solo se imprimen 10 terminos porque los valores dentro de la serie tienden a 0 pero nunca llegan a 0.
print(sorted(serie_de_shelton, reverse=True)) # Asi comienza en 1 y termina en 0