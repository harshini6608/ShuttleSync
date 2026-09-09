class Bus:
    def __init__(self, bus_id, capacity, passengers=0):
        self.bus_id = bus_id
        self.capacity = capacity
        self.passengers = passengers

    def available_seats(self):
        return self.capacity - self.passengers

    def add_passenger(self):
        if self.passengers < self.capacity:
            self.passengers += 1
            return True
        return False

    def remove_passenger(self):
        if self.passengers > 0:
            self.passengers -= 1
            return True
        return False

    def display(self):
        print(f"Bus ID: {self.bus_id}")
        print(f"Capacity: {self.capacity}")
        print(f"Passengers: {self.passengers}")
        print(f"Available Seats: {self.available_seats()}")
        print("-" * 30)


# Test buses
bus1 = Bus("BUS001", 40, 17)
bus2 = Bus("BUS002", 40, 25)

bus1.display()
bus2.display()

# Simulate one student entering BUS001
print("One passenger enters BUS001...")
bus1.add_passenger()
bus1.display()

# Simulate one passenger exiting BUS001
print("One passenger exits BUS001...")
bus1.remove_passenger()
bus1.display()