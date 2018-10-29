##Dictionary creation

# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}

# using dict()
my_dict = dict({1:'apple', 2:'ball'})

# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])

##Accessing Dictionary Elements

my_dict = {'name':'Jack', 'age': 26}

print(my_dict['name'])
print(my_dict.get('age'))

# my_dict.get('address')
# my_dict['address']

## Change or add the elements
my_dict = {'name':'Jack', 'age': 26}
my_dict['age'] = 27
print(my_dict)
my_dict['address'] = 'Downtown'  
print(my_dict)

## delete elements from the dictionary

# create a dictionary
squares = {1:1, 2:4, 3:9, 4:16, 5:25}  

# remove a particular item
print(squares.pop(4))  
print(squares)

# remove an arbitrary item
print(squares.popitem())
print(squares)

# delete a particular item
#del squares[5]  
print(squares)

# remove all items
squares.clear()

print(squares)

del squares

# Throws Error
# print(squares)

## Python Dictionary Comprehension

squares = dict({x: x*x for x in range(6)})
print(squares)

squares1 = {}
for x in range(6):
   squares1[x] = x*x

##Dictionary Membership Test
   squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

print(1 in squares)
print(2 not in squares)

# membership tests for key only not value
print(49 in squares)

##Iterating Through a Dictionary
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares:
    print(squares[i])
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

print(len(squares))
print(sorted(squares))
