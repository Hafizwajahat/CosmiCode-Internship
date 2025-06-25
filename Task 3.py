# CREATE
fruits = ['apple', 'banana', 'cherry']

# READ
print("First fruit:", fruits[0])  # Output: apple

# UPDATE
fruits[1] = 'blueberry'

# DELETE
fruits.remove('cherry')  # or use del fruits[2]

print("Updated list:", fruits)






# CREATE
colors = ('red', 'green', 'blue')

# READ
print("Second color:", colors[1])  # Output: green

# UPDATE & DELETE (not allowed directly)
# Tuples are immutable, but you can convert them to a list:
colors_list = list(colors)
colors_list[1] = 'yellow'
colors = tuple(colors_list)
print("Updated tuple:", colors)






# CREATE
numbers = {1, 2, 3, 4}

# READ (loop through, no indexing)
for n in numbers:
    print("Set item:", n)

# UPDATE
numbers.add(5)

# DELETE
numbers.remove(2)  # or use discard(2) to avoid error if not present

print("Updated set:", numbers)





# CREATE
student = {
    'name': 'Alice',
    'age': 21,
    'grade': 'A'
}

# READ
print("Student name:", student['name'])

# UPDATE
student['age'] = 22

# DELETE
del student['grade']

# ADD
student['major'] = 'Computer Science'

print("Updated dictionary:", student)
