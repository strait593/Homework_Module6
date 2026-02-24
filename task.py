from collections import UserDict


class InsufficientCharactersError(Exception):
    pass


class Field:
    def __init__(self, value):
        self.value = value

    # handles the conversion to str datatype
    def __str__(self) -> str:
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        super().__init__(name)


class Phone(Field):
    def __init__(self, phone):
        if len(str(phone)) < 10:
            raise InsufficientCharactersError("The phone number is too short.")
        super().__init__(phone)


class Record:
    # Handles the addition, removal and editing of phone numbers
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: list[Phone] = []

    def add_phone(self, value: str):
        self.phones.append(Phone(value))

    def remove(self, value: str):
        for phone in self.phones:
            if phone.value == value:
                self.phones.remove(phone)
                break

    def __str__(self) -> str:
        phones_str = "; ".join(p.value for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}"


class Addressbook(UserDict):
    # Handles the addition of contacts, searches based on name and removal of records
    def add_record(self, record: "Record"):
        self.data[record.name.value] = record

    def find(self, name: str):
        return self.data.get(name)

    def delete(self, name: str):
        if name in self.data:
            del self.data[name]

    def display_records(self) -> str:
        return "\n".join(str(record) for record in self.data.values())


"""
Use case for the code
"""

if __name__ == "__main__":
    book = Addressbook()

    dimon_record = Record("Dimon")
    dimon_record.add_phone("1231231234")
    dimon_record.add_phone("3213213210")
    book.add_record(dimon_record)

    jane_record = Record("Jane")
    jane_record.add_phone("1112223333")
    book.add_record(jane_record)

    print(book.display_records())