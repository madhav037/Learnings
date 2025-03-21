import numpy as np
from create_data import create_data
np.random.seed(0)


class Layer_object:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
    
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases
        

class Activation_ReLU:
    def forward(self, inputs):
        self.output = np.maximum(inputs, 0)        

class Activation_softmax:
    def forward(self, inputs):
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        self.output = probabilities

X, y = create_data(100, 3)

dense1 = Layer_object(2,3)
activation1 = Activation_ReLU()

dense2 = Layer_object(3,3)
activation2 = Activation_softmax()

dense1.forward(X)
activation1.forward(dense1.output)

dense2.forward(activation1.output)
activation2.forward(dense2.output)

# print("layer 1 : ", dense1.output)
# print("activation 1 : ", activation1.output)
# print("layer 2 : ", dense2.output)
print("activation 2 : ", activation2.output[:5])