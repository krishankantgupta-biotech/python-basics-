#===============FIBONACCI SERIES =============
# n1=0
# n2=1
# for  i in range(1,11,1):
#     print(n1)
#     temp=n1+n2
#     n1=n2
#     n2=temp

"""
************************* "MULTIPLICATION TABLE"*****************************

a=int(input(" table number:-"))
for i in range(1,11,1):
    print(f"{a}*{i}={a*i}")
"""
# #--------------------SUM OF EVEN AND ODD----------------------------
# sum=0
# for i in range(0,11,2):
#     sum=sum+i
# print(sum)    
#================odd=================
"""
sum=0
for i in range(1,11,2):
    sum=sum+i
print(sum)
"""
#^======================== FIBONACHI SERIES ==========================

# n1=0
# n2=1

# for i in range(1,10+1):
#     print(n1)
#     temp=n1+n2
#     n1=n2
#     n2=temp

    
"""
============================ ARMSTRONG NUMBER ========================

num=int(input("enter any number:- "))
power=(len(str(num)))
temp=num
sum=0


while(num>0):
    last_digit=num%10
    sum=sum+last_digit**power
    num=num//10

if(temp==sum):
   print("number is armstrong number ") 
else:
    ("not a armstrong ")       

"""
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^again^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
"""
num=(int(input("enter any number:-")))
power=len(str(num))
temp=num
sum=0
print()
while(num>0):
;    last_digit=num%10
    sum=sum+last_digit**power
    num=num//10

if(temp==sum):
    print("it is a armstrong number")
else:
    print("not a armstrong number")        
"""

# ~~~~~~~~~~~~~~~~~~~~~~~~again~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# num=int(input("enter a  number"))
# power=len(str(num))
# temp=num
# sum=0

# while(num>0):
#     last=num%10
#     sum=sum+last**power
#     num=num//10

# if(temp==sum):
#     print("armstrong") 
# else:
#     print("not a armstrong")    


#_------------------------------------again-----------------------_
"""
num=int(input("enter any number:-"))
power=len(str(num))
temp=num
sum=0
while(num<0):
    last=num%10
    sum=sum+last**power
    num=num//10
# if(sum==temp):
#     print("armstrong number")
# else:
#     print("not a armstrong no.")
# """
# num=int(input("enter any number "))
# power=len(str(num))
# temp=num
# sum=0

# while(num>0):
#     last_digit=num%10
#     sum=sum+last_digit**power
#     num=num//10

# if(temp==sum):
#    print("armstrong number ")

# else:
#     print("not armstrong number")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# num=int(input("enter number "))
# power=len(str(num))
# temp=num
# sum=0

# while(num>0):
#      last_number=num%10
#      sum=sum+last_number**power
#      num=num//10

# if(temp==sum):
#    print("armstrong number ")

# else:
#     print("not a armstrong number ")  

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ REVERSE THE NUMBER ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

# num=int(input("enter any number :- "))
# sum=0
# while(num>0):
#     last_digit=num%10
#     sum=sum*10+last_digit
#     num=num//10
# print(sum)

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ AGAIN ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# num=int(input(" enter any num :-"))
# sum=0

# while(num>0):
#     last_digit=num%10
#     sum=sum*10+last_digit
#     num=num//10
# print(sum)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ FIBONACHI SERIES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# n1=0
# n2=1

# for i in range(1,10+1):
#     print(n1)
#     temp=n1+n2
#     n1=n2
#     n2=temp
#===================================================C  PARRERN======================
"""
for row in range(1,7+1):
    for col in range(1,5+1):
        if(col==1):
            print("*",end=" ")
        elif(row==1) or (row==7):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()        
"""
#=================================E PATTERN============================
"""
for row in range(1,8):
    for col in range(1,6):
        if(col==1):
            print("*",end=" ")
        elif(row==1) or (row==4) or (row==7):
             print("*",end=" ")  
        else:
            print(" ",end=" ")
    print()
"""                   
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~K PATTERN~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
count1=3
count2=7
for row in range(1,8):
    for col in range(1,5):
        if(col==1):
            print("*",end=" ")
        elif(count1==):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()     
    """
#``````````````````````````````functions addition ```````````````````````````````

# def addition(a,b):
#  c=a+b
#  print(f"the sum of {a} and {b} is {c}")
# addition(11,12)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~NAME FOR FUNCTIONS~~~~~~~~~~~~~~~~~~~~~~~~
"""
def name(a):
    print(f"my name is {a}")
name("ram")
name("shyam")
"""

# def classes(c):
#     print(f"my class is {c}")
# classes("12th")
# classes("11th")
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!...FUNCTIONS SUBSTRACTION...!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# def subs(a,b):
#     c=a-b
#     print(f"the value after subs. of{b} from {a} is{c}")
# subs(20,10)


# =======================FACTORIAL OF TWO NUMBERS================================

# def fact(a,b):
#     c=a*b
#     print(f"the factorial of {a} and {b} is {c}")
# fact(10,10)
# fact(11,12)

# =======================function is even or odd check==================

# def num(a):
#     if (num%2==0):
#         print("even number")
#     else:
#         print("odd number") 
# print(f"num=290")       
# `````````````````` FIBONACHI SERIES ``````````````````````
"""
n1=0
n2=1
for i in range(1,11,1):
    print(n1)
    temp=n1+n2
    n1=n2
    n2=temp
"""
# ----------------- armstrong number-----------------
# num=int(input("enter any number:-"))
# power=(len(str(num)))
# temp=num
# sum=0
# while(num>0):
#     last_digit=num%10
#     sum=sum+last_digit**power
#     num=num//10
# if(temp==sum):
#     print(" its a armstrong nummber")
# else:
#     print("not a armstrong number")    

# ================================ fibonachi series ======================
# n1=0
# n2=1

# for i in range(1,20,1):
#     print(n1)
#     temp=n1+n2
#     n1=n2
#     n2=temp