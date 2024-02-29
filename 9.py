import itertools

def distance(city1, city2):
    return ((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2) ** 0.5

def total_distance(path, cities):
    total = 0
    for i in range(len(path)):
        total += distance(cities[path[i]], cities[path[(i + 1) % len(path)]])
    return total

def traveling_salesman(cities):
    shortest_path = None
    shortest_distance = float('inf')
    for path in itertools.permutations(range(len(cities))):
        dist = total_distance(path, cities)
        if dist < shortest_distance:
            shortest_distance = dist
            shortest_path = path
    return shortest_path, shortest_distance

if __name__ == "__main__":
    cities = [(0, 0), (1, 2), (3, 1), (5, 3)]
    shortest_path, shortest_distance = traveling_salesman(cities)
    print("Shortest Path:", shortest_path)
    print("Shortest Distance:", shortest_distance)
