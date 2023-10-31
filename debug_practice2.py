# debug_example.py

def find_largest(numbers):
    largest = numbers[0]  # Initialize with the first number
    for number in numbers:
        if number > largest:
            largest = number
    return largest

def main():
    numbers = [17, 42, 5, 8, 31, 22]
    result = find_largest(numbers)  # Set a breakpoint here
    print(f"The largest number is: {result}")

if __name__ == "__main__":
    main()

