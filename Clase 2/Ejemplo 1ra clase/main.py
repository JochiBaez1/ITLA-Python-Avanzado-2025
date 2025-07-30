import PaqueteOps.moduloOpsAritmeticas as ma



nombre = input("Ingrese su nombre: ")
print("Bienvenido a programa Calculadora")

opcion = int(input("1- Ops Aritmeticas 2- Ops Cientificas 3- Ops Relacionales: "))

if opcion == 1:
    o1 = int(input("1- Sumar 2- Restar 3- Multiplicar 4- dividir "))
    if o1 == 1:
        n1 = int(input("Ingrese el Primer Numero: "))
        n2 = int(input("Ingrese el Segundo Numero: "))
        ma.Sumar(n1,n2)
    elif o1 == 2:
        print("a")
    else:
        print("opcion incorrecta") 
elif opcion == 2:
    o2 = input("1- Sumar 2- Restar 3- Multiplicar 4- dividir ")
elif opcion == 3:
    o3 = input("1- Sumar 2- Restar 3- Multiplicar 4- dividir ")