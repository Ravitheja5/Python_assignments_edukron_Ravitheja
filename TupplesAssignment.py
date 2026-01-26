# Question 1: Create a tuple of first 10 natural numbers
print("Question 1: Create a tuple of first 10 natural numbers")
# Your code here
natural_numbers = tuple(range(1, 11))
print(natural_numbers)

# Question 2: Find the length of tuple (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("\nQuestion 2: Find the length of tuple (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)")
# Your code here
tuple_example = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
length = len(tuple_example) 
print(length)

# Question 3: Access the 3rd element from tuple ('a', 'b', 'c', 'd', 'e')
print("\nQuestion 3: Access the 3rd element from tuple ('a', 'b', 'c', 'd', 'e')")
# Your code here
char_tuple = ('a', 'b', 'c', 'd', 'e')
third_element = char_tuple[2]   
print(third_element)    

# Question 4: Find the maximum value in tuple (23, 45, 12, 67, 34, 89, 56)
print("\nQuestion 4: Find the maximum value in tuple (23, 45, 12, 67, 34, 89, 56)")
# Your code here

num_tuple = (23, 45, 12, 67, 34, 89, 56)
max_value = max(num_tuple)
print(max_value)

# Question 5: Count how many times 5 appears in (1, 5, 2, 5, 3, 5, 4, 5, 6)
print("\nQuestion 5: Count how many times 5 appears in (1, 5, 2, 5, 3, 5, 4, 5, 6)")
# Your code here
count_tuple = (1, 5, 2, 5, 3, 5, 4, 5, 6)
count_5 = count_tuple.count(5)
print(count_5)  

# Question 6: Create a tuple of mixed data types (integer, float, string, boolean)
print("\nQuestion 6: Create a tuple of mixed data types (integer, float, string, boolean)")
# Your code here
mixed_tuple = (42, 3.14, "Hello, World!", True)
print(mixed_tuple)

# Question 7: Find the index of element 'python' in ('java', 'python', 'c++', 'javascript')
print("\nQuestion 7: Find the index of element 'python' in ('java', 'python', 'c++', 'javascript')")
# Your code here
lang_tuple = ('java', 'python', 'c++', 'javascript')
index_python = lang_tuple.index('python')
print(index_python)

# Question 8: Check if 25 exists in tuple (10, 20, 30, 40, 50)
print("\nQuestion 8: Check if 25 exists in tuple (10, 20, 30, 40, 50)")
# Your code here
check_tuple = (10, 20, 30, 40, 50)
exists_25 = 25 in check_tuple       
print(exists_25)

# Question 9: Create a tuple of first 5 even numbers
print("\nQuestion 9: Create a tuple of first 5 even numbers")
# Your code here
el = []

for i in range (1, 11):
    if i % 2 == 0:
        el.append(i)
even_numbers = tuple(el)
print(even_numbers)

# Question 10: Find the average of numbers in tuple (15, 23, 31, 42, 56, 78)
print("\nQuestion 10: Find the average of numbers in tuple (15, 23, 31, 42, 56, 78)")
# Your code here 

num_tuple = (15, 23, 31, 42, 56, 78)
average = sum(num_tuple) / len(num_tuple)   
print(average)
