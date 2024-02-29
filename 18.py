import numpy as np

class NeuralNetwork:
    def __init__(self, layers, learning_rate=0.01):
        self.layers = layers
        self.learning_rate = learning_rate
        self.weights = [np.random.randn(layers[i], layers[i+1]) for i in range(len(layers)-1)]
        self.biases = [np.zeros((1, layers[i+1])) for i in range(len(layers)-1)]

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def feedforward(self, x):
        activations = [x]
        weighted_sum = None
        for w, b in zip(self.weights, self.biases):
            if weighted_sum is not None:
                x = weighted_sum
            weighted_sum = np.dot(x, w) + b
            x = self.sigmoid(weighted_sum)
            activations.append(x)
        return activations

    def backward(self, x, y, activations):
        delta = (activations[-1] - y) * self.sigmoid_derivative(activations[-1])
        d_weights = []
        d_biases = []
        for i in range(len(self.weights)-1, -1, -1):
            d_weights.insert(0, np.dot(activations[i].T, delta))
            d_biases.insert(0, np.sum(delta, axis=0))
            if i > 0:
                delta = np.dot(delta, self.weights[i].T) * self.sigmoid_derivative(activations[i])
        return d_weights, d_biases

    def train(self, X, y, epochs):
        for epoch in range(epochs):
            total_loss = 0
            for input_data, label in zip(X, y):
                input_data = np.array(input_data, ndmin=2)
                label = np.array(label, ndmin=2)
                activations = self.feedforward(input_data)
                d_weights, d_biases = self.backward(input_data, label, activations)
                for i in range(len(self.weights)):
                    self.weights[i] -= self.learning_rate * d_weights[i]
                    self.biases[i] -= self.learning_rate * d_biases[i]
                total_loss += np.mean(np.square(activations[-1] - label))
            if epoch % 100 == 0:
                print(f"Epoch {epoch}, Loss: {total_loss}")


# Example usage
if __name__ == "__main__":
    # Define the dataset (XOR problem)
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])

    # Define the neural network architecture
    neural_net = NeuralNetwork(layers=[2, 4, 1], learning_rate=0.1)

    # Train the neural network
    neural_net.train(X, y, epochs=1000)

    # Test the neural network
    for i in range(len(X)):
        input_data = X[i]
        label = y[i]
        prediction = neural_net.feedforward(input_data)[-1]
        print(f"Input: {input_data}, Target: {label}, Prediction: {prediction}")
