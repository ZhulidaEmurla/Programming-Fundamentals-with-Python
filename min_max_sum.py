
input_sequence = input()

numbers = [int(num) for num in input_sequence.split()]


minimum_number = min(numbers)
maximum_number = max(numbers)
sum_of_numbers = sum(numbers)


print(f"The minimum number is {minimum_number}")
print(f"The maximum number is {maximum_number}")
print(f"The sum number is: {sum_of_numbers}")
