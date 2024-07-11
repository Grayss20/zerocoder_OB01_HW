class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, name, price):
        self.items[name] = price

    def remove_item(self, name):
        del self.items[name]

    def get_price(self, name):
        if name in self.items:
            return self.items[name]
        else:
            return None

    def update_price(self, name, new_price):
        if name in self.items:
            self.items[name] = new_price
        else:
            print("Item not found")

    def info(self):
        print(f"Store: {self.name}")
        print(f"Address: {self.address}")
        print("Items:")
        for name, price in self.items.items():
            print(f"{name}: ${price}")


# Test code
store1 = Store("tesco", "123 Main Street")
store2 = Store("walmart", "456 Broad Street")
store3 = Store("amazon", "789 1st Avenue")

store1.add_item("apple", 0.99)
store1.add_item("banana", 0.50)
store1.add_item("orange", 0.75)
store1.add_item("milk", 1.99)
store2.add_item("orange", 0.75)
store2.add_item("milk", 1.99)
store3.add_item("bread", 0.99)
store3.add_item("eggs", 2.99)

store1.remove_item("apple")
store1.update_price("banana", 1.00)
print(f'Price of milk: ${store1.get_price("milk")}')
store1.info()
