import random

def objective_function(x):
    return -x**2 + 10*x + 20 

def hill_climbing(max_iterations, step_size, min_x, max_x):
    current_x = random.uniform(min_x, max_x)  
    current_value = objective_function(current_x)
    for _ in range(max_iterations):
        next_x = current_x + random.uniform(-step_size, step_size)
        if min_x <= next_x <= max_x:
            next_value = objective_function(next_x)
            if next_value > current_value:
                current_x = next_x
                current_value = next_value
    return current_x, current_value

max_iterations = 1000
step_size = 0.1
min_x = -10
max_x = 10

best_x, best_value = hill_climbing(max_iterations, step_size, min_x, max_x)
print(f"Best solution found: x = {best_x}, f(x) = {best_value}")
