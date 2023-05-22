from math import radians, sin, cos, sqrt, asin


# Credits: https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points
def haversine(city1, city2):
    aux1 = city1.longitude
    aux2 = city1.latitude
    aux3 = city2.longitude
    aux4 = city2.latitude
    lon1, lat1, lon2, lat2 = map(radians, [aux1, aux2, aux3, aux4])

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of earth in kilometers.
    return c * r * 1000


def in_list(nodes, name):
    for node in nodes:
        if node.name == name:
            return True
    return False


def astar(cities, start, end):
    cities[start].value = 0
    nodes = [cities[start]]
    visited = {}

    while len(nodes) > 0:
        current = nodes.pop()
        # Mark as visited
        visited[current.name] = True
        if current.name == end:
            printPath(cities, end)
            print()
            return

        for conName in current.connections:
            connection = current.getConnection(conName)
            to = connection.getTo()
            if to in visited:
                continue

            dist_child_end = haversine(cities[to], cities[end])
            dist_curr_child = current.getValue() + connection.getDistance()
            dist = dist_curr_child + dist_child_end
            actual_dist = cities[to].approximation

            # Case we don't want to update the node
            if dist >= actual_dist and in_list(nodes, to):
                continue

            cities[to].value = dist_curr_child
            cities[to].approximation = dist
            cities[to].directConnection = current.getName()

            # Case we want to update the node
            if dist < actual_dist and in_list(nodes, to):
                continue
            # Case we want to add the node
            nodes.append(cities[to])

        nodes = sorted(nodes, key=lambda c: c.approximation, reverse=True)


def printPath(nodes, name):
    if nodes[name].directConnection == "":
        print("Sortim de " + name, end="")
        return
    printPath(nodes, nodes[name].directConnection)
    print(" -> " + name, end="")
