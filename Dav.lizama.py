productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}

def stock_marca():
    marca = input("Ingrese la marca que desea buscar: ")
    marca = marca.lower()
    for stock, info in productos.items():
        if info[0].lower() == marca:
            total = stock[1]
            print(f"Hay {total} stocks disponible de la marca '{marca.capitalize()}' ")


def busqueda_precio():
    try:
        p_min = input(int(input("Ingresa el precio minimo: ")))
        p_max = input(int(input("Ingresa el precio maximo: ")))
    except ValueError:
        print("ERROR: Solo numeros validos!")
        return
    
    accesibilidad = []
    for modelos, (precio, cantidad) in stock.items():
        if p_min <= precio <= p_max and cantidad > 0:
            marca = productos[0]

    accesibilidad.append(f'"{marca}" Marca, {modelo} Modelo.') 
    if accesibilidad:
        for item in sorted(accesibilidad):
            print(item)
    else:
        print("No se encuentra dispositivos en su rango de busqueda")

def actualizar_precio():
    print("no me alcanzo el tiempo :c")


def salida():
    print("Hasta pronto!...")
    return

def main():
    while True:
        print(" ")
        print("*** Menu Principal ***")
        print("1.- Stock Marca")
        print("2.- Busqueda por precio")
        print("3.- Actualizar precio")
        print("4.- Salir")

        opcion = int(input("Ingrese alguna opcion: "))

        if opcion == 1:
            stock_marca()
        elif opcion == 2:
            busqueda_precio()
        elif opcion == 3:
            actualizar_precio()
        elif opcion == 4:
            salida()
            break
        else:
            print("ERROR: Opción requerida no existente!")

main()      
        