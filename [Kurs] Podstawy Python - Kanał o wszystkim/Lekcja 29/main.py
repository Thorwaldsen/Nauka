class Test:
    __lista = []
    def dodaj(self, arg):
        self.__lista.append(arg)

    def zdejmij(self):
        if len(self.__lista) > 0:
            return self.__lista.pop(len(self.__lista) - 1)
        else:
            return

obj = Test()
obj.dodaj("A")
obj.dodaj("B")
obj.dodaj("C")
obj._Test__lista.append("X")
print(obj.zdejmij())
print(obj._Test__lista)