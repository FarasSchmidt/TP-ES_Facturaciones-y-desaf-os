prod1 = int(input("Ingresar precio de un producto: "))
prod2 =  int(input("Ingresar precio de un producto: "))
prod3 = int(input("Ingresar precio de un producto: "))

total = int(prod1 + prod2 + prod3)
iva = int((total * 21) / 100)

print("el valor total de los productos es",total)
print("el promedio del valor de los tres productos es: ",total / 3)


print("El precio final de los productor más IVA es de: ",total + iva)