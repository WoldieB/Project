class Product:
    """
    This class represents a product with a name and price.
    """
    def __init__(self, name, price):
        """
        This method initializes a new Product object.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
        """
        self.name = name
        self.price = price


class ShoppingCart:
    """
    This class represents a shopping cart that can hold products and calculate their total price.
    """
    def __init__(self):
        """
        This method initializes a new ShoppingCart object.

        It creates an empty list to store items in the cart.
        """
        self.items = []

    def add_item(self, product, quantity):
        """
        This method adds a product to the shopping cart with a specified quantity.

        Args:
            product (Product): The product object to be added to the cart.
            quantity (int): The quantity of the product to be added.
        """
        self.items.append((product, quantity))

    def calculate_total(self):
        """
        This method calculates the total price of all items in the shopping cart.

        It iterates through each item in the cart, multiplies its price by quantity, and adds it to the total.

        Returns:
            float: The total price of all items in the cart.
        """
        total = 0
        for item in self.items:
            total += item[0].price * item[1]
        return total


# Product list
products = [
    Product("Apple", 3.50),
    Product("Banana", 0.75),
    Product("Orange", 1.80),
    Product("Pineapple", 1.50),
    Product("Tomato", 0.75),
    Product("Bread", 1.00),
    Product("Potato", 0.50),
    Product("Loxen", 2.50),
]

cart = ShoppingCart()

print("Welcome to our store! Here are the available products:")
for i, product in enumerate(products, 1):
    """
    This loop iterates through the product list and displays each product's name and price with numbering.
    """
    print(f"{i}. {product.name} - ${product.price}")

while True:
    choice = input("Enter the number of the product you would like to add to your cart (or 'done' to finish): ")

    if choice.lower() == 'done':
        break

    try:
        product_num = int(choice)
        if 1 <= product_num <= len(products):
            quantity = int(input("Enter the quantity: "))
            cart.add_item(products[product_num - 1], quantity)
            print(f"{products[product_num - 1].name} added to cart.")
        else:
            print("Invalid product number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid product number.")

total_price = cart.calculate_total()
print(f"Total price of your order: ${total_price}")


