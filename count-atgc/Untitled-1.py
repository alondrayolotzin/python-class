
# Definir la función para contar ocurrencias de símbolos en el ADN
def contar_ocurrencias_ADN(ADN):
    # Inicializar contadores
    ocurrencias = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

    # Contar ocurrencias de cada símbolo
    for base in ADN:
        if base in ocurrencias:
            ocurrencias[base] += 1

    # Imprimir resultados
    for base, count in ocurrencias.items():
        print(f'{base}: {count}')

# Pedir al usuario que ingrese la cadena de ADN
cadena_ADN = input("Ingresa la cadena de ADN: ").upper()

# Llamar a la función con la cadena de ADN ingresada por el usuario
contar_ocurrencias_ADN(cadena_ADN)