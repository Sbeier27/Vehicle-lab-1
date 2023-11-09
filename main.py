from turtledemo.chaos import f


class Car:
    def __init__(self, make, model, year, weight, num_doors):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.num_doors= num_doors

    def display_info(self):
        print (f"make: {self.make}\nmodel: {self.model}\nyear: {self.year}\nweight: {self.weight}\nnum_doors: {self.num_doors}")

    def honk(self):
        print("HONK")


class Boat:
    def __init__(self, make, model, year, weight, boat_type):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.boat_type = boat_type

    def display_info(self):
        print(
            f"make: {self.make}\nmodel: {self.model}\nyear: {self.year}\nweight: {self.weight}\nboat_type: {self.boat_type}")

    def honk(self):
        print("HRUNNNKKKKK")

class Truck:
    def __init__(self, make, model, year, weight, num_doors,payload_capacity):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.num_doors= num_doors
        self.payload_capacity = payload_capacity

    def display_info(self):
        print (f"make: {self.make}\nmodel: {self.model}\nyear: {self.year}\nweight: {self.weight}\nnum_doors: {self.num_doors}\npayload_capacity: {self.payload_capacity}")

    def honk(self):
        print("HJOOOOOOOOONNNNNNNNNNNKKKKKKKKKK")
    def dump_load(self):
        print("DUMPING LOAD")


if __name__ == "__main__":
    # Create instances of Vehicle Car
    car = Car("Toyota", "Corolla", 2021, 1275.0,4)
    truck= Truck("Mac", "Street 750", 2019, 220.0,4, 350) #<--- but this now takes truck's constructor.

    # Display information of the car
    print("Car Info:")
    car.display_info()
    car.honk()
    print()


    # Display information of the motorcycle
    print("Truck Info:")
    truck.display_info()
    truck.honk()
    print()

    # Show total number of vehicles created, if you are going for the Bonus

