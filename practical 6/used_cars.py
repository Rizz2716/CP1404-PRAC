
def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

main()
#
# from prac_06.car import Car
#
# def main():
#     """Demo test code to show how to use car class."""
#     limo = Car(100, "My limousine")
#     limo.add_fuel(20)
#     print("Limo fuel =", limo.fuel)
#     limo.drive(115)
#     print("odo =", limo.odometer)
#     print(limo)
#
#     print("Limo {}, {}".format(limo.fuel, limo.odometer))
#     print("Limo {self.fuel}, {self.odometer}".format(self=limo))
#
#
# main()