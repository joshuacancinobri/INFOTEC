from cliente import Cliente
from producto import Producto
from venta import Venta
from tienda import Tienda

# Crear cliente 1
cliente1 = Cliente("Luis", "luis@mail.com", 1000)
# Crear productos para Venta 1
p1 = Producto("Teclado", 250)
p2 = Producto("Mouse", 150)
# Crear venta 1 y agregar productos
venta1 = Venta(cliente1)
venta1.agregar_producto(p1)
venta1.agregar_producto(p2)

# Crear cliente 2
cliente2 = Cliente("Ana", "ana@mail.com", 2000)
# Crear productos para Venta 2
p3 = Producto("Monitor", 1300)
p4 = Producto("Audífonos", 450)
# Crear venta 2 y agregar productos
venta2 = Venta(cliente2)
venta2.agregar_producto(p3)
venta2.agregar_producto(p4)

# Crear tienda y registrar ambas ventas
tienda = Tienda("TechStore")
tienda.registrar_venta(venta1)
tienda.registrar_venta(venta2)

# Resultados
print("--- Venta 1 ---")
print(cliente1.mostrar_info())
print(f"Total de la venta: ${venta1.total():.2f}")

print("\n--- Venta 2 ---")
print(cliente2.mostrar_info())
print(f"Total de la venta: ${venta2.total():.2f}")

print("\n--- Resumen de Tienda ---")
print(f"Ventas registradas en {tienda.nombre}: {len(tienda.ventas)}")
print(f"Total de productos creados: {Producto.total_productos()}")