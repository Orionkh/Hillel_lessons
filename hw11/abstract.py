from abc import ABC, abstractmethod


# #1
class Class:
    @abstractmethod
    def abc_method(self):
        pass


_class = Class()


class NewClass(Class):
    def abc_method(self):
        print('Hi')


new_class = NewClass()

new_class.abc_method()


# #2
class ABCClass(ABC):
    @abstractmethod
    def abc_method(self):
        pass


# error
# _abc_class = ABCClass()


# #3
class ThirdClass(ABCClass):
    def abc_method(self):
        print('hi hi hi')


obj = ThirdClass()
obj.abc_method()