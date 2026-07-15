"""""""""
"""
#----------------check weather no. is even or not------------------------
numb=int(input("enter your  number:-"))
print()
if(numb%2==0):
    print("your number is even no.")
else:
    print("your number is odd no")
    """

 #--------------------no. is divisible by 7 or not--------------------------
# numb=int(input("enter your number:-"))
# print()
# if(numb%7==0):
#     print("number is divisible by 7")
# else:
#  print("number is not div. by 7")
#=========================alphabet or not=================================
# chr=str(input("enter any alphabet:-"))
# if(chr>='a' and chr<='z'):
#     print("number is alphabet")
# else:
#     print("not a alphabet")
"""""   
====================lowercase or uppercase=====================================
chr=str(input("enter alphabet:-"))
if(chr>='a' and chr<='z'):
  print("alphabet is lower case ")
elif(chr>='A'and chr<='Z'):
  print("your alphabet is  uppercase")
else:
  print('not a alphabet')   
"""
#==============vowel or consonent==========================
'''
chr=str(input("enter your alphabet:-"))
if(chr=='a' or chr=='e' or chr=='i' or chr=='o' or chr=='u'or chr=='A'or chr=='E' or chr=='I'or chr=='O'or chr=='U'):
    print("it  is vowel")
else:
    print("it is consonent")
'''
# =====================largest two numbers==============================
# n1=int(input("enter number 1"))
# n2=int(input("enter number 2"))
# n3=int(input("enter number 3"))
# if(n1>n2 and n1>n3):
#     print("number 1 is largest")
# elif(n2>n3 and n2>n1):
#     print("number 2 is largest")
# else:
#     print("number 3 is largest")
'''      
**************************** [-finding percentage-] *******************************

sub1=int(input("enter your marks in hindi:-"))
sub2=int(input("enter your marks in maths:-"))
sub3=int(input("enter your marks in english:-"))
sub4=int(input("enter your marks in sst:-"))
sub5=int(input("enter your marks in science:-"))
if(sub1+sub2+sub3+sub4+sub5>=450):
      print("your grade is A+ ")
elif(sub1+sub2+sub3+sub4+sub5>=400):
      print("your grade is B+")
elif(sub1+sub2+sub3+sub4+sub5>=350):
      print("your grade is C") 
elif(sub1+sub2+sub3+sub4+sub5>=300):
      print("your grade is D") 
else:
      print("you are fail")                
'''       
#============================= CENTURY YEAR OR NOT  ==================================

#year=int(input("enter year : "))
#if(year%100==0):
#   print("it is a century year" )
#else:
#    print(" it is not a century year ")

#=============================== leap year or not ======================================
# year=int(input("enter year"))
# if(year%4==0):
#       print("it is a leap year")
# else:
#       ("not a leap year")      
#==================1-10  using loop=========================

'''
for i in range(1,11,1):
    print(i)
'''    
#=================even/odd number between 1-100====================
# for i in range(1,101,2):
#       print(i)
'''
for i  in range(0,101,2):
    print(i)
'''
#================divisible by 5 numbers btw. 1-100===================
'''
for i in range(0,101,5):
    print(i)
'''
"""
for i in range(1,101,1):
    if(i%5==0):
       print(i)
"""
#==============sum of n  natural numbers================
# sum=0
# for i in range(1,11,1):
#     sum=sum+i
# print(sum)
#==================factorial of n natural numbers====================
"""
"""
fact=1
for i in range(1,6,1):
    fact=fact*i
print(fact)    
"""