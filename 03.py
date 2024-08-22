num1=int(input("Ingrese un numero"))
num2=int(input("Ingrese otro numero"))
num3=int(input("Ingrese el tercer numero"))

suma = num1+num2+num3
producto = num1*num2*num3

print("la suma es :" , suma)
print("El producto es  :" , producto)

if suma % 2 == 0:
    print("La suma es un numero par")
if producto % 5== 0:
    print(f"{producto} es multiplo de 5")

def calcular_promedio (num1,num2,num3):
    promedio = (num1+ num2+ num3)/3
    if promedio>10:
        print("El promedio es mayor que 10" , promedio)
    return promedio

try:
    division = num1 / num2 / num3
    print("La división es:", division)
except ZeroDivisionError:
    print("Error: no se puede dividir por cero")
