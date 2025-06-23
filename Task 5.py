def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers."
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def fibonacci(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Example usage
num = 7  # You can change this value for testing

print(f"Factorial of {num}:", factorial(num))
print(f"Fibonacci series up to {num} terms:", fibonacci(num))
print(f"Is {num} a prime number?:", "Yes" if is_prime(num) else "No")
