import math

def calcular_area_circulo(radio):
    """Calcula el área de un círculo utilizando pi."""
    return math.pi * (radio ** 2)

def main():

    lista_areas = []
    
    print("\n--- Calculadora de Área de Círculo ---")
    
    # 6. Repetir proceso hasta que el usuario decida salir
    while True:
        try:
            radio = float(input("Ingresa el radio del círculo: "))
            
            # 1. Estructura de control
            if radio > 0:
                area = calcular_area_circulo(radio) # 2. Función con parámetros y retorno
                lista_areas.append(area)
                print(f"Área calculada: {area:.4f}")
            else:
                print("El radio debe ser mayor a cero.")
                
        except ValueError:
            print("Por favor, ingresa un número válido.")

        continuar = input("\n¿Deseas calcular otro círculo? (s/n): ").lower()
        if continuar != 's':
            break

    # 3. Convertir a tupla
    resultados_tupla = tuple(lista_areas)
    
    # 4. Mostrar la tupla
    print("\nResultados almacenados (tupla):", resultados_tupla)
    if len(resultados_tupla) > 0:
        promedio = sum(resultados_tupla) / len(resultados_tupla)
        print(f"El promedio de las áreas calculadas es: {promedio:.4f}")
    else:
        print("No se realizaron cálculos.")
if __name__ == "__main__":
    main()