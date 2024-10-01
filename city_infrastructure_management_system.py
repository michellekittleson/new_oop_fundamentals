# Task 1: Vehice Registration System

class Vehicle:
    def __init__(self, registration_number, type, owner):
        self.registration_number = registration_number
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner

their_car = Vehicle("ABC123", "Sedan", "Them")
my_car = their_car.update_owner("Michelle")