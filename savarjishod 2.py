
    
rows, colmn = 7, 7
for i in range(rows):
    for j in range(colmn):
        if (i == 0 or i == rows - 1 or i == rows // 2) or (j == 0 or j == colmn - 1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

 
#  rows, colmn =  7,7
# for i in range(rows):
#     for j in range(colmn):
#         if i == 0 or rows-1 or j == 0 or j == colmn -1 or (i==rows//2):
#             print("*", end=" ")

#         else:
#             print(" " , end=" ")
#     print()

