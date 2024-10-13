# Function to generate Fibonacci series up to n terms
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Example: Generate first 10 Fibonacci numbers
n = 10
fib_sequence = fibonacci(n)
print(f"Fibonacci series up to {n} terms: {fib_sequence}")
