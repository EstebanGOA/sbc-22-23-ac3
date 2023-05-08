import reader
import astar

start = "Barcelona"
end = "Vic"


def main():
    cities = reader.read('../data/data.json')
    astar.astar(cities, start, end)


if __name__ == '__main__':
    main()
