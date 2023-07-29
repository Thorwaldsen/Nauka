from class_library import Person

person_one = Person("Joe", "Doe", "abc@gmail.com", "Potężny behemot")
person_one.print_person_information()

print("")

person_two = Person("Kamil", "Limak", "akalim@gmail.com", "Magiczny Kamil")
person_two.print_person_information()

person_three = person_one

print("")
print(person_one == person_two)

print("")

print(person_one)
print(person_two)
print(person_three)