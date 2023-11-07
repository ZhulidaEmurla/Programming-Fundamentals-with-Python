n = int(input())
parking = {}

for _ in range(n):
    command = input().split()
    action = command[0]
    username = command[1]

    if action == "register":
        license_plate = command[2]
        if username in parking:
            print(f"ERROR: already registered with plate number {parking[username]}")
        else:
            parking[username] = license_plate
            print(f"{username} registered {license_plate} successfully")

    elif action == "unregister":
        if username in parking:
            print(f"{username} unregistered successfully")
            del parking[username]
        else:
            print(f"ERROR: user {username} not found")

for username, license_plate in parking.items():
    print(f"{username} => {license_plate}")
