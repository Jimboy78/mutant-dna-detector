from app.mutant_checker import is_mutant


def test_is_mutant():
    dna_mutant = ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
    dna_human = ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CTCCTA", "TCACTG"]

    assert is_mutant(dna_mutant) is True
    assert is_mutant(dna_human) is False
