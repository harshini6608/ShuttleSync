from bus import Bus
from graph import graph, dijkstra


# ---------------------------------------
# CREATE BUSES
# ---------------------------------------

bus1 = Bus("BUS001", 40, 17)
bus2 = Bus("BUS002", 40, 25)


# ---------------------------------------
# BUS CURRENT LOCATIONS
# ---------------------------------------

bus_locations = {
    "BUS001": "Student Entry",
    "BUS002": "SJT"
}


# ---------------------------------------
# DESTINATION
# ---------------------------------------

destination = "Central Library"


# ---------------------------------------
# FUNCTION TO DISPLAY BUS INFORMATION
# ---------------------------------------

def display_bus(bus, current_stop):

    path, distance = dijkstra(
        graph,
        current_stop,
        destination
    )

    print("\n" + "-" * 50)

    print("BUS ID:", bus.bus_id)
    print("Current Stop:", current_stop)

    if len(path) > 1:
        print("Next Stop:", path[1])
    else:
        print("Next Stop: Destination Reached")

    print("Destination:", destination)

    print("Route:", " -> ".join(path))

    print("Distance:", distance)

    print("Passengers:", bus.passengers)

    print("Available Seats:", bus.available_seats())

    print("-" * 50)


# ---------------------------------------
# DISPLAY ALL BUSES
# ---------------------------------------

print("\n" + "=" * 50)
print("          SHUTTLESYNC")
print("       VIT SMART SHUTTLE SYSTEM")
print("=" * 50)

display_bus(
    bus1,
    bus_locations["BUS001"]
)

display_bus(
    bus2,
    bus_locations["BUS002"]
)

print("\nSystem Status: RUNNING")