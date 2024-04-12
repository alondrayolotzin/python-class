'''
NAME: nucleotide_counter.py

VERSION: 1.2

AUTHOR: Alondra Yolotzin Marquez Mendoza

DESCRIPTION:
This script counts the occurrences of each nucleotide (A, T, G, C) in a DNA sequence contained in a text file.

CATEGORY: Bioinformatics

USAGE:
% python  nucleotide_counter.py <file.txt>

ARGUMENTS:

- file.txt: Path to the DNA sequence file.
- Nucleotides to count: -n (specify which nucleotides to count), --nucleotides: (default: all).

METHOD:
The script uses Python's built-in functions and the argparse module to handle command-line arguments to count nucleotide incidences in a sequence

SEE ALSO: 
- argparse documentation: https://docs.python.org/3/library/argparse.html

'''

# ===========================================================================
# =                            imports
# ===========================================================================

import argparse

# ===========================================================================
# =                            Command Line Options
# ===========================================================================


# ===========================================================================
# =                            functions
# ===========================================================================
'''''
 Count the occurrences of each nucleotide in the DNA sequence.
    Arguments:
        sequence (str): Path to the DNA sequence file.
        nucleotides (list): List of nucleotides to count.
    Returns:
        - Dictionary containing the counts of each nucleotide.
        - Total count of nucleotides.
'''
def count_nucleotides(sequence, nucleotides):
    counts = {nucleotide.upper(): 0 for nucleotide in nucleotides}
    total = 0
    try:
        with open(sequence, 'r') as file:
            for line in file:
                for nucleotide in line.strip().upper():
                    if nucleotide in counts:
                        counts[nucleotide] += 1
                        total += 1
    except FileNotFoundError:
        print("Sorry, couldn't find the file.")
        return None, None
    return counts, total


# ===========================================================================
# =                            main
# ===========================================================================
'''main function'''

def main():
    parser = argparse.ArgumentParser(description='Count nucleotides in a DNA sequence.')
    parser.add_argument('sequence', metavar='sequence', type=str, help='Path to the DNA sequence file')
    parser.add_argument('-n', '--nucleotides', nargs='+', default=['A', 'T', 'G', 'C'], help='Nucleotides to count (default: all)')
    args = parser.parse_args()

    counts, total = count_nucleotides(args.sequence, args.nucleotides)

    if counts is not None and total is not None and total != 0:  # Verifica si total es distinto de cero
        print("Nucleotide counts:")
        for nucleotide, count in counts.items():
            print(f"{nucleotide}: {count} ({count/total*100:.2f}%)")
    else:
        print("No nucleotides found in the sequence.")

if __name__ == "__main__":
    main()


# step 1.

'''
The program reads the arguments provided by the user, which include the path
to the DNA sequence file and the nucleotides to count.
'''

# step 2.
'''
The program calls the count_nucleotides function with the parsed arguments.
This function opens the DNA sequence file, counts the occurrences of each nucleotide
in the sequence, and returns the counts and the total number of nucleotides counted.
'''

# step 3.
'''
If nucleotides are found in the sequence, the program prints the nucleotide counts 
and their percentages with respect to the total. Otherwise, it prints a message 
indicating that no nucleotides were found in the sequence.

'''


