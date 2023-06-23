class Private:
    def __init__(self):
        self._a = 10
        self.__a = 20

    def variables(self):
        print("var _a:", self._a)
        print("var __a:", self.__a)


obj = Private()
obj.variables()
print("var _a (direct):", obj._a)

# Error
# print("var __a (direct):", obj.__a)

print("var __a (name,class):", obj._Private__a)