budget = float(input())
price_for_one_kg_flour = float(input())
bread_count = 0
colored_eggs = 0
budget_left = 0
pack_of_eggs = 0
flour = 0
milk = 0

price_for_one_pack_eggs = price_for_one_kg_flour * 0.75
price_for_one_litre_milk = (price_for_one_kg_flour * 0.25 + price_for_one_kg_flour) / 4
total_price = price_for_one_kg_flour + price_for_one_pack_eggs + price_for_one_litre_milk

while budget > 0:
    milk += 1
    pack_of_eggs += 1
    flour += 1
    for _ in range(pack_of_eggs):
        milk -= 1
        pack_of_eggs -= 1
        flour -= 1
        bread_count += 1
        colored_eggs += 3
        budget -= total_price
        budget_left = budget

    if bread_count % 3 == 0:
        colored_eggs -= bread_count - 2

    if budget_left < total_price:
        break

print(f"You made {bread_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget_left:.2f}BGN left.")


