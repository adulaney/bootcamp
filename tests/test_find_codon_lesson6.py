import pytest
import find_codon_lesson6 as fcl6
seq = 'ATGGAGAACAACGAAGCCCCCTCCCCCTCGGGATCCAACAACAACGAGAACAACAATGCAGCCCAGAAGA\
AGCTGCAGCAGACCCAAGCCAAGGTGGACGAGGTGGTCGGGATTATGCGTGTGAACGTGGAGAAGGTCCTGGAGCGG\
GACCAGAAGCTATCGGAACTGGGCGAGCGTGCGGATCAGCTGGAGCAGGGAGCATCCCAGTTCGAGCAGCAGGCCGG\
CAAGCTGAAGCGCAAGCAATGGTGGGCCAACATGAAGATGATGATCATTCTGGGCGTGATAGCCGTTGTGCTGCTCA\
TCATCGTTCTGGTGTCGCTTTTCAATTGA'

def test_find_codon_lesson6():
    assert fcl6.find_codon_lesson6('ATG',seq) == 0
    assert fcl6.find_codon_lesson6('TGG',seq) == 1
    assert fcl6.find_codon_lesson6('AAT',seq) == 54
    assert fcl6.find_codon_lesson6('TGT',seq) ==