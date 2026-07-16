# Operators are special symbols that perform operations on variables and values. In Python, we have several types of operators, including arithmetic, comparison, logical, assignment and membership operators.
""" 1. Arithmetic Operators: These operators are used to perform mathematical operations like addition(+), subtraction(-), multiplication(*), division(/), floor division(//), remainder(%) and power(**), """
"CALCULATING GC CONTENT OF DNA SEQUENCE"
gc=48
length=80
gc_percentage=(gc/length)*100
print("percentage of gc content is:-",gc_percentage)
" COMPLETE CODON CAN BE FORMED OR NOT"
sequence_length=305
print("complete codon can be formed only if the length of the sequence is divisible by 3 hence these are extra nucleotides present :-",sequence_length%3)
""" 2. Comparison Operators: These operators are used to compare two values and return a boolean value (True or False). The comparison operators in Python are: equal to (==), not equal to (!=), greater than (>), less than (<), greater than or equal to (>=), and less than or equal to (<=). """
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~
expected_length=300
actual_length=300
print(expected_length==actual_length)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~
dna="ATGCGTA"
print(dna=="ATGCGTA")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
gene = "BRCA1"
print(gene == "TP53")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~
gene = "BRCA1"
print(gene != "TP53")
""" 3. Membership Operators: These operators are used to test whether a value is present in a sequence (like a list, tuple, or string). The membership operators in Python are: in and not in. """
dna_sequence = "ATGCGTA"
print("ATGC" in dna_sequence)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~
dna_sequence = "AATGCCCACGTTT"
print("ATGC" not in dna_sequence)
""" 4. Logical Operators: These operators are used to combine multiple conditions and return a boolean value (True or False). The logical operators in Python are: and, or, and not. """
sequence="ATGCGTA"
print("ATG" in sequence and "GTA" in sequence)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
sequence="ATGCGTA"
print("ATG" in sequence or "TTT" in sequence)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
sequence="ATGCGTA"
print(not "TTT" in sequence)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
sequence="ATGCGTA"
print("ATG" in sequence and "TTT" in sequence)
""" 5. Assignment Operators: These operators are used to assign values to variables. The assignment operators in Python are: =, +=, -=, *=, /=, //=, %=, **=, and &=. """
total_length=0
fragment_length=100
total_length+=fragment_length
print(total_length)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
dna_sequence="ATGCGTA"
new_sequence="TCA"
dna_sequence+=new_sequence
print(dna_sequence)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
dna_sequence2="ATGCGTATTT"
dna_sequence2*=2
print(dna_sequence2)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
dna_length=100
fake_length=20
dna_length-=fake_length
print(dna_length)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
dna_content=100
non_gc_content=20
dna_content/=non_gc_content
print(dna_content)
