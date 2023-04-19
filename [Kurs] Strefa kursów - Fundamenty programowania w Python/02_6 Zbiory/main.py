# x = set()
# print(x, type(x))
# y = set([1, 2, 3])
# print(y, type(y))
# z = {1, 2, 3}
# print(z, type(z))
# x = "sdfnsadkfjnsadkfasfd"
# y = set(x)
# print(x, type(x))
# print(y, type(y))
# z = sorted(y, key=x.index)
# print(z, type(z))
x = set([0, 1, 2, 3, 4, 5, 6])
y = set([3, 4, 5, 6, 7, 8, 9])
# z = x.union(y)
# print(z, type(z))
# a = x | y
# z = x.intersection(y)
# z = x & y
diff = x.difference(y)
diff = x - y
diff_sym = x.symmetric_difference(y)
diff_sym = x ^ y
print(diff, type(diff))
print(diff_sym, type(diff_sym))
