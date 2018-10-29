matrix1=[]
matrix2=[]
result=[]
import random
rows,cols=eval(input("enter rows,cols for matrix"))

for row in range(rows):
      matrix1.append([])
      for col in range(cols):
        matrix1[row].append(random.randint(0,9))
for row in range(rows):
      matrix2.append([])
      for col in range(cols):
        matrix2[row].append(random.randint(0,9))
print("matrix1 values")
for row in matrix1:
    for value in row:
        print(value,end=" ")
    print()
print("matrix2 values")
for row in range(len(matrix2)):
    for col in range(len(matrix2[row])):
          print(matrix2[row][col],end=" ")
    print()

print("matrix addition")
for row in range(rows):
    result.append([])
    for col in range(cols):
        result[row].append(matrix1[row][col]+matrix2[row][col])

print("result values")
for row in result:
    for value in row:
          print(value,end=" ")
    print()
     
