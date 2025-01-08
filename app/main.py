import random
import logging
from collections import defaultdict

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        if self.stock - quantity < 0:
            raise ValueError(f"Not enough stock for {self.name}. Available: {self.stock}")
        self.stock -= quantity
        logger.info(f"Stock for {self.name} updated. New stock: {self.stock}")

    def __str__(self):
        return f"{self.name} - ${self.price} (Stock: {self.stock})"


class Order:
    def __init__(self):
        self.items = defaultdict(int)  # Dictionary to store product and quantity
        self.total = 0

    def add_item(self, product, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        self.items[product] += quantity
        logger.info(f"Added {quantity} of {product.name} to the order.")

    def calculate_total(self):
        self.total = sum(product.price * quantity for product, quantity in self.items.items())
        logger.info(f"Total for the order: ${self.total:.2f}")
        return self.total

    def process_order(self):
        logger.info("Processing order...")
        for product, quantity in self.items.items():
            product.update_stock(quantity)
        self.calculate_total()


def create_product_catalog():
    return [
        Product("Laptop", 999.99, 10),
        Product("Smartphone", 499.99, 20),
        Product("Headphones", 89.99, 30),
        Product("Keyboard", 49.99, 50),
        Product("Monitor", 199.99, 15)
    ]


def display_inventory(catalog):
    logger.info("Inventory List:")
    for product in catalog:
        logger.info(f" - {product}")


def simulate_order(catalog):
    order = Order()
    
    # Simulate selecting random products and quantities
    for _ in range(random.randint(1, 5)):  # Randomly add 1 to 5 items to the order
        product = random.choice(catalog)
        quantity = random.randint(1, 3)  # Random quantity between 1 and 3
        try:
            order.add_item(product, quantity)
        except ValueError as e:
            logger.error(e)
    
    # Process the order
    try:
        order.process_order()
    except ValueError as e:
        logger.error(e)


def main():
    logger.info("Starting the E-commerce simulation...")
    
    # Create the product catalog
    catalog = create_product_catalog()
    
    # Display the initial inventory
    display_inventory(catalog)
    
    # Simulate an order
    simulate_order(catalog)
    
    logger.info("E-commerce simulation finished!")


if __name__ == "__main__":
    main()
