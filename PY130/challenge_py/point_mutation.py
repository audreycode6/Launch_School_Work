'''Write a program that can calculate the Hamming distance between two DNA strands.

A mutation is simply a mistake that occurs during the creation 
    or copying of a nucleic acid, in particular DNA. 
    Because nucleic acids are vital to cellular functions,
    mutations tend to cause a ripple effect throughout the cell. 
    Although mutations are technically mistakes, a very rare 
    mutation may equip the cell with a beneficial attribute. 
    In fact, the macro effects of evolution are attributable to 
    the accumulated result of beneficial microscopic 
    mutations over many generations.

The simplest and most common type of nucleic acid mutation 
    is a point mutation, which replaces one base with 
    another at a single nucleotide.

By counting the number of differences between two 
    homologous DNA strands taken from different genomes 
    with a common ancestor, we get a measure of the 
    minimum number of point mutations that could have occurred 
    on the evolutionary path between the two strands.

This is called the Hamming distance.

GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
^ ^ ^  ^ ^    ^^
The Hamming distance between these two DNA strands is 7.

The Hamming distance is only defined for sequences of equal length. 
    If you have two sequences of unequal length, 
    you should compute the Hamming distance over the shorter length.
'''

'''PEDAC:
P:
    in: string of DNA
    out: integer, representing the Hamming Distance
    e:
    - if length ==
    - if length not equal compare by len of smallest string
    i:
    - empty string == 0 OR identical stirng == 0
    - need to make a DNA class that takes in a string of DNA
        - needs a hamming_distance class method(?), takes in 
    - dont actually shorten real str
E: test_point_mut.py
    
'''

class DNA:
    def __init__(self, dna_str):
        self._dna_str = dna_str

    @property 
    # discourage modification of original dna_str by only definning getter
    def dna_str(self):
        return self._dna_str

    def hamming_distance(self, other_dna_str):
        hamming_distance = 0 # initalize counter for distance

        zipped_dna = zip(self.dna_str, other_dna_str)
        # zip only iterates up to the point of the smallest sequence
        for elem1, elem2 in zipped_dna:
            if elem1 != elem2:
                hamming_distance += 1

        return hamming_distance
