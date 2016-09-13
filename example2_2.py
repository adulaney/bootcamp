#Exercise 2.2
import os

with open('data/salmonella_spi1_region.fna','r') as f:
    counter = 0
    base_pairs = 'CcGgAaTtUu'
    Long_chain = ''
    for line in f:
        counter += 1
        if line[0] in base_pairs:
            Long_chain += line.rstrip()

#Example 2.3
def gc_blocks(seq, block_size):
    if type(block_size) != int or block_size <= 0:
        RuntimeError('Block size not a positive integer.')

    #Defines blocks of the sequence.
    seq = seq.upper()
    number_of_blocks = len(seq) // block_size
    new_seq_length = number_of_blocks * block_size
    shortened_seq = seq[0:new_seq_length]

    #Calculate GC content for different blocks
    gc_of_blocks = []
    for i in range(0,new_seq_length,block_size):
        gc_current_block = (shortened_seq[i:i+block_size].count('G')\
            + shortened_seq[i:i+block_size].count('C')) / block_size
        gc_of_blocks += [gc_current_block]

    gc_of_blocks = tuple(gc_of_blocks)
    return gc_of_blocks


#Example 2.3b
def gc_map(seq, block_size, gc_thresh):
    """Checks if a block of sequence is above gc threshold."""

    if type(block_size) != int or block_size <= 0:
        RuntimeError('Block size not a positive integer.')

    #Defines blocks of the sequence.
    seq = seq.lower()
    number_of_blocks = len(seq) // block_size
    new_seq_length = number_of_blocks * block_size
    shortened_seq = seq[0:new_seq_length]

    #Calculate GC content for different blocks
    threshold_sequence = ''
    for i in range(0, new_seq_length, block_size):
        gc_current_block = (shortened_seq[i:i+block_size].count('g')\
            + shortened_seq[i:i+block_size].count('c')) / block_size
        print(gc_current_block)
        if gc_current_block > gc_thresh:
            threshold_sequence += shortened_seq[i:i+block_size].upper()
        else:
            threshold_sequence += shortened_seq[i:i+block_size]

    return threshold_sequence


#Example 2.4a
def longest_orf(seq):
    """Finds longest open reading frame in DNA sequence."""
    start_codons = 'ATG'
    stop_codons = ['TGA','TAG','TAA']
    old_orf_length = 0
    for i in range(0,len(seq)):
        if seq[i:i+3] in start_codons:
            for j in range(i+3,len(seq),3):
                if seq[j:j+3] in stop_codons:
                    orf_length = j + 3 - i
                    if orf_length > old_orf_length:
                        old_orf_length = orf_length
                        orf_longest = seq[i:j+3]

    return orf_longest
