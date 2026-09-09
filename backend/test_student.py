from bus import Bus
from student import StudentTracker


# Create bus
bus1 = Bus("BUS001", 40, 17)

# Create student tracker
tracker = StudentTracker()


print("=" * 45)
print("       SHUTTLESYNC STUDENT SYSTEM")
print("=" * 45)

print("\nInitial Available Seats:",
      bus1.available_seats())


# Student 101 enters
print("\nStudent 101 scans QR - ENTER")

tracker.enter_bus("101", bus1)

print("Available Seats:",
      bus1.available_seats())


# Student 102 enters
print("\nStudent 102 scans QR - ENTER")

tracker.enter_bus("102", bus1)

print("Available Seats:",
      bus1.available_seats())


# Student 101 tries to enter again
print("\nStudent 101 scans QR - ENTER again")

tracker.enter_bus("101", bus1)

print("Available Seats:",
      bus1.available_seats())


# Student 101 exits
print("\nStudent 101 scans QR - EXIT")

tracker.exit_bus("101", bus1)

print("Available Seats:",
      bus1.available_seats())


# Student 101 tries to exit again
print("\nStudent 101 scans QR - EXIT again")

tracker.exit_bus("101", bus1)

print("Available Seats:",
      bus1.available_seats())


print("\n" + "=" * 45)