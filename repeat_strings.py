input_sequence = input().split()
final_string = ""

for string in input_sequence:
    repeated_string = string * len(string)
    final_string += repeated_string

print(final_string)
