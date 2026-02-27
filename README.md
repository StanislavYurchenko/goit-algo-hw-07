
# goit-algo-hw-07: Address Book Management System

A Python-based contact management system that allows users to store, organize, and manage contact information including names, phone numbers, and birthdays.

## Features

- **Contact Management**: Add, edit, find, and delete contacts
- **Phone Number Management**: Add, edit, remove, and find phone numbers for contacts
- **Birthday Tracking**: Store and retrieve contact birthdays
- **Upcoming Birthdays**: Get notifications for upcoming birthdays within a specified number of days
- **Data Validation**: Built-in validation for phone numbers and dates
- **Interactive CLI**: User-friendly command-line interface for easy interaction

## Project Structure

- **main.py** - Entry point for the application
- **phone_bot.py** - Interactive CLI bot for managing contacts
- **address_book.py** - `AddressBook` class for managing all records
- **record.py** - `Record` class representing individual contacts
- **field.py** - Base `Field` class for data validation
- **name.py** - `Name` class (validates contact names)
- **phone.py** - `Phone` class (validates 10-digit phone numbers)
- **birthday.py** - `Birthday` class (validates and formats dates)
- **get_upcoming_bithday.py** - Utility function for birthday notifications

## Requirements

- Python 3.10 or higher
- No external dependencies

## Usage

Run the application:
```bash
python main.py
```


## Commands

The CLI supports standard contact management operations:
- Add/edit/delete contacts
- Manage phone numbers
- Store and view birthdays
- Search for upcoming birthdays

## Author

Stanislav Yurchenko
