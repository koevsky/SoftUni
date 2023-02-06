def shopping_cart(*products):

    cart = {"Pizza": [], "Dessert": [], "Soup": []}

    for item in products:

        if item == "Stop":
            if not cart["Pizza"] and not cart["Dessert"] and not cart["Soup"]:
                return "No products in the cart!"

            result = ""
            cart = sorted(cart.items(), key= lambda x: (-len(x[1]), x[0]))
            for name, prods in cart:
                result += f"{name}:\n"
                for meal in sorted(prods):
                    result += f" - {meal}\n"

            return result

        m, p = item

        if m == "Soup" and len(cart[m]) < 3 and p not in cart[m]:
            cart[m].append(p)

        elif m == "Pizza" and len(cart[m]) < 4 and p not in cart[m]:
            cart[m].append(p)

        elif m == "Dessert" and len(cart[m]) < 2 and p not in cart[m]:
            cart[m].append(p)




print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

