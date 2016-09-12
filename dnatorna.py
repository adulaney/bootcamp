"""Convert DNA sequence to RNA"""

def rna(seq):
    """convert DNA sequence to RNA"""

    #Convert seq to uppercase
    seq = seq.upper()

    return seq.replace('T','U')
    
