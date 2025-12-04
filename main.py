import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(_file_), '..')))

from library_manager.inventory import LibraryInventory

def main():
    # Initialize inventory
    inventory = LibraryInventory()

    while True:
        print("\n--- Library Inventory Manager ---")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search by Title")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == '1':
                title = input("Enter Title: ")
                author = input("Enter Author: ")
                isbn = input("Enter ISBN: ")
                if title and author and isbn:
                    inventory.add_book(title, author, isbn)
                else:
                    print("All fields are required!")

            elif choice == '2':
                isbn = input("Enter ISBN to issue: ")
                results = inventory.search_by_isbn(isbn)
                if results:
                    book = results[0]
                    if book.issue():
                        print(f"Book '{book.title}' issued successfully.")
                        inventory.save_books()
                    else:
                        print("Book is already issued.")
                else:
                    print("Book not found.")

            elif choice == '3':
                isbn = input("Enter ISBN to return: ")
                results = inventory.search_by_isbn(isbn)
                if results:
                    book = results[0]
                    if book.return_book():
                        print(f"Book '{book.title}' returned successfully.")
                        inventory.save_books()
                    else:
                        print("Book was not issued.")
                else:
                    print("Book not found.")

            elif choice == '4':
                inventory.display_all()

            elif choice == '5':
                term = input("Enter title keyword: ")
                results = inventory.search_by_title(term)
                if results:
                    for b in results:
                        print(b)
                else:
                    print("No matching books found.")

            elif choice == '6':
                print("Exiting system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if _name_ == "_main_":
    main()
