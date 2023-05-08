from math import radians, sin, cos, sqrt, asin


# Credits: https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points
def haversine(city1, city2):
    aux1 = city1.getLongitude()
    aux2 = city1.getLatitude()
    aux3 = city2.getLongitude()
    aux4 = city2.getLatitude()
    lon1, lat1, lon2, lat2 = map(radians, [aux1, aux2, aux3, aux4])

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of earth in kilometers.
    return c * r * 1000


def in_list(nodes, name):
    for node in nodes:
        if node.getName == name:
            return True
    return False


def astar(cities, start, end):
    cities[start].setValue(0)
    nodes = [cities[start]]
    visited = {}

    while len(nodes) > 0:
        current = nodes.pop()
        # Mark as visited
        visited[current.getName()] = True
        if current.getName() == end:
            print("acabado")
            return

        for conName in current.getConnections():
            connection = current.getConnection(conName)
            to = connection.getTo()
            if to in visited:
                continue

            dist_child_end = haversine(cities[to], cities[end])
            dist_curr_child = current.getValue() + connection.getDistance()
            dist = dist_curr_child + dist_child_end
            actual_dist = cities[to].getValue()

            if dist < actual_dist and in_list(nodes, to):
                cities[to].setValue(dist)
                continue

            cities[to].setValue(int(dist))
            nodes.append(cities[to])




