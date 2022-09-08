
import math


alturatriangulo =float(input ("Ingrese la altura: "))
basetriangulo= float(input("Ingrese la base:"))


def areatriangulo(a, b):
   a = alturatriangulo 
   b = basetriangulo
   resultado= float(a*b/2)
   return resultado
radiocirculo =float(input("Ingrese el radio del círculo:"))
def areacirculo(a):
    a= radiocirculo
    resultado= math.pi * (a **2)
    return  resultado


print (f"El area de un triangulo es {areatriangulo(alturatriangulo,basetriangulo)}")
print (f"El Area de un circulo es {areacirculo(radiocirculo)}")