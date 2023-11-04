products = {}

while True:
    line = input()

    if line == "statistics":
        break

    product, quantity = line.split(": ")
    quantity = int(quantity)

    if product in products:
        products[product] += quantity
    else:
        products[product] = quantity

print("Products in stock:")
for product, quantity in products.items():
    print(f"- {product}: {quantity}")

total_products = len(products)
total_quantity = sum(products.values())

print(f"Total Products: {total_products}")
print(f"Total Quantity: {total_quantity}")
