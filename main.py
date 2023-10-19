import json
import os
import uuid  # Импортиране на библиотеката uuid

class Customer:
    def __init__(self, name):
        self.id = str(uuid.uuid4())  # Генериране на уникален ИД
        self.name = name

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity

class Invoice:
    def __init__(self, customer):
        self.customer = customer
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_total(self):
        total = sum(product.calculate_total() for product in self.products)
        return total

    def generate_invoice(self):
        print("Фактура:")
        print(f"Име на клиент: {self.customer.name}")
        print(f"ИД на клиент: {self.customer.id}")
        for product in self.products:
            print(f"{product.name} - {product.quantity} x ${product.price:.2f} = ${product.calculate_total():.2f}")
        print(f"Крайна цена: ${self.calculate_total():.2f}")

    def save_to_json(self, filename):
        desktop_path = os.path.expanduser("~/Desktop")
        file_path = os.path.join(desktop_path, filename)

        invoice_data = {
            "customer": {
                "id": self.customer.id,
                "name": self.customer.name
            },
            "products": [
                {
                    "name": product.name,
                    "price": product.price,
                    "quantity": product.quantity
                }
                for product in self.products
            ],
            "total": self.calculate_total()
        }

        with open(file_path, "w") as json_file:
            json.dump(invoice_data, json_file, indent=4)

def main():
    print("Система за издаване на касови бележки")
    customer_name = input("Въведете име на клиента: ")
    customer = Customer(customer_name)
    invoice = Invoice(customer)

    while True:
        print("1. Добави продукт")
        print("2. Принтирай фактура")
        print("3. Запази в JSON файл")
        print("4. Изход")

        choice = input("Въведете избора си: ")

        if choice == "1":
            name = input("Въведете продукт: ")
            price = float(input("Въведете цена: "))
            quantity = int(input("Въведете количество: "))
            product = Product(name, price, quantity)
            invoice.add_product(product)
        elif choice == "2":
            invoice.generate_invoice()
        elif choice == "3":
            filename = input("Въведете име на JSON файл: ")
            invoice.save_to_json(filename)
            print(f"Фактурата е запазена в {filename}")
        elif choice == "4":
            break
        else:
            print("Опитайте отново. Невалиден избор!")

if __name__ == "__main__":
    main()
