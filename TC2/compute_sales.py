"""
Este módulo proporciona funciones para calcular el costo total
de ventas utilizando un catálogo de precios dado.
"""
import sys
import json
import time


def cargar_archivo_json(nombre_archivo):
    """
    Carga datos desde un archivo JSON.

    Args:
        nombre_archivo (str): El nombre del archivo JSON a cargar.

    Returns:
        dict: Los datos cargados desde el archivo JSON.
    """
    try:
        with open(nombre_archivo, 'r') as archivo:
            datos = json.load(archivo)
        return datos
    except FileNotFoundError:
        print(f"Error: Archivo '{nombre_archivo}' no encontrado.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"""Error: Formato JSON inválido en el archivo
              '{nombre_archivo}'.""")
        sys.exit(1)


def calcular_ventas(catalogo_precios, registro_ventas):
    """
    Calcula el costo total de todas las ventas utilizando
    el catálogo de precios dado.

    Args:
        catalogo_precios (dict): Un diccionario que contiene
        el catálogo de precios de los productos.
        registro_ventas (dict): Un diccionario que contiene
        el registro de ventas.

    Returns:
        float: El costo total de todas las ventas.
    """
    costo_total = 0.0

    # Calculamos el costo total de todas las ventas
    # Creamos una lista para almacenar el valor de cada producto
    precios_por_producto = {}

    # Asocia los precios del catálogo con los productos
    for producto in catalogo_precios:
        titulo = producto['title']
        precio = producto['price']
        precios_por_producto[titulo] = precio

    # Calcula el total de los precios de las unidades vendidas
    # total_precios = 0
    for venta in registro_ventas:
        producto = venta['Product']
        cantidad = venta['Quantity']

        # Si el producto está en el catálogo, suma el precio correspondiente
        if producto in precios_por_producto:
            precio_unitario = precios_por_producto[producto]
            costo_total += precio_unitario * cantidad

    # print(f"Total de precios de las unidades vendidas: ${costo_total:.2f}")
    return round(costo_total, 2)


def main():
    """
    Función principal que ejecuta el programa.
    """
    if len(sys.argv) != 3:
        print("""Uso: python compute_sales.py TC1.ProductList.json
              TC1.Sales.json""")
        sys.exit(1)

    archivo_catalogo_precios = sys.argv[1]
    archivo_registro_ventas = sys.argv[2]

    # Cargar catálogo de precios y registro de ventas desde archivos JSON
    catalogo_precios = cargar_archivo_json(archivo_catalogo_precios)
    registro_ventas = cargar_archivo_json(archivo_registro_ventas)

    tiempo_inicio = time.time()
    costo_total = calcular_ventas(catalogo_precios, registro_ventas)
    tiempo_fin = time.time()
    tiempo_transcurrido = tiempo_fin - tiempo_inicio

    print("Costo total de todas las ventas:", costo_total)
    print("Tiempo transcurrido:", tiempo_transcurrido, "segundos")


if __name__ == "__main__":
    main()
