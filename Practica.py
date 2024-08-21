'''
escribir todo lo que quiero
'''
num1=int(input("Ingresar un numero :"))
num2=int(input("Ingresar otro numero :"))

suma =  num1+num2
producto = num1 * num2

print("la suma es :" ,suma)
print("el producto es :" ,producto)

#Ejercicio 2 
#Dar numeracion del 10 al 40

x=10
while x<=40:
    print(x)
    x=x+1

#Ejercicio 3
#lo mismo de arriba pero con for
for x in range(10, 41, 2):
    print(x)

#Para que se diviertan!!
#pedir 10 veces ingresar un numero
#entero y dar el producto

producto=1

for x in range(10):
    num = int(input("Ingrese un numero:"))
    producto=producto*num

print("El producto es :" ,producto)

#Ejercicio level Intermedio eso creo !!
#Ingresar 15 notas del 0 al 20
# si es >10 aprobado, caso contrario
#desaprobado, mostrar cuantos son aprobados
#y cuantos son desaprobados

aprobado= 0
desaprobado = 0
for x in range(15):
    nota = int(input("Ingresar notas"))
    if nota>10:
        aprobado=aprobado+1
    else:
        desaprobado=desaprobado+1

print("Los aprobados son:" ,aprobado)
print("los desprobados son:" ,desaprobado)

#El mismo ejercicio , solo que ahora no
#sera 15, sino que le diras al usuario
#que ingrese un numero en cantidades de notas

aprobado = 0
desaprobado = 0

n=int(input("Cuantas notas se ingresaran? :"))
for x in range(n):
    nota=int(input("Ingresar notas :"))
    if nota>10:
        aprobado=aprobado+1
    else:
        desaprobado=desaprobado+1

print("Los aprobados son:" ,aprobado)
print("los desprobados son:" ,desaprobado)
