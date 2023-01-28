# Universidad Tecnológica de Tijuana
# Ingeniería en Mecatrónica
# Club de Programación
# Ernesto Rodríguez Corona
# Kenia Angulo Varela
# Juan de Dios Villa Carbajal
# Jesús Alfonso Rodríguez
# Ejercicio 3

anhoActual = 2023
print ("Ingresa el nombre del aspirante: ", end="")
nombreAspirante = str(input())
print ("Ingresa el anho de nacimiento (Formato aaaa) de " + nombreAspirante + ": ", end="")
anhoAspirante = int (input())
edadAspirante = anhoActual - anhoAspirante
print ("El aspirante " + nombreAspirante + " tiene una edad de " + str(edadAspirante) + " anhos")