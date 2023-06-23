# #1
class Car:
    def wheels(self):
        print(4)

    def mode_of_transport(self):
        print("Private usage")


class Bus:
    def wheels(self):
        print(8)

    def mode_of_transport(self):
        print("Public usage")


cars = Car()
bus = Bus()
objects = [cars, bus]

for transport in objects:
    transport.wheels()
    transport.mode_of_transport()


# #2

class Vehicle:
    def desc(self):
        print('vehicle')

    def wheels(self):
        print('2 or 4 wheels')


class Volvo(Vehicle):
    def desc(self):
        print('this is car')

    def wheels(self):
        print('car have 4 wheels')


class Motorcycle:
    def desc(self):
        print('enduro')

    def wheels(self):
        print('enduro have 2 wheels')


volvo = Volvo()
volvo.desc()
volvo.wheels()

enduro = Motorcycle()
enduro.desc()
enduro.wheels()
