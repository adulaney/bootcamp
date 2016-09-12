def reverse_complement_ex(seq):
    #Initialize Reverse complement
    rev_seq = ''
    i = 0
    #Loop
    for base in seq:
        i += 1
        rev_seq= rev_seq + complement_base(seq[-i],material='DNA')
    return rev_seq    
