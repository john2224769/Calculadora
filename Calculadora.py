#CALCULADORA BÁSICA CON MENU
import math

print(" --------------------------------------------------------------------------------")
print("Programa calculadora para dos numeros, escoja la operacion que desea realizar: ")
print(" ")
print("Ingrese 1 para sumar ")
print("Ingrese 2 para restar ")
print("Ingrese 3 para multiplicar ")
print("Ingrese 4 para dividir ")
print("Ingrese 5 para potencia ")
print("Ingrese 6 para logaritmo ")
print(" ")
print(" ---------------------------------------------------------------------------------")

#input
n=int(input("Ingrese la opcion a realizar: "))
print(" ")
x=float(input("Ingrese el primer numero 'x': "))
print(" ")
y=float(input("Ingrese el segundo numero 'Y': "))
print(" ")

#processing
if n==1:
    r=x+y
    print("El resultado de la suma entre "+str(x)+" y "+str(y)+" es: "+str(r))
else:
    if n==2:
        r=x-y
        print("El resultado de la resta entre "+str(x)+" y "+str(y)+" es: "+str(r))
    else:
        if n==3:
            r=x*y
            print("El resultado de la multiplicacion entre "+str(x)+" y "+str(y)+" es: "+str(r))
        else:
            if n==4:
                if y!=0:
                    r=x/y
                    print("El resultado de la division entre "+str(x)+" y "+str(y)+" es: "+str(r))
                else:
                    print("La division no se puede realizar, el denominador es igual a cero")
            else:
                if n==5:
                    r=x**y
                    print("El resultado de la potencia entre "+str(x)+" y "+str(y)+" es: "+str(r))
                else:
                    if n==6:
                        if x>1:
                            r=math.log(y)/math.log(x)
                            print("El resultado del logaritmo base "+str(x)+" y "+str(y)+" es: "+str(r))
                        else:
                            print("La base ingresada es menor a cero, no es posible calcular el logaritmo")
                    else:
                        print("La opcion ingresada no esta en el menu o es incorrecta")