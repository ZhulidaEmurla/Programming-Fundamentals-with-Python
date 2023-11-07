products = {}

while True:
    command = input()
    if command == "buy":
        break

    product_name, price, quantity = command.split()
    price, quantity = float(price), int(quantity)

    if product_name not in products:
        products[product_name] = {'price': price, 'quantity': quantity}
    else:
        products[product_name]['price'] = price
        products[product_name]['quantity'] += quantity

for product, data in products.items():
    total_price = data['price'] * data['quantity']
    print(f"{product} -> {total_price:.2f}")
