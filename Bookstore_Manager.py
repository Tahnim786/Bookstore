import datetime

# Define classes to represent different entities

class Book:
    def __init__(self, title, author, genre, price, stock):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.stock = stock

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.purchased_books = []

class Order:
    def __init__(self, customer, books):
        self.customer = customer
        self.books = books
        self.order_date = datetime.datetime.now()

# Bookstore class to manage interactions

class Bookstore:
    def __init__(self):
        self.books = []       # List to store book objects
        self.customers = []   # List to store customer objects
        self.orders = []      # List to store order objects

    # Method to add a new book to the inventory
    def add_book(self, title, author, genre, price, stock):
        book = Book(title, author, genre, price, stock)
        self.books.append(book)
        print("Book added successfully.")

    # Method to add a new customer to the customer list
    def add_customer(self, name, email):
        customer = Customer(name, email)
        self.customers.append(customer)
        print("Customer added successfully.")

    # Method to place an order
    def place_order(self, customer_name, book_titles):
        customer = next((c for c in self.customers if c.name == customer_name), None)
        if customer:
            # Find book objects based on titles
            books = [book for book in self.books if book.title in book_titles]
            if books:
                # Create an order and update inventory and customer's purchased books
                order = Order(customer, books)
                self.orders.append(order)
                for book in books:
                    book.stock -= 1
                    customer.purchased_books.append(book)
                print("Order placed successfully.")
            else:
                print("Some books are not available in the inventory.")
        else:
            print("Customer not found.")

    # Method to view orders
    def view_orders(self):
        if self.orders:
            for order in self.orders:
                print(f"Order Date: {order.order_date}")
                print(f"Customer: {order.customer.name}")
                print("Books:")
                for book in order.books:
                    print(f"- {book.title}")
                print("-" * 20)
        else:
            print("No orders found.")

# Main function to interact with the bookstore management system

def main():
    bookstore = Bookstore()

    while True:
        print("\nBookstore Management Menu:")
        print("1. Add Book")
        print("2. Add Customer")
        print("3. Place Order")
        print("4. View Orders")
        print("5. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            genre = input("Enter book genre: ")
            price = float(input("Enter book price: "))
            stock = int(input("Enter stock quantity: "))
            bookstore.add_book(title, author, genre, price, stock)
        elif choice == "2":
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            bookstore.add_customer(name, email)
        elif choice == "3":
            customer_name = input("Enter customer name: ")
            book_titles = input("Enter book titles (comma-separated): ").split(",")
            bookstore.place_order(customer_name, book_titles)
        elif choice == "4":
            bookstore.view_orders()
        elif choice == "5":
            print("Exiting Bookstore Management System.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
