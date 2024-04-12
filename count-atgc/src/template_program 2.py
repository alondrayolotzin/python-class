'''
NAME: nucleotide_counter.py

VERSION: 1.0

AUTHOR: Alondra Yolotzin Marquez Mendoza

DESCRIPTION:
This script counts the occurrences of each nucleotide (A, T, G, C) in a DNA sequence contained in a text file.

CATEGORY: Bioinformatics

USAGE:
% python  nucleotide_counter.py <file.txt>
       

ARGUMENTS
The program takes one argument, which is the path to the input file containing the DNA sequence.

METHOD

The program reads the DNA sequence from the input file provided by the user.
It then iterates over the sequence, counting the occurrences of the symbols 'A', 'C', 'G', and 'T'.
Then prints the count of each symbol.

SEE ALSO


        
'''


# ===========================================================================
# =                            imports
# ===========================================================================

import sys

# ===========================================================================
# =                            Command Line Options
# ===========================================================================


# ===========================================================================
# =                            functions
# ===========================================================================

def count_nucleotides(filename):
    # Abre el archivo en modo lectura
    with open(filename, 'r') as file:
        # Lee la cadena de ADN del archivo
        dna_sequence = file.read()

    # Inicializa contadores para cada símbolo
    count_A = 0
    count_C = 0
    count_G = 0
    count_T = 0

    # Itera sobre la cadena de ADN y cuenta las ocurrencias de cada símbolo
    for symbol in dna_sequence:
        if symbol == 'A':
            count_A += 1
        elif symbol == 'C':
            count_C += 1
        elif symbol == 'G':
            count_G += 1
        elif symbol == 'T':
            count_T += 1

    # Imprime el resultado
    print(f'El símbolo A aparece {count_A} veces.')
    print(f'El símbolo C aparece {count_C} veces.')
    print(f'El símbolo G aparece {count_G} veces.')
    print(f'El símbolo T aparece {count_T} veces.')



# ===========================================================================
# =                            main
# ===========================================================================


# step 1.
'''
Read the DNA sequence from the file provided from the user.
'''

# step 2.
'''
Counters are initialized for each nucleotide contained in the sequence, and it iterates over it,
incrementing the counter for each nucleotide.
'''

# step 3.
'''
prints out the count of each nucleotide.
'''



