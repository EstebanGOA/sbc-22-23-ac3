import json
from city import City
from connection import Connection


def read(filename):
    f = open(filename, encoding="utf-8")
    data = json.load(f)
    citiesFile = data['cities']
    connections = data['connections']
    cities = {}
    for cityFile in citiesFile:
        city = City(cityFile['name'],
                    cityFile['address'],
                    cityFile['country'],
                    cityFile['latitude'],
                    cityFile['longitude'])
        cities[cityFile['name']] = city

    for element in connections:
        connection = Connection(element['to'],
                                element['distance'],
                                element['duration'])
        cities[element['from']].setConnection(connection)

    return cities


