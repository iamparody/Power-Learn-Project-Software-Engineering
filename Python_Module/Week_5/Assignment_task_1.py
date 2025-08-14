class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand      # Encapsulation: attributes are private to the class
        self.model = model
        self.storage = storage  # in GB

    def call(self, number):
        return f"Calling {number} from {self.brand} {self.model}..."

    def take_photo(self):
        return "Photo taken with standard camera."

    def __str__(self):
        return f"{self.brand} {self.model} ({self.storage}GB)"

class FlagshipSmartphone(Smartphone):
    def __init__(self, brand, model, storage, camera_resolution):
        super().__init__(brand, model, storage)
        self.camera_resolution = camera_resolution  # in MP

    # Polymorphism: Overriding the take_photo method
    def take_photo(self):
        return f"Photo taken with {self.camera_resolution}MP ultra HD camera!"

    # Additional method for flagship features
    def face_unlock(self):
        return "Phone unlocked using facial recognition."

# Example usage
if __name__ == "__main__":
    phone1 = Smartphone("Nokia", "3310", 16)
    print(phone1)
    print(phone1.call("1234567890"))
    print(phone1.take_photo())

    phone2 = FlagshipSmartphone("Samsung", "Galaxy S25", 256, 108)
    print(phone2)
    print(phone2.call("9876543210"))
    print(phone2.take_photo())
    print(phone2.face_unlock())
