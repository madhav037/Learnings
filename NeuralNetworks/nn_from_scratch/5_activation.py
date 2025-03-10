import numpy as np
from create_data import create_data
np.random.seed(0)

X, y = create_data(100, 3)

class Layer_object:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
    
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases
        

class Activation_ReLU:
    def forward(self, inputs):
        self.output = np.maximum(inputs, 0)        


layer1 = Layer_object(2,5)
activation1 = Activation_ReLU()
layer1.forward(X)        
activation1.forward(layer1.output)

print("layer 1 : ", layer1.output)
print("activation 1 : ", activation1.output)