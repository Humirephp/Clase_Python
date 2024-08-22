num1=int(input("Ingrese el primer numero"))
num2=int(input("Ingrese el segundo numero"))

suma= num1+num2
producto = num1*num2

print("la suma es", suma)
print("el producto es", producto)

if suma>100:
    print("la suma es mayor que 100")
elif producto<50:
    print("El producto es menor a 50")

