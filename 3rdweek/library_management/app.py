from book import BookManager
from member import MemberManager
from issue import IssueManager
from reports import ReportManager


def show_books(books):
    if not books:
        print("No books found.")
        return

    for book in books:
        status = "Available" if book["available"] else "Borrowed"

        print(
            f'ID: {book["id"]} | '
            f'Title: {book["title"]} | '
            f'Author: {book["author"]} | '
            f'Status: {status}'
        )


def show_members(members):
    if not members:
        print("No members found.")
        return

    for member in members:
        status = "Active" if member["active"] else "Inactive"

        print(
            f'ID: {member["id"]} | '
            f'Name: {member["name"]} | '
            f'Email: {member["email"]} | '
            f'Status: {status}'
        )


def main():
    books = BookManager()
    members = MemberManager()
    issues = IssueManager(books, members)
    reports = ReportManager(books, members, issues)

    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add book")
        print("2. List books")
        print("3. Search books")
        print("4. Update book")
        print("5. Delete book")
        print("6. Register member")
        print("7. List members")
        print("8. Update member")
        print("9. Delete member")
        print("10. Issue book")
        print("11. Return book")
        print("12. Available books report")
        print("13. Borrowed books report")
        print("14. Top borrowers report")
        print("15. Fine report")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                title = input("Enter book title: ")
                author = input("Enter author: ")
                year = int(input("Enter publication year: "))

                book = books.add_book(title, author, year)
                print("Book added successfully:", book)

            elif choice == "2":
                show_books(books.list_books())

            elif choice == "3":
                keyword = input("Enter title, author, or ID: ")
                show_books(books.search_books(keyword))

            elif choice == "4":
                book_id = input("Enter book ID: ")
                title = input("New title (blank to skip): ")
                author = input("New author (blank to skip): ")
                year_text = input("New year (blank to skip): ")

                updated = books.update_book(
                    book_id,
                    title=title if title.strip() else None,
                    author=author if author.strip() else None,
                    year=int(year_text) if year_text.strip() else None,
                )

                print("Book updated:", updated)

            elif choice == "5":
                book_id = input("Enter book ID: ")
                books.delete_book(book_id)
                print("Book deleted successfully.")

            elif choice == "6":
                name = input("Enter member name: ")
                email = input("Enter email: ")

                member = members.register_member(name, email)
                print("Member registered:", member)

            elif choice == "7":
                show_members(members.list_members())

            elif choice == "8":
                member_id = input("Enter member ID: ")
                name = input("New name (blank to skip): ")
                email = input("New email (blank to skip): ")

                updated = members.update_member(
                    member_id,
                    name=name if name.strip() else None,
                    email=email if email.strip() else None,
                )

                print("Member updated:", updated)

            elif choice == "9":
                member_id = input("Enter member ID: ")

                # Production-quality validation should prevent deleting
                # members who have active borrowing records.
                members.delete_member(member_id)
                print("Member deleted successfully.")

            elif choice == "10":
                book_id = input("Enter book ID: ")
                member_id = input("Enter member ID: ")

                record = issues.issue_book(book_id, member_id)
                print("Book issued successfully:", record)

            elif choice == "11":
                book_id = input("Enter book ID: ")
                member_id = input("Enter member ID: ")

                result = issues.return_book(book_id, member_id)
                print("Book returned successfully.")
                print("Late days:", result["late_days"])
                print("Fine: ₹", result["fine"])

            elif choice == "12":
                show_books(reports.available_books())

            elif choice == "13":
                show_books(reports.borrowed_books())

            elif choice == "14":
                ranking = reports.top_borrowers()

                if not ranking:
                    print("No borrowing records yet.")

                for item in ranking:
                    print(
                        f'{item["name"]} (ID: {item["member_id"]}) - '
                        f'{item["books_borrowed"]} books borrowed'
                    )

            elif choice == "15":
                fine_records = reports.fine_report()

                if not fine_records:
                    print("No fines to report.")

                for item in fine_records:
                    status = (
                        "Returned" if item["returned"]
                        else "Not returned"
                    )

                    print(
                        f'Book ID: {item["book_id"]} | '
                        f'Member ID: {item["member_id"]} | '
                        f'Late days: {item["late_days"]} | '
                        f'Fine: ₹{item["fine"]} | '
                        f'Status: {status}'
                    )

            elif choice == "0":
                print("Thank you for using the library system.")
                break

            else:
                print("Invalid choice. Please select a valid option.")

        except (ValueError, KeyError) as error:
            print("Error:", error)

        except Exception as error:
            # Handles the project's custom LibraryError subclasses too.
            from exceptions import LibraryError

            if isinstance(error, LibraryError):
                print("Library error:", error)
            else:
                print("Unexpected error:", error)


if __name__ == "__main__":
    main()