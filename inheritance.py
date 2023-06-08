class OneParameter:
    counter = 55

    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(f'My name {self.name}')

    @staticmethod
    def show_counter():
        print(OneParameter.counter)


class SecondParameter(OneParameter):
    def __init__(self, name, url):
        OneParameter.__init__(self, name)
        self.url = url

    def get_url(self):
        print(f'Search page is {self.url}')


a = SecondParameter('https', 'GOOGLE')
print(a.get_url())
print(a.print_name())
