for tienda in range(1,4):
    suma=0
    print(f"--Categoria--{tienda}")
    for producto in range (1,5):
        precio=int(input("Ingrese el precio del producto: "))
        suma=suma+precio
    print(f"El total de venta de las categoria {tienda} es: {suma}")