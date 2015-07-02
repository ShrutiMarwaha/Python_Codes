__author__ = 'shruti'
#dna_string = "AAAACCCGGT"
dna_string = "CCAGGGCCTAACAATATCGAGTCCAGATGATGCTTCGATTTTTCCCCTTAGCGACTACACGGGGCAACTTGACTCGGCCACTCGCCACGTCCGTTTATCCTGTACTTCGTCAATTTAAAGTATACCCTTCGTTTCCTTTCCACATCCAGCGTGGGGCTACTTGTTGTGATCTTACTACACAGTATGAATGGGTATAGCTCACTGCTTGGGCAACTAAGTTTCCGCCACCGTCACGGCCACACTCCCAACACCACATACAGAGTTACCCTACTAAGATGGGACCACGAATTTATTCCCCTTGTAGGATCTGAATCATTTGAACACCCATAGACCGGGAAACCTATAGGAGTTGTCCGATCGCGATGTTGTCATCCACCGCAGGCTACCGTGGATACTTTAAAGACGACCAGGACCTCATTCAAACATGTTAAACCGTGGTACTTCATTAAGATCTCGATACTGCTGAAGGGGTCCGCATCGTCTACTTTGTATGCCAGTTATTATGATAAGAACGACGGTGTAACTAAGCAAGGAAGCAAACCAACACTCTGATAACTTCTCACGGCGTAAGGCTAAAGAGTGCTCTCTCACTGAGAGCCTAGCTTTGTTACTTACTGATGGCGCGTACATGATAAACTACTTGAGTTCGACTCAAGCGATCCGCTCCGTATTTCCGGGGTAAATTACCCCTGGACTTTTAAGTAGAACTACTCTCCCATTCCCGTGGAGGGCTCGGCGCGGTCTTTTGTAAACAGATAGCTGTGTGAATTATCGCGCGCACAAGGAAACTCGCATCAGTTCTACGGCAACAACAGCTTCACGGCTCTTCCGCCAAGCTGAGCAATCAGGTCTTAGCGTCGTTCGAGATTTTCTATATG"
dna_string = dna_string.upper()
# strings are immutable in python, so you can't change rna_sting in the loop later, so fist convert into an array
# use "list" to convert string to an array
complimentary_strand = list(dna_string)

dna_length = len(dna_string)
for i in range(0,dna_length):
    if dna_string[i]=="A":
        complimentary_strand[i]="T"
    elif dna_string[i]=="T":
        complimentary_strand[i]="A"
    elif dna_string[i]=="G":
        complimentary_strand[i]="C"
    elif dna_string[i]=="C":
        complimentary_strand[i]="G"

complimentary_strand = complimentary_strand[::-1]
print "DNA stand: " + dna_string
print "Complimentary stand: " + "".join(complimentary_strand)

