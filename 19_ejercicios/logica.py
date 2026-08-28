def mayor(n1,n2,n3):
    n1= float(input("ingresa el primer numero:"))
    n2= float(input("ingresa el segundo numero:"))
    n3= float(input("ingresa el tercer numero:"))
    if n1> n2 and n2>n3:
        return print(f"El numero mayor es: {n1}")
    elif n2>n3 and n3>n1:
        return print(f"El numero mayor es:{n2}")
    else:
        return print(f"El numero mayor es:{n3}")     