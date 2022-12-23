import re
customer_pattern = r"%(\b[A-Z][a-z]+\b)%"
product_pattern = r"\<(\w+)\>"
count_pattern = r"\|(\d+)\|"
price_pattern = r"(([0]|[1-9][0-9]*)(\.\d+)?)\$"

total_income = 0

while True:
    line = input()
    if line == "end of shift":
        break
    customer = re.findall(customer_pattern, line)
    product = re.findall(product_pattern, line)
    count = re.findall(count_pattern, line)
    price = re.findall(price_pattern, line)
    if customer and product and count and price:
        customer = customer[0]
        product = product[0]
        count = int(count[0])
        price = price[0][0]
        if "." in price:
            price = float(price)
        else:
            price = int(price)
        total_income += price*count
        print(f"{customer}: {product} - {(price*count):.2f}")

print(f"Total income: {total_income:.2f}")
