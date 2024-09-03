
num1 =int(input("Ingresa un numero"))
num2 =int(input("Ingresa el segundo numero"))

def suma(num1 , num2):
    sumar= (num1 + num2)
    print("la suma es :", sumar)
    return sumar
   
def resta(num1 , num2):
    diferencia = (num1 - num2)
    print("la diferencia es :", diferencia)
    return diferencia
   
def division(num1 , num2):
    if num2 == 0:
        print("Error no se puede dividir por cero")
        return None
    dividiendo= (num1 / num2)
    print("la division es :", dividiendo)
    return dividiendo
   
def Multiplicacion(num1 , num2):
    Producto = (num1 * num2)
    print("la multiplicacion es :", Producto)
    return Producto

print("*****BIENVENIDO A LA CALCULADORA*****")
print("1, Sumar")
print("2, Restar")
print("3, Dividir")
print("4, Multiplicar")


operacion = input("****Ingresa el numero de la operacion que desea realizar**** :")

if operacion == '1':
    suma(num1, num2) 
elif operacion == '2':
    resta(num1, num2)
elif operacion == '3':
   division(num1, num2)
elif operacion == '4':
    Multiplicacion(num1,num2)
else:
    print("Operación no válida.")

