from datetime import datetime
from rentalcar import rentalcar

class Customer:
        def __init__(self, name, rental_company):
            self.name = name
            self.rental_record = []
            self.rental_company = rental_company
            self.rental_index_counter = 0

        def request_car(self, num_cars, rental_period, number_of_period):
            rental_time = self.rental_company.rent_car(num_cars, rental_period, number_of_period)
            if rental_time is not None:
                request_index = self.rental_index_counter
                self.rental_index_counter += 1
 
                self.rental_record[request_index] = {
                    'rental_time': rental_time,
                    'num_cars': num_cars,
                    'rental_period': rental_period,
                    'number_of_period':number_of_period,
                }
   
                print(f"{self.name} has successfully rented {num_cars} car(s) {rental_period}(s) with request index {request_index}.")
            else:
                print(f"Sorry, {self.name}. Not enough cars available for your request.")
   
      
    
        def return_car(self, rental_index):
            if rental_index in self.rental_record:
                rental_info = self.rental_record.pop(rental_index)
                return_time = datetime.now()
                total_cost = self.rental_company.return_car(rental_info['rental_time'])
                print(f"{self.name} has returned {rental_info['num_cars']} car(s) {rental_info['rental_period']}(s) with request index {rental_index}.")
                print(f"Total cost for the rental: ${total_cost}")
            else:
                print(f"Invalid rental index {rental_index} for {self.name}. Please provide a valid index.")