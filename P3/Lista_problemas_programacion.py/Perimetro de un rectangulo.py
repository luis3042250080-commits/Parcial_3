def calcular_geometria(base, altura):
    """Calcula area y perimetro, retorna ambos valores."""
    area = base * altura
    perimetro = 2 * (base + altura)
    return area, perimetro
def main():
    lista_areas = []
    lista_perimetros = []
    while True:
        try:
            base = float(input("Ingresa la base: "))
            altura = float(input("Ingresa la altura: "))
            if base > 0 and altura > 0:
                a, p = calcular_geometria(base, altura)
                lista_areas.append(a)
                lista_perimetros.append(p)
                print(f"Calculado -> area: {a}, Perimetro: {p}")
            else:
                print("Error: Las medidas deben ser mayores a cero.")
        except ValueError:
            print("Por favor, ingresa numeros validos.")
        continuar = input("\n Deseas calcular otra figura? (s/n): ").lower()
        if continuar != 's':
            break
    set_areas = set(lista_areas)
    set_perimetros = set(lista_perimetros)
    print("\nResultados unicos de Areas (set):", set_areas)
    print("Resultados unicos de Perimetros (set):", set_perimetros)
    if len(set_areas) > 0:
        promedio_a = sum(set_areas) / len(set_areas)
        promedio_p = sum(set_perimetros) / len(set_perimetros)
        print(f"\nPromedio de Areas unicas: {promedio_a:.2f}")
        print(f"Promedio de Perimetros unicos: {promedio_p:.2f}")
    else:
        print("\nNo se realizaron calculos.")

if __name__ == "__main__":
    main()