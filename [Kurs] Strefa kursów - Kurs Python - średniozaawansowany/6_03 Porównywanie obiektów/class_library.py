class Person:
    def __init__(self, name, surname, email, nickname):
        self.name = name
        self.surname = surname
        self.email = email
        self.nick = nickname

    def print_person_information(self):
        print(f"Name: {self.name}\nsurname: {self.surname}\nemail: {self.email}\nnick: {self.nick} ")
