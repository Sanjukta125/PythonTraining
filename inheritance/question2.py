# Base class
class Person:
    def __init__(self, name, person_id):
        self.name = name
        self.person_id = person_id

    def display_info(self):
        print("Person Information:")
        print(f"  Name: {self.name}")
        print(f"  ID: {self.person_id}")

# Derived class
class CrewMember(Person):
    def __init__(self, name, person_id, role):
        super().__init__(name, person_id)
        self.role = role

    def display_info(self):
        super().display_info()
        print(f"  Role: {self.role}")

# Further derived class
class Pilot(CrewMember):
    def __init__(self, name, person_id, role, license_number, rank):
        super().__init__(name, person_id, role)
        self.license_number = license_number
        self.rank = rank

    def display_info(self):
        super().display_info()
        print(f"  License Number: {self.license_number}")
        print(f"  Rank: {self.rank}")
pilot = Pilot("John Doe", "P001", "Pilot", "LIC123", "Captain")
pilot.display_info()