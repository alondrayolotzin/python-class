# Contador de nucleotidos 

Fecha: Jueves 21 de Marzo 2024 

**Participantes**:
Alondra Yolotzin Marquez Mendoza 

## Descripción del Problema

Cuenta las ocurrencias de los simbolos 'A', 'C', 'G' y 'T' de una cadena de DNA  que se lee a traves de un archivo. 

## Especificación de Requisitos

1. El programa debe ser capaz de leer una cadena de ADN desde un archivo de texto proporcionado por el usuario.
2. El programa debe contar las ocurrencias de los símbolos 'A', 'C', 'G' y 'T' en la cadena de ADN.
3. El programa debe imprimir el número de ocurrencias de cada símbolo.


## Análisis y Diseño

Requisitos funcionales

- El programa debe ser capaz de leer una cadena de ADN desde un archivo de texto proporcionado por el usuario.
- El programa debe contar las ocurrencias de los símbolos 'A', 'C', 'G' y 'T' en la cadena de ADN leída del archivo.
- El programa debe imprimir el número de ocurrencias de cada símbolo ('A', 'C', 'G', 'T') en la cadena de ADN.
 
Requsitos no funcionales

- Debe ser capaz de manejar secuencias de ADN de diferentes longitudes.
- Los resultados deben ser precisos y exactos. 

#### Caso de uso: 

```
         +---------------+
         |   Usuario     |
         +-------+-------+
                 |
                 | 1. Proporciona archivo de entrada
                 v
         +-------+-------+
         |  Contador de  | 
         | incidencia de |
         | nucleotidos   |
         +---------------+
```

- **Actor**: Usuario

- **Descripción**: El actor proporciona un archivo de entrada que contega la secuencia de DNA . El sistema valida el archivo y los datos de entrada, y calcula la cantidad de cada nucleótido (A, T, G, C) contenido en la secuencia.
 
- **Flujo principal**:
1. El actor inicia el sistema proporcionando el archivo de entrada con la secuencia de DNA. 
2. El sistema cuenta la cantidad de cada nucleótido presente 
3. Se imprimen los recuentos de nucleótidos
	
- **Flujos alternativos**:
	
                

