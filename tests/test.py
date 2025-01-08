import pytest
from app.main import Product, Order


def test_product_creation():
    product = Product("Laptop", 999.99, 10)
    assert product.name == "Laptop"
    assert product.price == 999.99
    assert product.stock == 10


def test_update_stock():
    product = Product("Laptop", 999.99, 10)
    product.update_stock(5)
    assert product.stock == 5

    with pytest.raises(ValueError):
        product.update_stock(6)  # Trying to reduce stock more than available


def test_order_add_item():
    order = Order()
    product = Product("Laptop", 999.99, 10)

    order.add_item(product, 2)
    assert order.items[product] == 2

    with pytest.raises(ValueError):
        order.add_item(product, 0)  # Invalid quantity


def test_order_process():
    product = Product("Laptop", 999.99, 10)
    order = Order()
    order.add_item(product, 2)
    order.process_order()

    # Check if stock is updated after order processing
    assert product.stock == 8
    assert order.total == 1999.98  # 2 * 999.99