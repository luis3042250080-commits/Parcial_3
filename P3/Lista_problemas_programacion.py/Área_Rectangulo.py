print("\033c")
#ejercicio con tuplas
def calcular_area(base, altura):
    area = base * altura
    return area
lista = []
contador = 0
acum = 0
respuesta = "s"

while respuesta.lower() == "s":
    base = float(input("Ingresa la base: "))
    altura = float(input("Ingresa la altura: "))
    resultado = calcular_area(base, altura)
    print(f"El área calculada es: {resultado}")
    acum += resultado
    contador += 1
    datos_actuales = (base, altura, resultado) 
    lista.append(datos_actuales)
    respuesta = input("¿Deseas ingresar otro dato? (S/N): ").strip()
tupla_final = tuple(lista)
print("\n--- RESULTADOS FINALES ---")
print(f"Total de áreas calculadas (Contador): {contador}")
print(f"Suma total de las áreas (Acumulador): {acum}")
print(f"Tupla final con el historial de datos: {tupla_final}")