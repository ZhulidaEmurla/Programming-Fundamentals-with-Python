sequence = list(map(int, input().split()))

while True:
    command = input().split()

    if command[0] == "Finish":
        break

    if command[0] == "Add":
        value = int(command[1])
        sequence.append(value)

    elif command[0] == "Remove":
        value = int(command[1])
        if value in sequence:
            sequence.remove(value)

    elif command[0] == "Replace":
        value, replacement = int(command[1]), int(command[2])
        if value in sequence:
            index = sequence.index(value)
            sequence[index] = replacement

    elif command[0] == "Collapse":
        value = int(command[1])
        sequence = [num for num in sequence if num >= value]

print(" ".join(map(str, sequence)))
