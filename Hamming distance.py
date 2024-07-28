def hamming_distance(strand1, strand2):
    if len(strand1) != len(strand2):
        print("Strands must be of equal length")

    distance = 0
    for nucleotide1, nucleotide2 in zip(strand1, strand2):
        if nucleotide1 != nucleotide2:
            distance += 1
    return distance




    
    
strand1 = "GAGCCTACTAACGGGAT"
strand2 = "CATCGTAATGACGGCCT"
print(hamming_distance(strand1, strand2)) 