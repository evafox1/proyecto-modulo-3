mayor = 0
precio = 0
producto_caro = ""
productos = []

while True:
    nombre_producto = input("Ingresa nombre de producto ('salir' para salir): ")

    if nombre_producto == "salir":
        break

    precio = int(input("Ingresa el precio del producto: "))

    productos.append([nombre_producto, precio])

    if precio > mayor:
        mayor = precio
        producto_caro = nombre_producto

if len(productos) > 0:
    print(f"El producto más caro es: {producto_caro} con ${mayor}")
    print(f"El total de productos es: {len(productos)}")
    print(f"Los productos y sus precios son: {productos}")
else:
    print("No se ingresaron productos.")



