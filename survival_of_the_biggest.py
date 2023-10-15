input_sequence = input()
n = int(input())
numbers = [int(num) for num in input_sequence.split()]
if n >= len(numbers):
    print("Cannot remove more numbers than the list contains.")
else:
    sorted_numbers = sorted(numbers)
    remaining_numbers = sorted_numbers[n:]
    result = ", ".join(map(str, remaining_numbers))
    print(result)

