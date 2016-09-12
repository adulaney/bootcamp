def ratio(x,y):
    """The ratio of 'x' to 'y'."""
    return x / y


def complement_base(base, material='DNA'):
    """Returns the Watson-Crick comlement of a base"""

    if base in 'Aa':
        if material == 'DNA':
            return 'T'
        elif material =='RNA':
            return 'U'
        else:
            raise RuntimeError('Invalid Material')
    elif base in 'TtUu':
        return 'A'
    elif base in 'Gg':
        return 'C'
    else:
        return 'G'


def reverse_complement_ex(seq,material='DNA'):
    """Returns reverse complement of nucleotide chain
    Example 1.3a"""
    #Initialize Reverse complement
    rev_seq = ''
    i = 0
    #Loop
    for base in seq:
        i += 1
        rev_seq= rev_seq + complement_base(seq[-i],material='DNA')
    return rev_seq


def reverse_complement_ex1_3b(seq,material='DNA'):
    """Returns reverse complement of nucleotide chain
    Example 1.3b"""

    rev_seq = seq[::-1].upper()

    if material == 'DNA':
        rev_seq = rev_seq.replace('A','t')
    elif material == 'RNA':
        rev_seq = rev_seq.replace('A','u')
    rev_seq = rev_seq.replace('G','c')
    rev_seq = rev_seq.replace('C','g')
    rev_seq = rev_seq.replace('T','a')

    return rev_seq.upper()


def longest_common_substring(seq1,seq2):
    """Finds longest common substring between 2 sequences"""
    commonseq =''
    if len(seq1)>=len(seq2):
        shortest = len(seq2)
        longseq = seq1
        shortseq = seq2
    else:
        shortest = len(seq1)
        longseq = seq2
        shortseq = seq1
    #Iterate for length of common substring
    for i in range(shortest):
    #    if i >= 1:
            #Iterate along the shortest strand to check all
            #substrings of length i
        for j in range(shortest+1-i):
            if shortseq[j:j+i] in longseq:
                    commonseq = shortseq[j:j+i]
    return commonseq


def secondary_RNA_struc(seq):
    """Finds secondary RNA structures
    Example 1.5"""


def reverse_complement(seq,material='DNA'):
    """Compute reverse complement of a nucleic acid sequence."""
    #Initialize reverse complement
    rev_comp = ''

    #Loop through and populate list with reverse complement
    for base in reversed(seq):
        rev_comp += complement_base(base,material=material)

    return rev_comp


def display_complements(seq):
    """Print sequence above its reverse complement."""


def answer_to_the_ultimate_question_of_life_and_everything():
    """Simpler program that Deep Thought's, I bet."""
    return 42

def think_too_much():
    """Express Caesar's skepticism about Cassius"""

    print("""Yond Cassius has a lean and hungry look,
    He thinks too much; such men are dangerous.""")


def parentheses_check(seq):
    """"Checking secondary structure base pairs are even"""

    left = seq.count('(')
    right = seq.count(')')
    if left == right:
        return 'Valid Structure'
    else:
        return 'Not a valid Structure'
