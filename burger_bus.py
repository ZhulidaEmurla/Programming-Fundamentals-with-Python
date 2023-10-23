total_profit = 0
city_count = int(input())
for city_index in range(1, city_count + 1):
    city_name = input()
    income = float(input())
    expenses = float(input())
    if city_index % 3 == 0:
        expenses += expenses * 0.5

    if city_index % 5 == 0:
        income -= income * 0.1

    profit = income - expenses
    total_profit += profit
    print(f"In {city_name} Burger Bus earned {profit:.2f} leva.")
print(f"Burger Bus total profit: {total_profit:.2f} leva.")



