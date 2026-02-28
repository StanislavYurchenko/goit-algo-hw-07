from phone import Phone
from name import Name
from birthday import Birthday


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones: list[Phone] = []
        self.birthday = None

    def __str__(self) -> str:
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday.value if self.birthday else 'N/A'}"

    def add_phone(self, phone: str) -> None:
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str) -> None:
        self.phones = [ph for ph in self.phones if ph.value != phone]

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        for i, ph in enumerate(self.phones):
            if ph.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return
        else:
            raise ValueError(f"Phone number {old_phone} not found in record for {self.name.value}") 

    def find_phone(self, phone: str) -> Phone | None:
        return next((ph for ph in self.phones if ph.value == phone), None)

    def add_birthday(self, birthday: str) -> None:
        self.birthday = Birthday(birthday)