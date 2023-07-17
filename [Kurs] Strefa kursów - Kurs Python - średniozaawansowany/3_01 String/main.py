# zmienne

one_line_string = "To jest string w jednej linii"

multi_line_string = """
To jest string, 
który jest w kilku liniach

może zawierać entery
          oraz spacje
"""

user = "ArturRosiek"

# print("%s" % (one_line_string))
# print("%s" % (multi_line_string))

# print("---------------------------")

# print("{} to jest pierwsza zmienna. {} to jest druga zmienna".format(one_line_string, multi_line_string))

# print(f" {one_line_string} to jest pierwsza zmienna. {multi_line_string} to jest druga zmienna")

pozycja_litery = multi_line_string.find('a')
# print("Pozycja {}".format(pozycja_litery))

# print("Pozycja 41 to: {}".format(multi_line_string[41]))

# print("Zmienna multi_line_string jest: {}".format(type(multi_line_string)))

# print("Nazwa Użytkowania w systemie Linux to: {}".format(user.lower()))

print("Rozdzielona\tTabem")
print("To pierwsza linia\nTo jest druga linia")
