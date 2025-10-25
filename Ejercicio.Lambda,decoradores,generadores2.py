import functools
import time

def auditar_funcion(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"Ejecutando función: {func.__name__}")
        print(f"Llamada número: {wrapper.calls}")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Duración de ejecución: {end_time - start_time:.4f} segundos")
        return result
    wrapper.calls = 0
    return wrapper

@auditar_funcion
def leer_temperaturas():
    datos = [("CDMX", 26), ("Monterrey", 34), ("Toluca", 19), ("Cancún", 38), ("Guadalajara", 30), ("Puebla", 22)]
    for dato in datos:
        yield dato

@auditar_funcion
def filtrar_temperaturas_altas(temperaturas):
    return list(filter(lambda x: x[1] >= 30, temperaturas))

@auditar_funcion
def transformar_a_alertas(temperaturas):
    return list(map(lambda x: f"Alerta de calor en {x[0]}: {x[1]}°C", temperaturas))

@auditar_funcion
def ordenar_alertas(alertas):
    return sorted(alertas, key=lambda x: int(x.split(':')[1].strip('°C')), reverse=True)

@auditar_funcion
def calcular_promedio(temperaturas):
    if temperaturas:
        suma_temperaturas = functools.reduce(lambda acc, x: acc + x[1], temperaturas, 0)
        return suma_temperaturas / len(temperaturas)
    else:
        return 0

@auditar_funcion
def procesar_temperaturas():
    temperaturas = list(leer_temperaturas())
    temperaturas_altas = filtrar_temperaturas_altas(temperaturas)
    alertas_calor = transformar_a_alertas(temperaturas_altas)
    alertas_ordenadas = ordenar_alertas(alertas_calor)
    promedio_temperaturas = calcular_promedio(temperaturas_altas)

    print("\nLista ordenada de alertas:")
    for alerta in alertas_ordenadas:
        print(alerta)

    print(f"\nTemperatura promedio de alertas: {promedio_temperaturas:.2f}°C")

if __name__ == "__main__":
    procesar_temperaturas()