from collections import UserDict
from record import Record
from get_upcoming_bithday import get_upcoming_birthdays


class AddressBook(UserDict[str, Record]):
    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record

    def find(self, name: str) -> Record | None:
        return self.data.get(name)


    def delete(self, name: str) -> None:
        if name in self.data:
            del self.data[name]


    def get_upcoming_birthdays(self, days=7) -> str:
        users = [{"name": record.name.value, "birthday": record.birthday.value} for record in self.data.values() if record.birthday]
        upcoming = get_upcoming_birthdays(users, days)
        birsdays_str = "\n".join(f"{user['name']}'s congratulation date - {user['congratulation_date']}" for user in upcoming)
        
        return f"Upcoming birthdays in the next {days} days:\n{birsdays_str}" if birsdays_str else "No upcoming birthdays."


    def __str__(self) -> str:
        return "\n".join(str(record) for record in self.data.values())