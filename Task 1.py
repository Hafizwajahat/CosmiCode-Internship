print ('Hello, Data Science!')


# # # Program to input student marks, calculate average and assign grade

# # # Input number of subjects
# # num_subjects = int(input("Enter the number of subjects: "))

# # # Initialize total marks
# # total_marks = 0

# # # Loop to take marks input
# # for i in range(1, num_subjects + 1):
# #     mark = float(input(f"Enter mark for subject {i}: "))
# #     total_marks += mark

# # # Calculate average
# # average = total_marks / num_subjects

# # # Determine grade using if-else
# # if average >= 90:
# #     grade = 'A'
# # elif average >= 80:
# #     grade = 'B'
# # elif average >= 70:
# #     grade = 'C'
# # elif average >= 60:
# #     grade = 'D'
# # else:
# #     grade = 'F'

# # # Output results
# # print("\n--- Result ---")
# # print(f"Total Marks: {total_marks}")
# # print(f"Average Marks: {average:.2f}")
# # print(f"Grade: {grade}")







# # # CREATE
# # fruits = ['apple', 'banana', 'cherry']

# # # READ
# # print("First fruit:", fruits[0])  # Output: apple

# # # UPDATE
# # fruits[1] = 'blueberry'

# # # DELETE
# # fruits.remove('cherry')  # or use del fruits[2]

# # print("Updated list:", fruits)






# # # CREATE
# # colors = ('red', 'green', 'blue')

# # # READ
# # print("Second color:", colors[1])  # Output: green

# # # UPDATE & DELETE (not allowed directly)
# # # Tuples are immutable, but you can convert them to a list:
# # colors_list = list(colors)
# # colors_list[1] = 'yellow'
# # colors = tuple(colors_list)
# # print("Updated tuple:", colors)





# # # CREATE
# # numbers = {1, 2, 3, 4}

# # # READ (loop through, no indexing)
# # for n in numbers:
# #     print("Set item:", n)

# # # UPDATE
# # numbers.add(5)

# # # DELETE
# # numbers.remove(2)  # or use discard(2) to avoid error if not present

# # print("Updated set:", numbers)





# # # CREATE
# # student = {
# #     'name': 'Alice',
# #     'age': 21,
# #     'grade': 'A'
# # }

# # # READ
# # print("Student name:", student['name'])

# # # UPDATE
# # student['age'] = 22

# # # DELETE
# # del student['grade']

# # # ADD
# # student['major'] = 'Computer Science'

# # print("Updated dictionary:", student)








def string_manipulation(s):
    # Count vowels
    vowels = 'aeiouAEIOU'
    vowel_count = sum(1 for char in s if char in vowels)
    
    # Reverse the string
    reversed_s = s[::-1]
    
    # Check for palindrome (ignoring case)
    is_palindrome = s.lower() == reversed_s.lower()
    









# def factorial(n):
#     if n < 0:
#         return "Factorial not defined for negative numbers."
#     result = 1
#     for i in range(2, n + 1):
#         result *= i
#     return result

# def fibonacci(n):
#     series = []
#     a, b = 0, 1
#     for _ in range(n):
#         series.append(a)
#         a, b = b, a + b
#     return series

# def is_prime(n):
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True

# # Example usage
# num = 7  # You can change this value for testing

# print(f"Factorial of {num}:", factorial(num))
# print(f"Fibonacci series up to {num} terms:", fibonacci(num))
# print(f"Is {num} a prime number?:", "Yes" if is_prime(num) else "No")

