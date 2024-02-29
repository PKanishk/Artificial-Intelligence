import math
import random

def objective_function(x):
    return x**2

def simulated_annealing(objective_function, initial_solution, initial_temperature, cooling_rate, num_iterations):
    current_solution = initial_solution
    current_cost = objective_function(current_solution)
    best_solution = current_solution
    best_cost = current_cost
    temperature = initial_temperature
    for i in range(num_iterations):
        neighbor_solution = current_solution + random.uniform(-0.1, 0.1) 
        neighbor_cost = objective_function(neighbor_solution)
        if neighbor_cost < current_cost:
            current_solution = neighbor_solution
            current_cost = neighbor_cost
            if neighbor_cost < best_cost:
                best_solution = neighbor_solution
                best_cost = neighbor_cost
        else:
            delta = neighbor_cost - current_cost
            probability = math.exp(-delta / temperature)
            if random.random() < probability:
                current_solution = neighbor_solution
                current_cost = neighbor_cost
        temperature *= cooling_rate
    return best_solution, best_cost

initial_solution = 10 
initial_temperature = 1000 
cooling_rate = 0.99  
num_iterations = 1000 
best_solution, best_cost = simulated_annealing(objective_function, initial_solution, initial_temperature, cooling_rate, num_iterations)
print("Best solution:", best_solution)
print("Best cost:", best_cost)
