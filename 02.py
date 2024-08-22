num1=int(input("Ingrese un numero entero"))
num2=int(input("Ingrese el segundo numero"))

suma = num1+num2
producto = num1*num2

print("la suma es :", suma)
print("el producto es :", producto)


if suma>200:
    print("la suma es mayor que 200")
elif producto>1000:
    print("El producto es mayor que 1000")
try:
    division = num1/num2
    print("la division  es :", division)
    if division <1:
      print("El resultado de la division es menor que 1") 
except ZeroDivisionError:
    print("Error no se puede dividir en cero")
