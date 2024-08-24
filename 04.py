num1=int(input("Ingresa el primer numero :"))
num2=int(input("Ingrese el siguiente numero :"))
num3=int(input("Ingrese el tercer numero :"))
num4=int(input("Ingrese el cuarto numero :"))

suma = num1+num2+num3+num4
producto= num1*num2

if suma % 2 !=0:
    print("la suma es un numero impar :", suma)

if producto % 7==0:
     print(f"{producto} es multiplo de 7")
    
def calcular_promedio(num1,num2,num3,num4):
        promedio=(num1+num2+num3+num4)/4
        if promedio<10:
          print("el promedio es bajo :", promedio)
        return promedio

try:
    division = suma/num4
    print("La división es:", division)
except ZeroDivisionError:
    print("Error: no se puede dividir por cero")


        
