num1=int(input("Ingresa un 1ro numero :"))
num2=int(input("Ingresa un 2do numero :"))
num3=int(input("Ingresa un 3ro numero :"))
num4=int(input("Ingresa un 4to numero :"))
num5=int(input("Ingresa un 5to numero :"))

suma = num1+num2+num3+num4+num5
producto = num1*num2*num3*num4*num5

num_maximo = max(num1,num2,num3,num4,num5)
num_minimo = min(num1,num2,num3,num4,num5)

if suma % 2 == 0:
    print("la suma es un numero par:", suma)
if producto % 4 == 0 and producto % 6 == 0:
    print("el producto es divisible por 4 0 6 : ", producto)

resta = num_maximo - num_minimo
print("La resta del numero maximo y el numero minimo es :", resta)
if resta % 3 == 0:
    print("La resta es multiplo de 3:", resta)

def calcular_promedio(num1,num2,num3,num4,num5):
    promedio=(num1+num2+num3+num4+num5)/5
    if promedio > 15 :
        print("El pronedio es alto",promedio)
    if promedio % 1 == 0:
        print(f"el pronedio {promedio} es un numero entero :")
    return promedio

try:
    resuktado = suma / producto
    print("la division entre el resultado de la suma y el producto es :", resuktado)
except ZeroDivisionError:
    print("Error: no se puede dividir por cero porque la suma es 0")
