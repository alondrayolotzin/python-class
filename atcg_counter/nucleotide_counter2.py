import argparse

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
                    else:
                        print(f"Invalid character: {nucleotide}")
                        return None, None
    except FileNotFoundError:
        print("Sorry, couldn't find the file.")
        return None, None
    return counts, total

parser = argparse.ArgumentParser(description='Count nucleotides in a DNA sequence.')
parser.add_argument('sequence', metavar='sequence', type=str, help='Path to the DNA sequence file')
parser.add_argument('-n', '--nucleotides', nargs='+', default=['A', 'T', 'G', 'C'], help='Nucleotides to count (default: all)')
args = parser.parse_args()

counts, total = count_nucleotides(args.sequence, args.nucleotides)

if counts is not None and total is not None and total != 0:
    print("Nucleotide counts:")
    for nucleotide, count in counts.items():
        print(f"{nucleotide}: {count}")
else:
    print("No nucleotides found in the sequence.")
    