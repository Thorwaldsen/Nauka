# lista w języku python zapisana jest za pomocą - []

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
my_list2 = ["Slowo", "a", "s d d ", 3, 5]
my_index = len(my_list) - 1
print(my_list[my_index])
print("Index: {}".format(my_index))

my_string = "To jest przykładowy string"
print(my_string[0])

# Sring 'str' object does not support item assigment!
# my_string[0] = "c"

my_list[0] = 0
print(my_list[0])
print(my_list)
print(my_list[1:11:2])
print(my_list[0:-1])

my_list.append('D')
my_list.append('F')
print(my_list)

my_list.remove(2)
print(my_list)
my_list.remove('D')
print(my_list)

my_list.pop()
print(my_list)
my_list.pop()
print(my_list)

my_list[1:3] = ['A', 'B']
print(my_list)
my_list[1:3] = ['A', 'B', 'C', 'D']
print(my_list)

my_list[5:] = []
print(my_list)

my_list += my_list2
print(my_list)