def to_rna(dna_strand):
    dna_rna_strand = {"G": "C", "C": "G", "T": "A", "A": "U"}
    rna_strand = ""
    for letter in dna_strand:
        rna_strand += dna_rna_strand[letter]
    return rna_strand

