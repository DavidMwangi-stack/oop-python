# class Smartphone:
#     def __init__(self, brand, model, storage_gb, ram_gb, battery_mah):
#         self.brand = brand
#         self.model = model
#         self._storage_gb = storage_gb  # Encapsulated (protected by convention)
#         self._ram_gb = ram_gb      # Encapsulated (protected by convention)
#         self._battery_mah = battery_mah # Encapsulated (protected by convention)
#         self._is_on = False        # Encapsulated (private-like by convention)
#         self._apps_installed = []  # Encapsulated (private-like by convention)

#     def power_on(self):
#         if not self._is_on:
#             self._is_on = True
#             print(f"{self.brand} {self.model} is powering on...")
#         else:
#             print(f"{self.brand} {self.model} is already on.")

#     def power_off(self):
#         if self._is_on:
#             self._is_on = False
#             print(f"{self.brand} {self.model} is powering off...")
#         else:
#             print(f"{self.brand} {self.model} is already off.")

#     def install_app(self, app_name):
#         if app_name not in self._apps_installed:
#             self._apps_installed.append(app_name)
#             print(f"{app_name} installed on {self.brand} {self.model}.")
#         else:
#             print(f"{app_name} is already installed.")

#     def uninstall_app(self, app_name):
#         if app_name in self._apps_installed:
#             self._apps_installed.remove(app_name)
#             print(f"{app_name} uninstalled from {self.brand} {self.model}.")
#         else:
#             print(f"{app_name} is not installed.")

#     def get_storage_info(self):
#         return f"Storage: {self._storage_gb} GB"

#     def get_ram_info(self):
#         return f"RAM: {self._ram_gb} GB"

#     def _check_battery(self): # Encapsulated (private-like by convention)
#         if self._battery_mah < 2000:
#             print("Battery level is low.")
#         else:
#             print("Battery level is good.")

#     def use_camera(self):
#         if self._is_on:
#             print(f"{self.brand} {self.model}: Camera activated.")
#             self._check_battery()
#         else:
#             print("Please power on the phone first.")

#     def __repr__(self):
#         return f"{self.brand} {self.model} (Storage: {self._storage_gb}GB, RAM: {self._ram_gb}GB, Battery: {self._battery_mah}mAh)"

# # Creating instances of the Smartphone class
# phone1 = Smartphone("Samsung", "Galaxy S23", 256, 8, 3900)
# phone2 = Smartphone("Apple", "iPhone 15", 128, 6, 3274)

# print(phone1)
# print(phone2)

# phone1.power_on()
# phone1.install_app("Instagram")
# phone1.install_app("WhatsApp")
# phone1.use_camera()
# phone1.power_off()

# phone2.power_on()
# phone2.uninstall_app("TikTok") # Not installed yet
# phone2.power_off()

# print(phone1.get_storage_info())
# # print(phone1._battery_mah) # Accessing "protected" attribute (not recommended)

# # adding an inheritance layer to explore polymorphism:
# class GamingSmartphone(Smartphone):
#     def __init__(self, brand, model, storage_gb, ram_gb, battery_mah, cooling_system):
#         super().__init__(brand, model, storage_gb, ram_gb, battery_mah)
#         self.cooling_system = cooling_system
#         self._performance_mode = False # Encapsulated

#     def enable_performance_mode(self):
#         if self._is_on:
#             self._performance_mode = True
#             print(f"{self.brand} {self.model}: Performance mode enabled. {self.cooling_system} active.")
#         else:
#             print("Please power on the phone first.")

#     def disable_performance_mode(self):
#         self._performance_mode = False
#         print(f"{self.brand} {self.model}: Performance mode disabled.")

#     # Override the use_camera method for a "gaming" feel (polymorphism)
#     def use_camera(self):
#         if self._is_on:
#             print(f"{self.brand} {self.model}: Capturing high-resolution gaming moments!")
#             self._check_battery()
#         else:
#             print("Please power on the phone first.")

# class FoldableSmartphone(Smartphone):
#     def __init__(self, brand, model, storage_gb, ram_gb, battery_mah, display_size_folded, display_size_unfolded):
#         super().__init__(brand, model, storage_gb, ram_gb, battery_mah)
#         self.display_size_folded = display_size_folded
#         self.display_size_unfolded = display_size_unfolded
#         self._is_folded = True # Encapsulated

#     def fold(self):
#         if not self._is_folded:
#             self._is_folded = True
#             print(f"{self.brand} {self.model}: Folding display to {self.display_size_folded}.")
#         else:
#             print(f"{self.brand} {self.model} is already folded.")

#     def unfold(self):
#         if self._is_folded:
#             self._is_folded = False
#             print(f"{self.brand} {self.model}: Unfolding display to {self.display_size_unfolded}.")
#         else:
#             print(f"{self.brand} {self.model} is already unfolded.")

# # Creating instances of the derived classes
# gaming_phone = GamingSmartphone("ROG", "Phone 7", 512, 16, 6000, "Vapor Chamber")
# foldable_phone = FoldableSmartphone("Samsung", "Galaxy Z Fold 5", 512, 12, 4400, "6.2 inches", "7.6 inches")

# print("\n--- Gaming Smartphone ---")
# print(gaming_phone)
# gaming_phone.power_on()
# gaming_phone.enable_performance_mode()
# gaming_phone.use_camera() # Polymorphic behavior
# gaming_phone.power_off()

# print("\n--- Foldable Smartphone ---")
# print(foldable_phone)
# foldable_phone.power_on()
# foldable_phone.unfold()
# foldable_phone.use_camera() # Inherited behavior
# foldable_phone.fold()
# foldable_phone.power_off()

# Activity 2
class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} is moving.")

class Car(Animal):
    def __init__(self, model):
        super().__init__("Car")
        self.model = model

    def move(self):
        print(f"{self.model} is Driving 🚗.")

class Plane(Animal):
    def __init__(self, airline):
        super().__init__("Plane")
        self.airline = airline

    def move(self):
        print(f"{self.airline} is Flying ✈️.")

class Dog(Animal):
    def __init__(self, breed, name):
        super().__init__(name)
        self.breed = breed

    def move(self):
        print(f"{self.name} the {self.breed} is Running 🐾.")

class Fish(Animal):
    def __init__(self, species, name):
        super().__init__(name)
        self.species = species

    def move(self):
        print(f"{self.name} the {self.species} is Swimming 🐠.")

# Create instances of different classes
generic_animal = Animal("Creature")
my_car = Car("Toyota Camry")
my_plane = Plane("Kenya Airways")
my_dog = Dog("Golden Retriever", "Buddy")
my_fish = Fish("Clownfish", "Nemo")

# Call the move() method on each object
generic_animal.move()
my_car.move()
my_plane.move()
my_dog.move()
my_fish.move()

# Demonstrate polymorphism by iterating through a list of objects
things_that_move = [generic_animal, my_car, my_plane, my_dog, my_fish]

print("\nDemonstrating Polymorphism:")
for thing in things_that_move:
    thing.move()