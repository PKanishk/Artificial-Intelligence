import random

# Define the objective function that we want to optimize
def objective_function(x):
    return -(x ** 2)  # Example objective function, we want to maximize -x^2

# Define the hill climbing algorithm
def hill_climbing(max_iterations, step_size, initial_solution):
    current_solution = initial_solution

    for _ in range(max_iterations):
        # Generate a new solution by adding random noise to the current solution
        new_solution = current_solution + random.uniform(-step_size, step_size)

        # Evaluate the objective function for the current and new solutions
        current_value = objective_function(current_solution)
        new_value = objective_function(new_solution)

        # Check if the new solution is better than the current one
        if new_value > current_value:
            current_solution = new_solution

    return current_solution, objective_function(current_solution)

if __name__ == "__main__":
    # Parameters
    max_iterations = 1000
    step_size = 0.1
    initial_solution = 10

    # Run hill climbing algorithm
    final_solution, optimal_value = hill_climbing(max_iterations, step_size, initial_solution)

    print("Optimal Solution:", final_solution)
    print("Optimal Value:", optimal_value)
