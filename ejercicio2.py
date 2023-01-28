# Universidad Tecnológica de Tijuana
# Ingeniería en Mecatrónica
# Club de Programación
# Ernesto Rodríguez Corona
# Kenia Angulo Varela
# Juan de Dios Villa Carbajal
# Jesús Alfonso Rodríguez
# Ejercicio 2

precioDolar = 19.37 #Busquen el precio actual del dolar
print ("Ingresa cuántos pesos quieres convertir a dolar: ", end="")
monedaMexicana = float(input())
dolarAmericano = monedaMexicana / precioDolar
print ("Usted puede cambiar " + str(dolarAmericano) + " USD.")