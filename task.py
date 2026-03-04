from collections import UserDict

class InsufficientCharactersError(Exception):
    pass
class InvalidCharacter(Exception):
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

        if str(phone).isalpha():
            raise InvalidCharacter("Invalid character entered.")

class Record:
    # Handles the addition, removal and editing of phone numbers
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: list[Phone] = []

    def add_phone(self, value: str):
        for char in value:
            if char.isalpha():
                raise InvalidCharacter("Letters can`t be a part of a phone number.")
        else:
            self.phones.append(Phone(value))

    def remove_phone(self, value: str):
        for phone in self.phones:
            if phone.value == value:
                self.phones.remove(phone)
                break
    
    def edit_phone(self, old_phone:str,updated_phone:str):
        phone_for_editing = self.find_phone(old_phone)

        if phone_for_editing:
            self.remove_phone(old_phone)
            self.add_phone(updated_phone)
        else:
            raise ValueError(f"Phone number {old_phone} does not exist.")
    
    def find_phone(self,value):
        for phone in self.phones:
            if phone.value == value:
                return phone
            
        return None

    def __str__(self) -> str:
        phones_str = "; ".join(p.value for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}"
    
class AddressBook(UserDict):
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
    
    def __str__(self):
        return str(self.display_records())

"""
Use case for the code
"""

if __name__ == "__main__":
    book = AddressBook()
    #Checking the functionality of Record class
    dimon_record = Record("Dimon")
    dimon_record.add_phone("1231231234")
    dimon_record.add_phone("3213213210")    #corrected, now, if i`ll try to add a letter, script will raise  an InvalidCharacter error
    dimon_record.edit_phone("1231231234", "5906064014")
    dimon_record.remove_phone("5906064014")
    print(dimon_record.find_phone("1111111111"))    #corrected
    book.add_record(dimon_record)

    jane_record = Record("Jane")
    jane_record.add_phone("1112223333")
    book.add_record(jane_record)
    print(book)