
sequence = input().split()
moves = 0

while True:
    command = input()
    if command == "end":
        break

    index1, index2 = map(int, command.split())

    moves += 1

    if 0 <= index1 < len(sequence) and 0 <= index2 < len(sequence) and index1 != index2:
        if sequence[index1] == sequence[index2]:
            element = sequence[index1]
            sequence[index1] = sequence[index2] = None
            print(f"Congrats! You have found matching elements - {element}!")

            if all(element is None for element in sequence):
                print(f"You have won in {moves} turns!")
                break
        else:
            print("Try again!")
    else:
        middle_index = len(sequence) // 2
        sequence.insert(middle_index, f"-{moves}a")
        sequence.insert(middle_index, f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")

if not all(element is None for element in sequence):
    print(f"Sorry you lose :(\n{' '.join(filter(lambda e: e is not None, sequence))}")
