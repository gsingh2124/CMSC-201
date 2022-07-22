'''
File:           hw5_part1.py
Author:         Gurjinder Singh
Date:           10/18/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    Genetic extraction

'''

import sys
from random import choice, seed


if len(sys.argv) >= 2:
    seed(sys.argv[1])

# USE IF YOU ARE TESTING AND DON'T WANT TO USE COMMAND LINE ARGUMENTS
# seed(input('What seed do you want to use? '))
# END SECTION

STOP_PARAM = 'stop'
SEQ_PARAM = 'seq'
NUCLEOTIDES = ['A', 'T', 'C', 'G']
# your constants should start here
START = ['ATG']
STOP = ['TAA', 'TGA', 'TAG']
CODON_LENGTH = 3


def extract_genes(sequence):
    output = []
    count = int("0") #for checking when to switch from start to stop
    codon_List = [] #new list dividing up the sequence into codons
    start_Index = 0 #index that gets assigned the first start codon index
    current_String = ""#current compiled codons
    itterator = 0 #itterator for while loop
    for i in range(len(sequence)):
        if (i % 3) == 0:
            codon_List.append(sequence[i:i+3])
    itterator = 0 #check for start or stop sequence
    while itterator < (len(sequence)/CODON_LENGTH):#Gets the new size of the list because its split into codons now
        if count == 0:#Start phase
            if codon_List[itterator] in START:#if current codon is a start codon...
                count = 1#once a start codon is found, the switch to the stop algorithm starts
                start_Index = itterator
                current_String = current_String + codon_List[itterator]#adding the start codon to the currently compiled list of codons
            itterator = itterator + 1#move up one index in the codon list
        elif count == 1:#Stop phase
            current_String = current_String + codon_List[itterator]#add the next codon regardless if its a stop codon or not
            if codon_List[itterator] in STOP:#once a stop codon is found...
                count = 0#switch back to start algorithm
                itterator = start_Index + 1  # step up in index
                output.append(current_String)#add currently compiled codons to output list
                current_String = ""#empty current codons
            else: #if its not a stop codon...
                itterator = itterator + 1#step up in index, so the next codon gets added within the stop phase
    return output


    """
    This function should return a list of genes that start with the
    start codon and end with one of the three stop codons.
    :param sequence: a string of nucleotides
    :return: a list of "genes"
    """


if __name__ == '__main__':
    length_or_stop = input('How many codons do you want to create? (or stop to end, seq to enter your own sequence)')
    while length_or_stop.lower() != STOP_PARAM:
        try:
            if length_or_stop.lower() == SEQ_PARAM:
                the_sequence = input('Enter your own sequence: ').upper()
                if len(the_sequence) % 3 != 0:
                    raise ValueError('The length of the string must be divisible by 3')
                if any(x not in NUCLEOTIDES for x in the_sequence):
                    raise ValueError('The sequence must contain only A, T, C, G')
            else:
                the_sequence = ''.join([choice(NUCLEOTIDES) for _ in range(3 * int(length_or_stop))])
            print(the_sequence)
            print(extract_genes(the_sequence))
        except ValueError:
            print('You entered a non-STOP non-integer, try again. ')
        length_or_stop = input('How many codons do you want to create? (or stop to end, seq to enter your own sequence)')
