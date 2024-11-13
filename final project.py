class Product:
    def __init__(self, product_id, name, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.stock_quantity = stock_quantity

class InventoryManagementSystem:
    def __init__(self):
        self.products = {}
        self.current_user = None

    def login(self):
        username = input("Enter username (admin/user): ")
        password = input("Enter password: ")
        if username == "admin" and password == "adminpass":
            self.current_user = "admin"
            print("Welcome, Admin!")
        elif username == "user" and password == "userpass":
            self.current_user = "user"
            print("Welcome, User!")
        else:
            print("Invalid login!")

    def add_product(self):
        if self.current_user == "admin":
            product_id = input("Product ID: ")
            name = input("Product Name: ")
            stock_quantity = int(input("Stock Quantity: "))
            self.products[product_id] = Product(product_id, name, stock_quantity)
            print(f"Added: {name}")
        else:
            print("Only admin can add products.")

    def view_products(self):
        if self.products:
            for product in self.products.values():
                print(f"{product.product_id}: {product.name}, Stock: {product.stock_quantity}")
        else:
            print("No products available.")

def main():
    ims = InventoryManagementSystem()

    while True:
        action = input("Enter 'login' to log in, 'exit' to quit: ").strip().lower()
        if action == 'login':
            ims.login()
            while ims.current_user:
                command = input("Enter command (add/view/logout): ").strip().lower()
                if command == "add":
                    ims.add_product()
                elif command == "view":
                    ims.view_products()
                elif command == "logout":
                    ims.current_user = None
                    print("Logged out.")
                else:
                    print("Invalid command.")
        elif action == 'exit':
            break
        else:
            print("Invalid action. Please enter 'login' or 'exit'.")

if __name__ == "__main__":
    main()