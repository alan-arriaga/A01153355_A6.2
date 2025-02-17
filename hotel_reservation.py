import json
import os
import unittest

class Hotel:
    FILE = "hotels.json"
    
    def __init__(self, hotel_id, name, location, rooms_available):
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.rooms_available = rooms_available
    
    def to_dict(self):
        return {
            "hotel_id": self.hotel_id,
            "name": self.name,
            "location": self.location,
            "rooms_available": self.rooms_available,
        }
    
    @classmethod
    def load_hotels(cls):
        if os.path.exists(cls.FILE):
            try:
                with open(cls.FILE, "r") as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError):
                print("Error reading hotel data. Initializing empty data.")
                return []
        return []
    
    @classmethod
    def save_hotels(cls, hotels):
        with open(cls.FILE, "w") as file:
            json.dump(hotels, file, indent=4)
    
    @classmethod
    def create_hotel(cls, hotel):
        hotels = cls.load_hotels()
        hotels.append(hotel.to_dict())
        cls.save_hotels(hotels)
    
    @classmethod
    def delete_hotel(cls, hotel_id):
        hotels = cls.load_hotels()
        hotels = [h for h in hotels if h["hotel_id"] != hotel_id]
        cls.save_hotels(hotels)
    
    @classmethod
    def display_hotels(cls):
        return cls.load_hotels()


class Customer:
    FILE = "customers.json"
    
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email
    
    def to_dict(self):
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email,
        }
    
    @classmethod
    def load_customers(cls):
        if os.path.exists(cls.FILE):
            try:
                with open(cls.FILE, "r") as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError):
                print("Error reading customer data. Initializing empty data.")
                return []
        return []
    
    @classmethod
    def save_customers(cls, customers):
        with open(cls.FILE, "w") as file:
            json.dump(customers, file, indent=4)
    
    @classmethod
    def create_customer(cls, customer):
        customers = cls.load_customers()
        customers.append(customer.to_dict())
        cls.save_customers(customers)
    
    @classmethod
    def delete_customer(cls, customer_id):
        customers = cls.load_customers()
        customers = [c for c in customers if c["customer_id"] != customer_id]
        cls.save_customers(customers)
    
    @classmethod
    def display_customers(cls):
        return cls.load_customers()


class Reservation:
    FILE = "reservations.json"
    
    def __init__(self, reservation_id, customer_id, hotel_id):
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.hotel_id = hotel_id
    
    def to_dict(self):
        return {
            "reservation_id": self.reservation_id,
            "customer_id": self.customer_id,
            "hotel_id": self.hotel_id,
        }
    
    @classmethod
    def load_reservations(cls):
        if os.path.exists(cls.FILE):
            try:
                with open(cls.FILE, "r") as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError):
                print("Error reading reservation data. Initializing empty data.")
                return []
        return []
    
    @classmethod
    def save_reservations(cls, reservations):
        with open(cls.FILE, "w") as file:
            json.dump(reservations, file, indent=4)
    
    @classmethod
    def create_reservation(cls, reservation):
        reservations = cls.load_reservations()
        reservations.append(reservation.to_dict())
        cls.save_reservations(reservations)
    
    @classmethod
    def cancel_reservation(cls, reservation_id):
        reservations = cls.load_reservations()
        reservations = [r for r in reservations if r["reservation_id"] != reservation_id]
        cls.save_reservations(reservations)


class TestHotelReservationSystem(unittest.TestCase):
    def setUp(self):
        self.hotel = Hotel("H1", "Grand Hotel", "NYC", 10)
        self.customer = Customer("C1", "John Doe", "johndoe@example.com")
        self.reservation = Reservation("R1", "C1", "H1")
    
    def test_create_hotel(self):
        Hotel.create_hotel(self.hotel)
        hotels = Hotel.display_hotels()
        self.assertIn(self.hotel.to_dict(), hotels)
    
    def test_create_customer(self):
        Customer.create_customer(self.customer)
        customers = Customer.display_customers()
        self.assertIn(self.customer.to_dict(), customers)
    
    def test_create_reservation(self):
        Reservation.create_reservation(self.reservation)
        reservations = Reservation.load_reservations()
        self.assertIn(self.reservation.to_dict(), reservations)
    
  #  def test_delete_hotel(self):
   #     Hotel.create_hotel(self.hotel)
    #    Hotel.delete_hotel("H1")
    #    hotels = Hotel.display_hotels()
     #   self.assertNotIn(self.hotel.to_dict(), hotels)
    
   # def test_delete_customer(self):
    #    Customer.create_customer(self.customer)
     #   Customer.delete_customer("C1")
      #  customers = Customer.display_customers()
       # self.assertNotIn(self.customer.to_dict(), customers)
    
    def test_cancel_reservation(self):
        Reservation.create_reservation(self.reservation)
        Reservation.cancel_reservation("R1")
        reservations = Reservation.load_reservations()
        self.assertNotIn(self.reservation.to_dict(), reservations)

if __name__ == "__main__":
    # Run tests
    unittest.main()


