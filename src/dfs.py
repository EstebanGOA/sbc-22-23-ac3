import sys


class DFS:

    def __init__(self, start_city, end_city, cities):
        self.cities = cities
        self.start_city = start_city
        self.end_city = end_city
        self.visited_cities = set()

        # Set the shortest distance to the maximum value of an integer.
        # ref: https://stackoverflow.com/questions/7604966/maximum-and-minimum-values-for-ints
        self.shortest_distance = sys.maxsize
        self.shortest_path = []

    def solve(self):
        self.dfs(self.start_city, 0, [])
        return self.shortest_path

    def dfs(self, current_city, distance, path):

        if current_city == self.end_city:
            if distance < self.shortest_distance:
                self.shortest_distance = distance
                self.shortest_path = path + [current_city.getName()]
            return

        # We are looking for the solution with the shortest distance, so we can stop searching if the current distance
        # is greater than the shortest distance found so far.
        if distance > self.shortest_distance:
            return

        self.visited_cities.add(current_city)

        for next_city in current_city.getConnections():
            # Connections store the city name as a string, so we need to get the object instead.
            next_city = self.cities[next_city]

            if next_city not in self.visited_cities:
                self.dfs(
                    next_city,
                    distance + current_city.getDistanceBetween(next_city),
                    path + [current_city.getName()]
                )

        self.visited_cities.remove(current_city)
