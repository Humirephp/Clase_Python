num1=int(input("Ingresa un 1er numero :"))
num2=int(input("Ingresa un 2do numero :"))
num3=int(input("Ingresa un 3ro numero :"))
num4=int(input("Ingresa un 4to numero :"))
num5=int(input("Ingresa un 5to numero :"))

maximo = max(num1,num2,num3,num4,num5)
minimo= min(num1,num2,num3,num4,num5)

suma=num1+num2+num3+num4+num5
producto=num1*num3*num5

if suma % 3 == 0:
    print("La suma es divisible por 3" , suma)
if producto>100:
    print("el producto es alto :" , producto)


def calcular_promedio(num1,num2,num3,num4,num5):
    promedio =(num1+num2+num3+num4+num5)/5
    if promedio % 1 == 0:
        print("EL promedio es un numero entero :" , promedio)
    return promedio

resta = maximo - minimo
print("La resta del numero maximo y minimo es :", resta)
if resta < 0 :
    print("Advertencia la resta es negativa :")


try:
    resultado = producto/suma
    print("El resultado de la division del producto y la suma es " , resultado)
except ZeroDivisionError:
    print("Error: no se puede dividir por cero porque la suma es 0")