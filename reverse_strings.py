while True:
    line = input()
    if line == "end":
        break
    reversed_line = line[::-1]
    print(f"{line} = {reversed_line}")
