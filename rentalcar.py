from datetime import datetime, timedelta

class rentalcar:
    def __init__(self):
        self.available_cars = 100
        self.rented_cars = {}

        
    def display_available_cars(self):
        print("Available Cars: " + str(self.available_cars))   
        
    #calculate the rental time duration to be used when return the card 
    #and deduct from available cars 
    def rent_car(self, num_cars, rental_period, number_of_period):
        if num_cars > 0 and self.available_cars >= num_cars:
            current_time = datetime.now()
            rental_time = current_time  # Store the time of renting
            return_time = current_time + self.calculate_rental_duration(rental_period, number_of_period)

            self.rented_cars[rental_time] = {
                'num_cars': num_cars,
                'return_time': return_time
            }

            self.available_cars -= num_cars
            return rental_time  # Return the time of renting
        else:
            return None

    def calculate_rental_duration(self, rental_period, number_of_period):
        if rental_period == "hourly":
            return timedelta(hours= number_of_period)
        elif rental_period == "daily":
            return timedelta(days= number_of_period)
        elif rental_period == "weekly":
            return timedelta(weeks= number_of_period)
        else:
            raise ValueError("Invalid rental period. Please choose hourly, daily, or weekly.")

    def return_car(self, rental_time):
        if rental_time in self.rented_cars:
            rental_info = self.rented_cars.pop(rental_time)
            return_time = rental_info['return_time']
            rented_duration = return_time - rental_time
            total_cost = self.calculate_rental_cost(rental_info['num_cars'], rented_duration)
            self.available_cars += rental_info['num_cars']
            print(f"The total bill amount is: ${bill_amount}")
            return total_cost
        else:
            return None


    def calculate_rental_cost(self, num_cars, rented_duration):
        hourly_rate = 10
        daily_rate = 50
        weekly_rate = 200

        total_hours = rented_duration.total_seconds() / 3600

        if total_hours < 24:
            return hourly_rate * num_cars * total_hours
        elif total_hours < 168:
            return daily_rate * num_cars * (total_hours / 24)
        else:
            return weekly_rate * num_cars * (total_hours / 168)

