class Location(object):
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return f"Location({self.latitude}, {self.longitude})"

class DriverMetadata(object):
    def __init__(self, id, name, car_make, car_model):
        self.id = id
        self.name = name
        self.car_make = car_make
        self.car_model = car_model

    def __str__(self):
        return f"{self.name} drives a {self.car_make} {self.car_model}."
    
class DriverScheduling(object):
    def __init__(self, driver_id, time_start, time_end, min_rate, location):
        self.driver_id = driver_id
        self.time_start = time_start
        self.time_end = time_end
        self.min_rate = min_rate
        self.location = location

class RiderRequest(object):
    def __init__(self, rider_id, time_start, time_end, max_rate, location):
        self.rider_id = rider_id
        self.time_start = time_start
        self.time_end = time_end
        self.max_rate = max_rate
        self.location = location

class DriverSearchService(object):
    def __init__(self)):
        self.drivers = None

    def load_drivers(self):
        """Load the drivers preferences/location from the database."""
        self.drivers = []    

    def search(self, rider_request):
        """
        Search for drivers based on time, rate and location.
        Time and rate are hard constraints, location is a soft constraint.
        So the service returns n drivers that are available at the given time, with rate less than or equal to the rider's max rate, and are close to the rider's location.
        """
        return [driver for driver in self.drivers if driver.time_start <= time <= driver.time_end and driver.location == location]
    
    def update_driver_scheduling(self, driver_scheduling):
        """Update the driver's scheduling preferences."""
        pass
