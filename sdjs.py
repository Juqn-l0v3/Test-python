INVENTORY_LIBRARY = { # THIS IS THE INVENTORY LIBRARY, IT CONTAINS A DICTIONARY WITH BOOKS, AUTHORS, CATEGORIES, PRICES AND QUANTITIES
    "Book1": ("Author1", "Fiction", 10.99, 100),
    "Book2": ("Author2", "Non-Fiction", 15.99, 50),
    "Book3": ("Author3", "Science", 12.50, 200),
    "Book4": ("Author4", "History", 20.00, 75),
    "Book5": ("Author5", "Fantasy", 18.75, 150),
}
def register_inventory(): # THIS IS THE SECTION TO REGISTER A BOOK, IT ASKS FOR THE BOOK NAME, AUTHOR, CATEGORY, PRICE AND QUANTITY
    book = input("Enter the book you want to add: ")
    author = input ("Enter the author: ")
    category = input ("Enter the category: ")
    price = float (input ("Enter the price of the book: "))
    quantity = int (input ("Enter the quantity: "))
    INVENTORY_LIBRARY[book] = (price, quantity, category, author)

    print ("Successful registration")


def search_book(): # THIS IS THE SECTION TO SEARCH FOR A BOOK, IT ASKS FOR THE BOOK NAME AND IF IT EXISTS, IT RETURNS THE PRICE, QUANTITY, CATEGORY AND AUTHOR
    book = input("Enter the name of the book you want to search for: ")
    if book in INVENTORY_LIBRARY:
        price, quantity, category, author = INVENTORY_LIBRARY[book]
        print(f"Book: {book}, Author: {author}, Category: {category}, Price: ${price:.2f}, Quantity: {quantity}")
    else:
        print("Book not found.")


def uptade_inventory(): # THIS IS THE SECTION TO UPDATE A BOOK, IT ASKS FOR THE BOOK NAME AND IF IT EXISTS, IT ALLOWS TO UPDATE THE PRICE AND QUANTITY
    book = input("Enter the name of the book you want to update: ")
    if book in INVENTORY_LIBRARY:
        price, quantity, category, author = INVENTORY_LIBRARY[book]
        while True:
            try:
                new_price = float(input(f"Enter the new price for {book} (current: ${price:.2f}): "))
                break
            except ValueError:
                print("Invalid entry, please enter a valid price.")
        while True:
            try:
                new_quantity = int(input(f"Enter the new quantity for {book} (current: {quantity}): "))
                break
            except ValueError:
                print("Invalid entry, please enter a valid quantity.")
        INVENTORY_LIBRARY[book] = (new_price, new_quantity, category, author)
        print(f"{book} has been updated successfully.")
    else:
        print("Book not found.")

def delete_books(): # THIS IS THE SECTION TO DELETE A BOOK, IT ASKS FOR THE BOOK NAME AND IF IT EXISTS, IT DELETES IT FROM THE INVENTORY
    book = input("Enter the name of the book you want to delete: ")
    if book in INVENTORY_LIBRARY:
        del INVENTORY_LIBRARY[book]
        print (f"The book {book} has been removed from inventory.")
    else:
        print("Product no found.")


SALES = {}

def register_sale(): # THIS IS THE SECTION TO REGISTER A SALE, IT ASKS FOR THE BOOK NAME, CUSTOMER NAME, STOCK SOLD, DATE AND DISCOUNT
    book = input("Enter the name of the book sold: ")
    if book not in INVENTORY_LIBRARY:
        print("Book not found in inventory.")
        return
    customer = input("Enter the name of the customer: ")
    while True:
        try:
            quantity = int(input("Enter the quantity sold: "))
            if quantity <= 0:
                raise ValueError("Quantity must be greater than zero.")
            break
        except ValueError as e:
            print(f"Invalid entry: {e}. Please enter a valid quantity.")
    date = input("Enter the date of sale (YYYY-MM-DD): ")
    while True:
        try:
            discount = float(input("Enter the discount percentage (0-100): "))
            if not (0 <= discount <= 100):
                raise ValueError("Discount must be between 0 and 100.")
            break
        except ValueError as e:
            print(f"Invalid entry: {e}. Please enter a valid discount percentage.")


def top_3_products():
    sales_count = {}
    for book, details in SALES.items():
        customer, quantity, date, discount = details
        if book in sales_count:
            sales_count[book] += quantity
        else:
            sales_count[book] = quantity
    sorted_sales = sorted(sales_count.items(), key=lambda x: x[1], reverse=True)
    top_three = sorted_sales[:3]
    print("Top 3 Best-Selling Books:")
    for book, count in top_three:
        print(f"Book: {book}, Quantity Sold: {count}")


def generate_total_sales_report():
    print("Total Sales Report:")
    for book, details in SALES.items():
        customer, quantity, date, discount = details
        price = INVENTORY_LIBRARY.get(book, (0, 0))[0]  # Get price from inventory or default to 0
        gross_income = price * quantity
        net_income = gross_income * (1 - discount / 100)
        print(f"Book: {book}, Customer: {customer}, Quantity Sold: {quantity}, Date: {date}, Discount: {discount}%, Gross Income: ${gross_income:.2f}, Net Income: ${net_income:.2f}")

def Calculate_net_and_gross_income():
    total_gross_income = 0
    total_net_income = 0
    for book, details in SALES.items():
        customer, quantity, date, discount = details
        price = INVENTORY_LIBRARY.get(book, (0, 0))[0]  # Get price from inventory or default to 0
        gross_income = price * quantity
        net_income = gross_income * (1 - discount / 100)
        total_gross_income += gross_income
        total_net_income += net_income
    print(f"Total Gross Income: ${total_gross_income:.2f}")
    print(f"Total Net Income: ${total_net_income:.2f}")


while True: # HERE I USE A CYCLE, SO THAT THE PROGRAM CONTINUES UNTIL THE SAME USER DECIDES TO EXIT THE PROGRAM
    print ("Menu options.")

    print ("1. Add book.")
    print ("2. Search book.")
    print ("3. Uptade book.")
    print ("4. Delete book.")
    print ("5. register sale.")
    print ("6. See the top 3 best-selling books.")
    print ("7. Generate report.")
    print ("8. Calcule income")
    print ("9. Exit.")

    options = input ("Select one option (1-9): ")
    if options == "1":
        register_inventory()
    elif options == "2":
        search_book()
    elif options == "3":
        uptade_inventory()
    elif options == "4":
        delete_books()
    elif options == "5":
        register_sale()
    elif options == "6":
        top_3_products()
    elif options == "7":
        generate_total_sales_report()
    elif options == "8":
        Calculate_net_and_gross_income()
    elif options == "9":
        print ("Bye, see you later!! ")
        break
    else: 
        print ("Just a number from 1 to 9! ")