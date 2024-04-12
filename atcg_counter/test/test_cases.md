# Casos de prueba o escenarios

Este documento describe los escenarios de prueba diseñados para evaluar el funcionamiento del programa de Python que cuenta los nucleótidos en una secuencia de ADN. El objetivo principal de estas pruebas es asegurar la calidad y el correcto funcionamiento del programa bajo diversas condiciones.
    
La ejecución exitosa de estos casos de prueba es esencial para confirmar que el programa es completamente funcional y que puede enfrentar diferentes escenarios de entrada y errores potenciales
    
### Caso de prueba 1: Comprobacion de conteo adecuado 
- Descripción: Verificar que el conteo de los nucleotidos es exacto y que el calculo del porcentaje es certero
- Datos de entrada: nucleotide_counter.py <archivo_valido.txt> 
- Resultado esperado: Recuento de cada nucleótido con sus porcentajes.

### Caso de prueba 2: Archivo de secuencia válido con todos los nucleótidos presentes
- Descripción: Verificar que el archivo proporcionado es valido
- Datos de entrada: nucleotide_counter.py <archivo_valido.txt>
- Resultado esperado: Se mostrara el conteo de nucleotidos, de no ser asi se mostrara un mensaje indicando que no se pudo encontrar el archivo.

### Caso de prueba 3: Archivo de secuencia vacío
- Descripción: Verificar que el archivo proporcionado tiene una secuencia 
- Datos de entrada: nucleotide_counter.py <archivo_valido.txt>
- Resultado esperado: Se mostrara el conteo de nucleotidos, de no ser asi se mostrara un mensaje indicando que no se encontraron nucleótidos en la secuencia.

### Caso de prueba 4: Especificación de nucleótidos a contar
- Descripción: Verificar que el programa permite la especificacion de los nucleotidos que se quieren contar, y no tomar en cuenta todas las bases por default 
- Datos de entrada: nucleotide_counter.py <archivo_valido.txt> -n A T
- Resultado esperado: Recuento de los nucleótidos A y T con sus porcentajes.




        