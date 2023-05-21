import reader
import astar
from backtracking import DFS

start = "Barcelona"
end = "Reus"


def main():
    cities = reader.read('../data/data.json')
    astar.astar(cities, start, end)
    dfs = DFS(cities[start], cities[end], cities)
    path = dfs.solve()
    print(path)


if __name__ == '__main__':
    main()
