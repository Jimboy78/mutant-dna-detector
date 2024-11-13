def is_mutant(dna):
    def has_sequence(seq):
        for i in range(len(seq) - 3):
            if seq[i] == seq[i + 1] == seq[i + 2] == seq[i + 3]:
                return True
        return False

    row_length = len(dna[0])
    for row in dna:
        if len(row) != row_length:
            raise ValueError("DNA rows must have the same length.")

    n = len(dna)
    sequences_found = 0

    for row in dna:
        if has_sequence(row):
            sequences_found += 1

    for col in range(row_length):
        column = ''.join([dna[row][col] for row in range(n)])
        if has_sequence(column):
            sequences_found += 1

    return sequences_found >= 2
