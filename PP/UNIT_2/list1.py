import random

list1=[1,2,3,4,5]
list2=[1,1.5,1+4j]
list3=["red","green","blue"]
l1=list((1,2,3,4,5))
# list common operations

print(1 in list1) 
print(6 not in list1)
print(list1 + list2)
print(list1*2)
print(list2[2])
print(List1[1:2])
print(len(list1))
print(min(list1))
print(max(list1))
print(sum(list1))

#traversing list elements
print("*****************************")

for i in list1:
    print(i)

for j in list2:
    print(j,end=" ")

random.shuffle(list1)
print(list1)


#index operations
print("*****************************")

list4=[10,5,20,15,5,5,30,25,40,35,50,60]
print(list4[-1])
print(list4[-3])

# list Slicing
print("*****************************")
print(list4[2:4])
print(list4[:2])
print(list4[3:])
print(list4[1:-3])
print(list4[-4:-2])
print(list4[11:1])

#list Comparisions
print("*****************************")
list5=["red","green","blue"]
print(list3==list5)
print(list3!=list5)
print(list3>list5)

#list Comprehensions
print("*****************************")

list6=[ i for i in range(6)]
print(list6)
list7=(list6 ** 2 for x in list6)
print(list7)

#list methods
print("*****************************")

list4.append(50)
print(list4)
print(list4.count(5))
print(list1.extend(list2))
print(list4.index(4))
list4.insert(1,15)
print(list4)
list4.pop(8)
print(list4)
list4.remove(5)
print(list4)
list2.reverse()
print(list2)
print(list4.sort())

# splitting a string into a List
print("*****************************")
item="sree nidhi institute of technology"
item.split()
print(item)
