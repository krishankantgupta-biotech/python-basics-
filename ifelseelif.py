#~~~~~~~~~~~~~~~~~USING IF ELSE AND ELIF STATEMENTS~~~~~~~~~~~~~~~~~~~~~~~
gc_content=int(input("Enter the GC content of the DNA sequence :-"))
if gc_content > 50:
    print("RICH IN GC CONTENT")
elif gc_content < 50:
    print("LOW IN GC CONTENT")
else:
    print("AVERAGE IN GC CONTENT")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
nucleotide_count=int(input("ENTER THE NUCLEOTIDE COUNT OF THE DNA SEQUENCE :-"))
if nucleotide_count % 3 == 0:
    print(" complete codon can be formed")
else:
    print(" complete codon cannot be formed")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
dna_sequence=input("Enter the DNA sequence :-")
if "ATG" in dna_sequence :
    print("START CODON FOUND")
else:
    print("START CODON NOT FOUND")
