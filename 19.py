import numpy as np
import matplotlib.pyplot as plt
import random
import math

# Define the distance function between two cities
def distance(city1, city2):
    return np.linalg.norm(city1 - city2)

# Define the total distance for a given tour
def total_distance(tour, cities):
    distance_sum = 0
    for i in range(len(tour) - 1):
        distance_sum += distance(cities[tour[i]], cities[tour[i + 1]])
    distance_sum += distance(cities[tour[-1]], cities[tour[0]])  # Return to the starting city
    return distance_sum

# Define the acceptance probability function
def acceptance_probability(old_distance, new_distance, temperature):
    if new_distance < old_distance:
        return 1.0
    return math.exp((old_distance - new_distance) / temperature)

# Simulated Annealing algorithm
def simulated_annealing(cities, initial_temperature, cooling_rate, stopping_temperature):
    num_cities = len(cities)
    current_tour = list(range(num_cities))
    random.shuffle(current_tour)
    current_distance = total_distance(current_tour, cities)

    best_tour = current_tour[:]
    best_distance = current_distance

    temperature = initial_temperature

    while temperature > stopping_temperature:
        new_tour = current_tour[:]
        # Swap two cities in the tour to generate a new neighbor
        swap_indices = sorted(random.sample(range(num_cities), 2))
        new_tour[swap_indices[0]:swap_indices[1] + 1] = reversed(new_tour[swap_indices[0]:swap_indices[1] + 1])
        new_distance = total_distance(new_tour, cities)

        if acceptance_probability(current_distance, new_distance, temperature) > random.random():
            current_tour = new_tour
            current_distance = new_distance

        if new_distance < best_distance:
            best_tour = new_tour
            best_distance = new_distance

        temperature *= cooling_rate

    return best_tour, best_distance

# Generate random cities
num_cities = 20
cities = np.random.rand(num_cities, 2)

# Parameters for Simulated Annealing
initial_temperature = 10000
cooling_rate = 0.995
stopping_temperature = 1e-5

# Run Simulated Annealing
best_tour, best_distance = simulated_annealing(cities, initial_temperature, cooling_rate, stopping_temperature)

# Plot the results
plt.figure(figsize=(10, 6))
plt.scatter(cities[:, 0], cities[:, 1], c='blue', s=100)
for i in range(num_cities):
    plt.text(cities[i, 0], cities[i, 1], str(i), fontsize=12, ha='center', va='center', color='white')
for i in range(len(best_tour) - 1):
    plt.plot([cities[best_tour[i], 0], cities[best_tour[i + 1], 0]],
             [cities[best_tour[i], 1], cities[best_tour[i + 1], 1]], c='red')
plt.plot([cities[best_tour[-1], 0], cities[best_tour[0], 0]],
         [cities[best_tour[-1], 1], cities[best_tour[0], 1]], c='red')
plt.title(f"Simulated Annealing - Total Distance: {best_distance:.2f}")
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
