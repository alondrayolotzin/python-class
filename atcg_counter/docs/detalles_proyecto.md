# Contador de nucleotidos

Fecha: 22/04/2024

**Participantes**:
- Alondra Yolotzin Marquez Mendoza 
<alondram@lcg.unam.mx>

## Descripción del Problema

El proposito general del programa es proporcionar una herramienta que permita resolver el problema de contar la cantidad de cada nucleótido (A, T, G, C) en una secuencia de ADN contenida en un archivo de texto. Para esto, el script acepta como entrada el archivo que contiene la secuencia de ADN y opcionalmente permite especificar qué nucleótidos se deben contar.


## Especificación de Requisitos

**Requisitos funcionales**

- El programa debe ser capaz de contar la cantidad de cada nucleótido (A, T, G, C) presente en una secuencia de ADN contenida en un archivo de texto.
- Debe permitir al usuario especificar la ubicación del archivo que contiene la secuencia de ADN a analizar.
- Debe dar la opción para que el usuario especifique qué nucleótidos quiere contar. Esta funcionalidad es opcional, ya que si no hay especificación se contaran todos los nucleótidos 
- Se debera producir un mensaje de error si el archivo no existe.
- Se debera producir un mensaje de error si el archivo tiene caracteres invalidos
- Se debera producir un mensaje de error si el archivo esta vacio
- El output debera ser el conteo de nucleótidos, mostrando la cantidad de cada nucleótido y su porcentaje con respecto al total.

**Requisitos no funcionales**

- El script deberá estar escrito en Python.
- El tiempo de respuesta debe ser rápido, incluso con archivos de gran tamaño.
- Debe ser capaz de manejar secuencias de ADN de diferentes longitudes.
- Los resultados deben ser precisos y exactos. 
- La entrada del archivo debe ser flexible (i.e. se acepta a través de la línea de comandos).


## Análisis y Diseño
El programa utilizara algunas funciones que permitan al usuario precisión y exactitud en su uso; ademas manejara algunas excepciones que permitan la  validación de el archivo y los datos propocionados. 

La loógica básica del scrip es la siguiente: 

```bash 

Función contar_nucleotidos(archivo, nucleotidos):
    Inicializar un diccionario de recuentos a 0 para cada nucleótido
    Inicializar un contador total a 0
    Intentar abrir el archivo
    Para cada línea en el archivo:
        Para cada nucleótido en la línea:
            Si el nucleótido está en la lista de nucleótidos:
                Incrementar su recuento en el diccionario
                Incrementar el contador total
                Manejar excepcion de carácter invalido 
    Manejar excepción de archivo no encontrado
    Devolver el diccionario de recuentos y el contador total

Función principal():
    Parsear los argumentos de línea de comandos
    Llamar a contar_nucleotidos con los argumentos parseados
    Si se obtuvieron recuentos y el contador total no es cero:
        Imprimir los recuentos de nucleótidos y sus porcentajes
    De lo contrario:
        Imprimir un mensaje de no se encontraron nucleótidos

Llamar a la función principal para iniciar el programa
```
El formato del archivo de entrada debe ser un archivo de texto plano que contenga la secuencia de ADN, de cualquier longitud. Además, la secuencia puede estar tanto en mayúsculas como en minúsculas, ya que el script las convertirá a mayúsculas durante el procesamiento.

#### Caso de uso: Sumar Números

```
         +---------------+
         |   Usuario     |
         +-------+-------+
                 |
                 | 1. Proporciona archivo de entrada que contenga secuencia
                 v
         +-------+-------+
         |  Contador de  | 
         | incidencia de |
         | nucleotidos   |
         +---------------+
```

- **Actor**: Usuario
- **Descripción**:El actor proporciona un archivo de entrada que contega la secuencia de DNA . El sistema valida el archivo y los datos de entrada, y calcula la cantidad de cada nucleótido (A, T, G, C) contenido en la secuencia.

- **Flujo principal**:
1. El actor inicia el sistema proporcionando el archivo de entrada con la secuencia de DNA. 
2. El sistema valida el archivo y los datos de entrada.
3. El sistema cuenta la cantidad de cada nucleótido presente 
4. Se imprimen los recuentos de nucleótidos y sus porcentajes con respecto al total, si se encontraron nucleótidos en la secuencia.
	
- **Flujos alternativos**:
	

1. Si no se especifica la ruta del archivo o los argumentos no son válidos, se imprime un mensaje de error 
2. Si no se encuentran nucleótidos en la secuencia (archivo vacio), el script imprime un mensaje indicando que no se encontraron nucleótidos en la secuencia.          

