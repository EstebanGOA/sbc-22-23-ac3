import sys

class City:

    def __init__(self, name, address, country, latitude, longitude):
        # When building the path the connection
        self.directConnection = ""
        self.value = sys.maxsize
        self.approximation = sys.maxsize
        self.name = name
        self.address = address
        self.country = country
        self.latitude = latitude
        self.longitude = longitude
        self.connections = {}


    def getName(self):
        return self.name

    def getLatitude(self):
        return self.latitude

    def getLongitude(self):
        return self.longitude

    def setConnection(self, connection):
        self.connections[connection.getTo()] = connection

    def getConnections(self):
        return self.connections

    def getConnection(self, name):
        return self.connections[name]

    def setDirectConnection(self, connection):
        self.directConnection = connection

    def setValue(self, value):
        self.value = 0

    def getValue(self):
        return self.value

    def getDistanceBetween(self, city):
        return self.connections[city.getName()].getDistance()


