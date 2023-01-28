# Universidad Tecnológica de Tijuana
# Ingeniería en Mecatrónica
# Club de Programación
# Ernesto Rodríguez Corona
# Kenia Angulo Varela
# Juan de Dios Villa Carbajal
# Jesús Alfonso Rodríguez
# Ejercicio 5

precioMetro = 0 #Ustedes pondrán el precio del metro
cantidadPintura = 0
cobroFinal = 0
print ("Ingresa cuantos m2 se van a pintar: ", end = "")
cantidadPintura = int (input())
cobroFinal = cantidadPintura * precioMetro
print ("Por " + str(cantidadPintura) + " m2, el total es de " + str(cobroFinal) + " $ MXN")
