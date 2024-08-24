inicio = int(input("Ingresa el valor de  inicio :"))
fin = int(input("Ingresa el valor de fin : "))

if inicio >=fin :
    print("Error: El valor de inicio debe ser menor que el valor de fin.")
else:

 if inicio % 2 !=0:
    inicio +=1


 print(f"Numeros pares entre {inicio} y {fin}:")
while inicio <=fin:
     print(inicio)
     inicio +=2

