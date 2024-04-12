# Casos de prueba o escenarios

Este documento describe los escenarios de prueba diseñados para evaluar el funcionamiento del programa de Python que cuenta los nucleótidos en una secuencia de ADN. El objetivo principal de estas pruebas es asegurar la calidad y el correcto funcionamiento del programa bajo diversas condiciones.
    
La ejecución exitosa de estos casos de prueba es esencial para confirmar que el programa es completamente funcional y que puede enfrentar diferentes escenarios de entrada y errores potenciales
    
    
    
### Caso de prueba 1:

- Descripción: Archivo de entrada existe y contiene una secuencia de ADN válida.
- Datos de entrada: Archivo "test1.txt" con la siguiente secuencia de ADN: "ATCGATCG"
- Resultado esperado: La función debe contar correctamente las ocurrencias de cada nucleótido y mostrar los resultados esperados.

### Caso de prueba 2: 

- Descripción: Archivo de entrada no existe.
- Datos de entrada: Archivo "test2.txt" (archivo inexistente).
- Resultado esperado: La función debe manejar el error correctamente e informar al usuario que el archivo no fue encontrado (la funcion se implemento en la segunda modificacion del código)


### Caso de prueba 3: 

- Descripción: Archivo de entrada está vacío.
- Datos de entrada: Archivo "test3.txt" con contenido vacío.
- Resultado esperado: La función debe contar correctamente las ocurrencias de cada nucleótido, aunque no haya datos en el archivo (la funcion se implemento en la segunda modificacion del código).

### Caso de prueba 4: 

- Descripción: Archivo de entrada contiene caracteres inválidos.
- Datos de entrada: Archivo "test4.txt" con la siguiente secuencia de ADN: "ATCGXYZ".
- Resultado esperado: La función debe manejar correctamente los caracteres inválidos y contar solo las ocurrencias de nucleótidos válidos (A, C, G, T) (la funcion se implemento en la segunda modificacion del código).
        