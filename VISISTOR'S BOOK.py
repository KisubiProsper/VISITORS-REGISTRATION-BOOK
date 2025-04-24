import csv
from datetime import datetime

def authenticate_user():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "Programmer" and password == "prosper256":
        
        print("Access granted!")
        return True 
    else:
        print("Invalid credentials! Access denied.")
        return False

def write_to_csv(data):
    with open("visitors_book.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data)
def search_by_name(name):
    try:
        with open("visitors_book.csv", mode="r") as file:
            reader = csv.reader(file)
            results = [row for row in reader if name.lower() in row[0].lower()]
            if results:
                print(f"Search Results for '{name}':")
                for result in results:
                    print(", ".join(result))
            else:
                print(f"No records found for the name '{name}'.")
    except FileNotFoundError:
        print("No visitor records found.")

def main():
    print("Welcome to the Fundi Bots Digital Visitor's Book!")
    
    while True:
        print("\nMenu:")
        print("1. Record a new entry")
        print("2. Search for previous entries")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")


        if choice == "1":
            name = input("Enter your full name: ")
            address = input("Enter your address: ")
            purpose = input("Enter the purpose of your visit: ")
            date_of_visit = input("Enter the date of your visit (YYYY-MM-DD): ")

            try:
                datetime.strptime(date_of_visit, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format! Please use YYYY-MM-DD.")
                continue

            contacts = input("Enter your contact information (phone/email): ")
            comment = input("Enter your comment or feedback: ")
            visitor_data = [name, address, purpose, date_of_visit, contacts, comment]
            write_to_csv(visitor_data)

            print("Thank you! Your details have been recorded.")

        elif choice == "2":
            search_name = input("Enter the name to search for: ")
            search_by_name(search_name)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please select 1, 2, or 3.")

if __name__ == "__main__":
    if authenticate_user():
        main()
    else:
        print("Exiting program.")

