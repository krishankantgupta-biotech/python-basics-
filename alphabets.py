#.................. X STRUCTURE..........................

count=5
for row in range(1,5+1):
    for col in range(1,5+1):
        if  (row==col):
            print("*",end=" ")
        elif(count==col):
            print("*",end=" ")
        else:
            print(" ",end=" ") 
    count-=1            
    print()
 
    #======================= Y STRUCTURE========================
# for row in range (1,8+1):
#     for col in range (1,6+1):
#         if (row==col) or (row<=4):
#             print("*",end=" ") 
#         elif(col==3) or (col<=4):
#             print("*",end=" ")
# print()