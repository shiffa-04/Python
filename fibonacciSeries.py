def generate_fibonacci(limit):
    fibonacci_sequence = [0, 1]
    while fibonacci_sequence[-1] + fibonacci_sequence[-2] <= limit:
        next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fibonacci)
    return fibonacci_sequence

def main():
    limit = int(input("Enter the limit for Fibonacci sequence generation: "))
    fibonacci_sequence = generate_fibonacci(limit)
    print("Fibonacci sequence up to limit {}:".format(limit))
    print(fibonacci_sequence)

if __name__ == "__main__":
    main()