import reader
import astar

start = "Barcelona"
end = "Tremp"


def main():
    cities = reader.read('../data/data.json')
    astar.astar(cities, start, end)


if __name__ == '__main__':
    main()
