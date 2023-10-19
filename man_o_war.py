pirate_ship = [int(section) for section in input().split(">")]
warship = [int(section) for section in input().split(">")]
max_health = int(input())

while True:
    command = input()
    if command == "Retire":
        break

    parts = command.split()
    action = parts[0]

    if action == "Fire":
        index, damage = int(parts[1]), int(parts[2])
        if 0 <= index < len(warship):
            warship[index] -= damage
            if warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                exit()
    elif action == "Defend":
        start, end, damage = int(parts[1]), int(parts[2]), int(parts[3])
        if 0 <= start <= end < len(pirate_ship):
            for i in range(start, end + 1):
                pirate_ship[i] -= damage
                if pirate_ship[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit()
    elif action == "Repair":
        index, health = int(parts[1]), int(parts[2])
        if 0 <= index < len(pirate_ship):
            pirate_ship[index] += health
            if pirate_ship[index] > max_health:
                pirate_ship[index] = max_health
    elif action == "Status":
        count = len([section for section in pirate_ship if section < 0.2 * max_health])
        print(f"{count} sections need repair.")

pirate_sum = sum(pirate_ship)
warship_sum = sum(warship)

if pirate_sum > 0 and warship_sum > 0:
    print(f"Pirate ship status: {pirate_sum}")
    print(f"Warship status: {warship_sum}")
else:
    print(f"Pirate ship status: {pirate_sum if pirate_sum > 0 else 0}")
    print(f"Warship status: {warship_sum if warship_sum > 0 else 0}")
