#Exercise 2.2
import os

with open('data/salmonella_spi1_region.fna','r') as f:
    counter = 0
    base_pairs = 'CcGgAaTtUu'
    Long_chain = ''
    for line in f:
        counter += 1
        if line[0] in base_pairs:
            Long_chain += line

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
    for i in range(0,new_seq_length,3):
        gc_current_block = (shortened_seq[i:i+3].count('G')\
            + shortened_seq[i:i+3].count('C')) / block_size
        gc_of_blocks += [gc_current_block]

    gc_of_blocks = tuple(gc_of_blocks)
    return gc_of_blocks
