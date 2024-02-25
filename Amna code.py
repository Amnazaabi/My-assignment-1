#!/usr/bin/env python
# coding: utf-8

# In[8]:


from datetime import datetime

class Passenger:  # Create the Passenger class
    def __init__(self, name, ticket_number, seat_number):  # Initialize Passenger object with name, ticket number, and seat number
        self.name = name  # Set passenger name
        self.ticket_number = ticket_number  # Set ticket number
        self.seat_number = seat_number  # Set seat number

    def get_name(self):  # Get passenger name
        return self.name

    def get_ticket_number(self):  # Get ticket number
        return self.ticket_number

    def get_seat_number(self):  # Get seat number
        return self.seat_number

    def set_name(self, name):  # Set passenger name
        self.name = name

    def set_ticket_number(self, ticket_number):  # Set ticket number
        self.ticket_number = ticket_number

    def set_seat_number(self, seat_number):  # Set seat number
        self.seat_number = seat_number


class Flight:  # Create the Flight class
    def __init__(self, flight_number, departure_airport, destination_airport, departure_datetime, arrival_datetime, gate):
        # Initialize Flight object with flight number, departure airport, destination airport, departure datetime, arrival datetime, and gate
        self.flight_number = flight_number
        self.departure_airport = departure_airport
        self.destination_airport = destination_airport
        self.departure_datetime = departure_datetime
        self.arrival_datetime = arrival_datetime
        self.gate = gate

    def get_flight_number(self):  # Get flight number
        return self.flight_number

    def get_departure_airport(self):  # Get departure airport
        return self.departure_airport

    def get_destination_airport(self):  # Get destination airport
        return self.destination_airport

    def get_departure_datetime(self):  # Get departure datetime
        return self.departure_datetime

    def get_arrival_datetime(self):  # Get arrival datetime
        return self.arrival_datetime

    def get_gate(self):  # Get gate
        return self.gate

    def set_flight_number(self, flight_number):  # Set flight number
        self.flight_number = flight_number

    def set_departure_airport(self, departure_airport):  # Set departure airport
        self.departure_airport = departure_airport

    def set_destination_airport(self, destination_airport):  # Set destination airport
        self.destination_airport = destination_airport

    def set_departure_datetime(self, departure_datetime):  # Set departure datetime
        self.departure_datetime = departure_datetime

    def set_arrival_datetime(self, arrival_datetime):  # Set arrival datetime
        self.arrival_datetime = arrival_datetime

    def set_gate(self, gate):  # Set gate
        self.gate = gate


class BoardingPass:  # Create the Boarding Pass class
    def __init__(self, passenger_name, flight_number, departure_airport, destination_airport, arrival_datetime, gate, seat_number, electronic_ticket):
        # Initialize Boarding Pass object with passenger name, flight number, departure airport, destination airport, arrival datetime, gate, seat number, and electronic ticket
        self.passenger_name = passenger_name
        self.flight_number = flight_number
        self.departure_airport = departure_airport
        self.destination_airport = destination_airport
        self.arrival_datetime = arrival_datetime
        self.gate = gate
        self.seat_number = seat_number
        self.electronic_ticket = electronic_ticket

    def get_passenger_name(self):  # Get passenger name
        return self.passenger_name

    def get_flight_number(self):  # Get flight number
        return self.flight_number

    def get_departure_airport(self):  # Get departure airport
        return self.departure_airport

    def get_destination_airport(self):  # Get destination airport
        return self.destination_airport

    def get_arrival_datetime(self):  # Get arrival datetime
        return self.arrival_datetime

    def get_gate(self):  # Get gate
        return self.gate

    def get_seat_number(self):  # Get seat number
        return self.seat_number

    def get_electronic_ticket(self):  # Get electronic ticket
        return self.electronic_ticket

    def set_passenger_name(self, passenger_name):  # Set passenger name
        self.passenger_name = passenger_name

    def set_flight_number(self, flight_number):  # Set flight number
        self.flight_number = flight_number

    def set_departure_airport(self, departure_airport):  # Set departure airport
        self.departure_airport = departure_airport

    def set_destination_airport(self, destination_airport):  # Set destination airport
        self.destination_airport = destination_airport

    def set_arrival_datetime(self, arrival_datetime):  # Set arrival datetime
        self.arrival_datetime = arrival_datetime

    def set_gate(self, gate):  # Set gate
        self.gate = gate

    def set_seat_number(self, seat_number):  # Set seat number
        self.seat_number = seat_number

    def set_electronic_ticket(self, electronic_ticket):  # Set electronic ticket
        self.electronic_ticket = electronic_ticket


class BoardingPassSystem:  # Create the Boarding Pass System class
    def __init__(self):  # Initialize Boarding Pass System object
        self.boarding_pass = None

    def generate_boarding_pass_info(self, passenger, flight):
        # This method should generate boarding pass information
        self.boarding_pass = BoardingPass(passenger.get_name(), flight.get_flight_number(), 
                                          flight.get_departure_airport(), flight.get_destination_airport(), 
                                          flight.get_arrival_datetime(), flight.get_gate(), 
                                          passenger.get_seat_number(), passenger.get_ticket_number())

    def update_boarding_pass_info(self, boarding_pass):
        # This method should update boarding pass information
        self.boarding_pass = boarding_pass

    def view_boarding_pass_info(self):
        # This method should view boarding pass information
        if self.boarding_pass:
            print("Passenger Name:", self.boarding_pass.get_passenger_name())
            print("Flight Number:", self.boarding_pass.get_flight_number())
            print("Departure Airport:", self.boarding_pass.get_departure_airport())
            print("Destination Airport:", self.boarding_pass.get_destination_airport())
            print("Arrival Date Time:", self.boarding_pass.get_arrival_datetime())
            print("Gate:", self.boarding_pass.get_gate())
            print("Seat Number:", self.boarding_pass.get_seat_number())
            print("Electronic Ticket:", self.boarding_pass.get_electronic_ticket())
        else:
            print("No boarding pass information available.")


# In[9]:


# Test cases
passenger2 = Passenger("Ayesha", "987654321", "B24")  # Create passenger object
flight2 = Flight("XYZ789", "LAX", "JFK", datetime(2024, 3, 2, 10, 0), datetime(2024, 3, 2, 14, 0), "GATE2")  # Create flight object

boarding_pass_system = BoardingPassSystem()  # Create boarding pass system object

#Generate boarding pass information
print("\n\n\tGenerate Boarding pass information\n\n")
boarding_pass_system.generate_boarding_pass_info(passenger2, flight2)  # Generate boarding pass
boarding_pass_system.view_boarding_pass_info()  # View boarding pass information

# Update boarding pass information
print("\n\n\tUpdate  Boarding pass information\n")
passenger3 = Passenger("Mohammad", "555666777", "C15")  # Create passenger object
flight3 = Flight("DEF456", "SFO", "ORD", datetime(2024, 3, 3, 12, 0), datetime(2024, 3, 3, 16, 0), "GATE3")  # Create flight object
boarding_pass_system.generate_boarding_pass_info(passenger3, flight3)  # Generate boarding pass
boarding_pass_system.view_boarding_pass_info()  # View boarding pass information

# View updated boarding pass information
print("\n\n\tView  Boarding pass information\n")
boarding_pass_system.update_boarding_pass_info(BoardingPass("Ayesha", "GHI789", "ORD", "SEA", datetime(2024, 3, 4, 14, 0), "GATE4", "D28", "999888777"))
boarding_pass_system.view_boarding_pass_info()  # View boarding pass information


# In[ ]:




