"""
======================= LIST METHODS 0===================
``````````add data to list````````````
1..append(value):- adds data at the last
2.insert(index,value):- adds data at any index
3..extend(lst2):-adds new list to current list
"""
# ((((((((((((((((((((((((((((((   remove data from list   ))))))))))))))))))))))))))))))

# 1. .pop()/,pop(index):- remove data from the end 
# 2. .remove(value):- remove particular value
# 3. .clear:- remove all values  from list
# 4. del :- deletes all values

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
=> .sort() :- arrange data in accending order.
.sort(reverse=True) :- arrange data in decending order.

NOTE : inplace sorting.

=> sorted(lstName) : in accending order.
NOTE :- External sorting

=> max(lstName) :- return maximum valuein the list
=> min(lstName) :- return minimum valuein the list

=> .count(value) :-  return the total count of a value in the list.

=> .index(value) :- to get index value of the value.

=> .copy()

=> sum(lstName) :- return the sum of all values in the list.

=> reversed(lstName):- reverse the list.
"""
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#lst=[1,3,5,73,23,32,4,2,43,654,-383]
# lst.append(9)
# print(lst)

# # lst.pop()
# del lst[1:3]
# print(lst)

# lst2=[21,3,2,43,2,34,3,-483,54,-5,4,2,1,2,2,2,2,2,1,12,2]
# # lst2.sort(reverse=True)

# # lst3=sorted(lst2)

# # print(lst3)

# # print(max(lst2))
# # print(min(lst2))

# # print(lst2.count(2))

# # print(lst2.index(-483))

# # print(sum(lst))
# # l4=reversed(lst2)
# # for i in l4:
# #     print(i,end=",")

# ========================== ADDING ELEMENTS ================================ 

# lst1=['orange','red','green']
# lst1.append('blue')
# print(lst1)
lst=[1,1,2,2,2,2,2,2,24,4,5,5,5,6]
#lst.append(5)
lst.pop(5)
# print(lst)

# ======================== REMOVING ELEMENTS =====================

# lst2=['silver','gold','platinum','diamond']
# lst2.pop()
# print(lst2)

# =========== SORTING THE ELEMENTS ==================
# lst1=[1,3,7,9,0,-11,-22,456,234]
# lst1.sort()
# print(lst1)
# lst1.sort(reverse=True)
# print(lst1)

# ============ maximum and minimum ===============
# lst1=[1,3,7,9,0,-11,-22,456,234]
# print(max(lst1))
# print(min(lst1))
# ================tuple========================
"""
NOTE:- tuples are enclosed in a round bracket()
`````

Only  two  types of functions in tuple
```````````````````````````````````````

=> .count - counts number of values 
=> .index - determines place of index no.


# ============= SET ===============
"""
# NOTE :- set are enclosed in a curly bracket {}
# ````
# it has basically 6 types of functions:-
    
strvalue={1,2,3,45,7,8,"ram","shyam","hello dosto"}
# 1.st.add("raman")

# print(st)

s1={1,2,3,4,5,6,7,8}
s2={1,2,3,14,25,26,73,84}

# s3=s1.union(s2) or s1|s2 =>{1, 2, 3, 4, 5, 6, 7, 8, 73, 14, 84, 25, 26}
# s3=s1.intersection(s2) or s1&s2 =>{1, 2, 3}
# s3=s1.difference(s2) or s1-s2 =>{4, 5, 6, 7, 8}

# s3 = s1-s2 =>{4, 5, 6, 7, 8}

# s3 = s1&s2 => {1, 2, 3}
# s3= s1|s2 => {1, 2, 3, 4, 5, 6, 7, 8, 73, 14, 84, 25, 26}
# print(s3)