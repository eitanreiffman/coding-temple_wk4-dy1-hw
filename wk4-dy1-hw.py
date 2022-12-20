# Exercise 1:
# Filter out all of the empty strings from the list below
# Output: ['Argentina', 'San Diego', 'Boston', 'New York']

places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

print(list(filter(lambda word: word.split(), places)))

# Exercise 2:
# Write an anonymous function that sorts this list by the last name
# Hint: Use the ".sort()" method and access the key
# Output: ['Victor aNisimov', 'Gary A.J. Bernstein', 'Joel Carter', 'Andrew P. Garfield', 'David hassELHOFF']

authors = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]

authors.sort(reverse=False, key=lambda author: author.lower().split()[-1])
print(authors)

# Exercise 3:
# Convert the list below from Celsius to Farhenheit
# Using the map function with a lambda
# Output: [('Nashua', 89.6), ('Boston', 53.6), ('Los Angeles', 111.2), ('Miami', 84.2)]
# F = (9/5)*C + 32

places = [('Nashua',32),("Boston",12),("Los Angeles",44),("Miami",29)]

print(list(map(lambda x: (x[0], (9/5) * x[1] + 32), places)))

# Exercise 4:
# Write a recursion function to perform the fibonacci sequence up to the number passed in.
# Output for fib(5) => 
# Iteration 0: 0
# Iteration 1: 1
# Iteration 2: 1
# Iteration 3: 2
# Iteration 4: 3
# Iteration 5: 5
# Iteration 6: 8

# Here's a function that outputs the fibonacci sequence without using recursion:

def fibonacci(x):
    f_list = []
    for num in range(x+1):
        if num <= 1:
            f_list.append(num)
        else:
            num = f_list[-1] + f_list[-2]
            f_list.append(num)
    return f_list

print(fibonacci(10))

# Exercise 5:
# Create a generator that takes a number argument and yields that number squared
# Then prints each number squared until zero is reached

def my_generator(number):
    while number > 0:
        yield number ** 2
        number -= 1

for x in my_generator(10):
    print(x)