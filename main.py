from modulos.calculadora import *

while True:
    print("1. suma")
    print("2. resta")
    print("3. multiplicacion")
    print("4. division")
    print("5. salir")
    OP=input("Elija una opcion : ")

    if OP=="1":
        num1=float(input("Ingrese el primer numero : "))
        num2=float(input("Ingrese el segundo numero : "))
        print("El resultado es : ", suma(num1, num2))
    elif OP=="2":
        num1=float(input("Ingrese el primer numero : "))
        num2=float(input("Ingrese el segundo numero : "))
        print("El resultado es : ", resta(num1, num2))
    elif OP=="3":
        num1=float(input("Ingrese el primer numero : "))
        num2=float(input("Ingrese el segundo numero : "))
        print("El resultado es : ", multiplicacion(num1, num2))
    elif OP=="4":
        num1=float(input("Ingrese el primer numero : "))
        num2=float(input("Ingrese el segundo numero : "))
        print("El resultado es : ", division(num1, num2))