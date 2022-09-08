
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

chequearprimo = int(input("Ingrese un numero a verificar su primalidad: "))

def numeroprimo():
    if chequearprimo > 1:
        
        for i in range(2,int(chequearprimo)):
            if (chequearprimo % i) == 0:
                print(f"El numero{chequearprimo} no es primo")
                break
        else:
            print(f"El numero {chequearprimo} es primo")
    else: ("Ingrese un numero mayor a 1")            
                
   
            
        

       



print(numeroprimo())
print (f"El area de un triangulo es {areatriangulo(alturatriangulo,basetriangulo)}")
print (f"El Area de un circulo es {areacirculo(radiocirculo)}")