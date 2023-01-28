# Universidad Tecnológica de Tijuana
# Ingeniería en Mecatrónica
# Club de Programación
# Ernesto Rodríguez Corona
# Kenia Angulo Varela
# Juan de Dios Villa Carbajal
# Jesús Alfonso Rodríguez
# Ejercicio 4

cobroHora = 0 #Ustedes ingresarán el precio
print ("Ingrese el total de horas que utilizo el estacionamiento: ", end="")
horasOcupadas = float (input())
redondeoHoras = round (horasOcupadas + 0.5)
cobroTotal = redondeoHoras * cobroHora
print ("Con " + str(redondeoHoras) + " horas, se realiza un cobro de " + str(cobroTotal) + " $ MXN")
