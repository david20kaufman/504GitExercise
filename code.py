def count_amino_acids(seq: str):
    aa_counter = dict()
    for aa in seq:
        if aa not in aa_counter: # Encounter a new amino acid
            aa_counter[aa] = 1
        else: # Count an amino acid already found
            aa_counter[aa] += 1
    return aa_counter

def print_frequencies(aa_counts: dict):
    total = sum(aa_counts.values()) # Count the total number of amino acids
    print('freqs')
    for aa, count in aa_counts.items(): # Iterate through all amino acids and their counts
        print(f'{aa}:{count/total}')

seq = 'ATCTGACGCGCGCCGC'
aa_counts = count_amino_acids(seq)
print_frequencies(aa_counts)
        