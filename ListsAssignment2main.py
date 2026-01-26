# Question 14: Find the sum of each sublist in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nQuestion 14: Find the sum of each sublist in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")

# Your code here

l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in l:
    print(sum(i))

# Question 15: Transpose the matrix [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nQuestion 15: Transpose the matrix [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
# Your code here
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range (0,len(matrix)):
    for j in range (0,len(matrix)):
        print(matrix[j][i],end=" ")
    print("\n")

# Question 16: Find the maximum value in each sublist of [[1, 5, 3], [9, 2, 7], [4, 8, 6]]
print("\nQuestion 16: Find the maximum value in each sublist of [[1, 5, 3], [9, 2, 7], [4, 8, 6]]")
# Your code here
for i in [[1, 5, 3], [9, 2, 7], [4, 8, 6]]:
    print(max(i))

# Question 17: Create a 3D list
print("\nQuestion 17: Create a 3D list: [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]")

three_d_list = [
    [[1, 2],[3, 4]],

    [[5, 6],[7, 8]]
]

for i in range (0,len(three_d_list)):
    for j in range (0,len(three_d_list)):
        for k in range (0,len(three_d_list)):
            print(three_d_list[i][j][k],end=" ")
        print("\n")

# Question 17: Create a 3D list
print("\nQuestion 17: Create a 3D list: [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]")

three_d_list =[
    [[1, 2],[3, 4]],

    [[5, 6],[7, 8]]
]

for i in range (0,len(three_d_list)):
    for j in range (0,len(three_d_list)):
        for k in range (0,len(three_d_list)):
            print(sum(three_d_list[i][j]),end=" ")
            break
        print("\n")

# Question 19: Extract all even numbers from nested list [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nQuestion 19: Extract all even numbers from nested list [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
# Your code here

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
even_numbers = []
for eachItem in nested_list:
 for number in eachItem:
        if number %2==0:
            even_numbers.append(number)
print(even_numbers)

# Question 20: Create a list of mixed data types: [1, "hello", 3.14, True, [1, 2, 3]]
print("\nQuestion 20: Create a list of mixed data types: [1, 'hello', 3.14, True, [1, 2, 3]]")
# Your code here
mixed_list = [1, "hello", 3.14, True, [1, 2, 3]]
for item in mixed_list:
    print(f"{item} is of type {type(item)}")

# Question 21: Find the length of each string in ["apple", "banana", "cherry", "date"]
print("\nQuestion 21: Find the length of each string in ['apple', 'banana', 'cherry', 'date']")
# Your code here

string_list = ['apple', 'banana', 'cherry', 'date']

for i in string_list:
    print(len(i))

# Question 22: Create a list of tuples: [(1, 'a'), (2, 'b'), (3, 'c')]
print("\nQuestion 22: Create a list of tuples: [(1, 'a'), (2, 'b'), (3, 'c')]")
# Your code here

tuple_list = [(1, 'a'), (2, 'b'), (3, 'c')]
print(tuple_list)

# Question 23: Extract first element from each tuple in [(1, 'a'), (2, 'b'), (3, 'c')]
print("\nQuestion 23: Extract first element from each tuple in [(1, 'a'), (2, 'b'), (3, 'c')]")
# Your code here

tuple_list = [(1, 'a'), (2, 'b'), (3, 'c')]
for i in tuple_list:
    print(i[0])

# Question 24: Create a list of dictionaries: [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
print("\nQuestion 24: Create a list of dictionaries: [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]")
# Your code here
dict_list = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
for person in dict_list:
    print(f"{person['name']} is {person['age']} years old.")

# Question 25: Extract all 'name' values from list of dictionaries
print("\nQuestion 25: Extract all 'name' values from list of dictionaries")
# Your code here
dict_list = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
for eachItem in dict_list:
    print(eachItem['name'])

# Question 26: Find the person with maximum age in list of dictionaries
print("\nQuestion 26: Find the person with maximum age in list of dictionaries")
# Your code here
max_age = 0
dict_list = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
for eachItem in dict_list:
    if eachItem['age']>max_age:
        max_age=eachItem['age']
        person_name=eachItem['name']
print(f"The Oldest Person is : {person_name} with age {max_age}")
##(f"The oldest person is {person_name} with age {max_age}.")

# Question 27: Create a 4D list: [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]]
print("\nQuestion 27: Create a 4D list: [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]]")
# Your code here
list_4d = [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]]
print(list_4d)

# Question 28: Find the maximum value in 4D list
print("\nQuestion 28: Find the maximum value in 4D list")
# Your code here
max = 0

for a in list_4d:
    for b in a:
        for c in b:
            for d in c:
                if d>max:
                    max=d
print(f"The Maximum value in 4D list is : {max}")

# Question 29: Create a list of sets: [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}]
print("\nQuestion 29: Create a list of sets: [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}]")
# Your code here
set_list = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}]
print(set_list)

# Question 30: Find the union of all sets in list of sets
print("\nQuestion 30: Find the union of all sets in list of sets")
# Your code here
union_set = set()
for s in set_list:
    union_set = union_set.union(s)      
print(union_set)

# Question 31: Create a list of complex numbers: [1+2j, 3+4j, 5+6j]
print("\nQuestion 31: Create a list of complex numbers: [1+2j, 3+4j, 5+6j]")
# Your code here

complex_list = [1+2j, 3+4j, 5+6j]
for num in complex_list:        
    print(num)

# Question 32: Find the magnitude of each complex number in list
print("\nQuestion 32: Find the magnitude of each complex number in list")
# Your code here
