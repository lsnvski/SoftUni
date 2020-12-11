def check_product(item, price):
    if item in total_products.keys():
        total_products[item][1] += price[1]
        price_input, price_dict = price[0], total_products[item][0]
        if price_input != price_dict:
            total_products[item][0] = price_input

        return True


products = input().split(" ")
total_products = {}

while products:

    if products[0] == "buy":
        break

    for prod in range(0, len(products), 3):
        prod_id, prod_price, prod_quantity = products[0], float(products[1]), int(products[2])
        if not check_product(prod_id, [prod_price, prod_quantity]):
            total_products[prod_id] = [prod_price, prod_quantity]
    products = input().split(" ")


for key, value in total_products.items():
    print(f'{key} -> {value[0] * value[1]:.2f}')