from typing import List, Tuple, Dict
from address_book import AddressBook
from record import Record


def input_error(func):
    def inner(*args, **kwargs) -> str:
        message = "Command is wrong or has wrong parameters."
        try:
            return func(*args, **kwargs)

        except ValueError as e:
            return e.args[0] if e.args else message
            
        except KeyError as e:
            return e.args[0] if e.args else message

        except IndexError as e:
            return e.args[0] if e.args else message

        except AttributeError as e:
            return e.args[0] if e.args else message

    return inner


@input_error
def add_contact(args, book: AddressBook):
    name, phone = args
    record = book.find(name)
    message = "Contact updated."

    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."

    if phone:
        record.add_phone(phone)

    return message


@input_error
def change_contact(args: List[str], book: AddressBook) -> str:
    name, old_phone, new_phone = args
    record = book.find(name)
    record.edit_phone(old_phone, new_phone)
    return "Contact updated."


@input_error
def show_phones(args: List[str], book: AddressBook) -> Record | str:
    name = args[0]
    record = book.find(name)
    return f"Phones for {name}: {'; '.join(p.value for p in record.phones)}" if record else "Contact not found."


@input_error
def get_all_contacts(book: AddressBook) -> AddressBook:
    return book


@input_error
def add_birthday(args: List[str], book: AddressBook) -> str:
    name, birthday = args
    record = book.find(name)

    if record is None:
        raise KeyError

    record.add_birthday(birthday)

    return "Birthday added."


@input_error
def show_birthday(args: List[str], book: AddressBook) -> str:
    name = args[0]
    record = book.find(name)

    if record.birthday is None: 
        return "Birthday not set for this contact."

    return f"{record.name.value}'s birthday is on {record.birthday.value.strftime('%d.%m.%Y')}."


@input_error
def show_upcoming_birthdays(args: List[str], book: AddressBook) -> str:
    days = int(args[0]) if len(args) else 7

    return book.get_upcoming_birthdays(days)
    

def parse_input(user_input: str) -> Tuple[str, List[str]]:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def phone_bot() -> None:
    print("Welcome to the assistant bot!")
    book = AddressBook()

    while True:
        user_input: str = input("Enter a command: ").strip()
        
        if not user_input:
            print("Please enter a command.")
            continue

        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phones(args, book))

        elif command == "all":
            print(get_all_contacts(book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(show_upcoming_birthdays(args, book))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    phone_bot()