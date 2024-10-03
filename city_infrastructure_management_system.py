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

# Task 2: Event Management System Enhancement

class Event:
    def __init__(self, name, date, participants):
        self.name = name
        self.date = date
        self.participants = participants
    
    def add_participant(self):
        participant = input("Enter the name of the participant: ")
        self.participants += 1
        print(f"{participant} has been added. ")
        return self.participants

    def get_participant_count(self):
        print(f"There are now {self.participants} participants.")

event = Event("Baking Class", "10/02/2024", 20)

while True:
    action = input("Would you like to [add] a participant or get the current [count]? Type [exit] to exit progrom. ")

    if action == 'exit':
        break
    try:
        if action == 'add':
            event.add_participant()
        elif action == 'count':
            event.get_participant_count()
    except Exception as e:
        print(f"An error occurred: {e}")