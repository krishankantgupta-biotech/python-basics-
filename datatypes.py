#TYPES OF DATATYPES IN PYTHON 
"""There are various types in python like int, float, complex, string, list, tuple, set, dictionary etc."""
"ingteger data type store whole numbers like 1,2,3,4,5,6,7,8,9"
gene_count=23000
print(gene_count)
"float data type store decimal numbers like 1.5, 2.7, 3.14"
gc_content=0.5
ph=7.8
print(gc_content,ph)
"string data type store text or characters like 'hello', 'python', 'krishna'"
name="krishna"
print(name)
"boolean data type store True or False values"
dna="ATGGGGAUGTCGGAAA"
has_startcodon="AUG"in dna
print(has_startcodon)
dna2="ATGCATGGGGG"
has_startcodon2="AUG"in dna2
print(has_startcodon2)
"list data type store multiple values in a single variable like [1,2,3,4,5], ['a','b','c'], [1,'a',2,'b']"
dna_sequence=["ATG","GGA","AUG","TCG","GAA"]
print(dna_sequence)
gene=["BRCA1","TP53","EGFR"]
print(gene)
"tuple data type is similar to list but it is immutable, meaning its elements cannot be changed after creation"
gene_tuple=("BRCA1","TP53","EGFR")
print(gene_tuple)
"dictionary data type store key-value pairs like {'name':'krishna','age':19,'gender':'male'}"
gene_info={"gene_1":"BRCA1","gene_2":"TP53","gene_3":"EGFR"}
print(gene_info["gene_1"])
print(gene_info["gene_2"])
print(gene_info["gene_3"])
"set data type store unique values like {1,2,3,4,5}, {'a','b','c'}, {1,'a',2,'b'} but it is unordered and does not allow duplicate values"
gene_set={"BRCA1","TP53","EGFR","BRCA1"}
print(gene_set)
