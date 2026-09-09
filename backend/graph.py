import heapq


# VIT Vellore - Proposed ShuttleSync Stop Graph
# Edge weights represent approximate route distance units.
# These are for the project model, not official VIT road distances.

graph = {
    "Student Entry": {
        "MGR Block": 2,
        "SJT": 3
    },

    "MGR Block": {
        "Student Entry": 2,
        "Gandhi Block": 2,
        "PRP": 3
    },

    "SJT": {
        "Student Entry": 3,
        "TT": 2,
        "PRP": 2
    },

    "TT": {
        "SJT": 2,
        "SMV": 3,
        "Central Library": 4
    },

    "Gandhi Block": {
        "MGR Block": 2,
        "PRP": 2,
        "Central Library": 3
    },

    "PRP": {
        "MGR Block": 3,
        "SJT": 2,
        "Gandhi Block": 2,
        "SMV": 2
    },

    "SMV": {
        "TT": 3,
        "PRP": 2,
        "Central Library": 2
    },

    "Central Library": {
        "TT": 4,
        "Gandhi Block": 3,
        "SMV": 2,
        "Hostel Zone": 4
    },

    "Hostel Zone": {
        "Central Library": 4,
        "SJT": 5
    }
}


def dijkstra(graph, start, destination):

    distances = {
        node: float("inf")
        for node in graph
    }

    previous = {
        node: None
        for node in graph
    }

    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:

        current_distance, current_node = heapq.heappop(
            priority_queue
        )

        if current_node == destination:
            break

        if current_distance > distances[current_node]:
            continue

        for neighbour, weight in graph[current_node].items():

            distance = current_distance + weight

            if distance < distances[neighbour]:

                distances[neighbour] = distance
                previous[neighbour] = current_node

                heapq.heappush(
                    priority_queue,
                    (distance, neighbour)
                )

    # Build shortest path
    path = []

    current = destination

    while current is not None:

        path.append(current)

        current = previous[current]

    path.reverse()

    return path, distances[destination]


# ------------------------------------------------
# TEST
# ------------------------------------------------

start = "Student Entry"
destination = "Central Library"

path, distance = dijkstra(
    graph,
    start,
    destination
)

print("=" * 50)
print("       SHUTTLESYNC - VIT VELLORE")
print("=" * 50)

print("Current Stop:", start)
print("Destination:", destination)

print(
    "Shortest Route:",
    " -> ".join(path)
)

print("Total Distance:", distance)

if len(path) > 1:
    print("Next Stop:", path[1])

print("=" * 50)