matrix=[[1,2,3],[4,5,6],[7,8,9]]
for rows in range(len(matrix)):
    for cols in range(len(matrix[rows])):
       print(matrix[rows][cols], end=" ")
    print( )

print("**************************")
for row in matrix:
    for value in row:
        print(value, end=" ")
    print()
    

