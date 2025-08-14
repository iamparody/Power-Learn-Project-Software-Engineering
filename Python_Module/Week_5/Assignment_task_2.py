class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing ⛵"

# Function to demonstrate polymorphism
def start_moving(vehicle):
    print(vehicle.move())

# Example usage
if __name__ == "__main__":
    car = Car()
    plane = Plane()
    boat = Boat()

    start_moving(car)    # Output: Driving 🚗
    start_moving(plane)  # Output: Flying ✈️
    start_moving(boat)   # Output: Sailing ⛵
