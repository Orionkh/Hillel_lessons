class PlaceHolder:
    pass


class OneParameter:
    counter = 55
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(f"My name {self.name}")

    @staticmethod
    def show_counter():
        print(OneParameter.counter)


a = OneParameter('Andrii')
print(a.print_name())
OneParameter.show_counter()

