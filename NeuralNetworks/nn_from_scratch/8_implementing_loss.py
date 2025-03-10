# import numpy as np
# softmax_outputs = np.array([[0.7, 0.1, 0.2],
#                             [0.1, 0.5, 0.4],
#                             [0.02, 0.9, 0.08]])

# class_target = [0, 1, 1]

# neg_loss = -np.log(softmax_outputs[range(len(softmax_outputs)), class_target])

# average_loss = np.mean(neg_loss)

# print(average_loss)


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

class Loss:
    def calculate(self, output, y):
        sample_losses = self.forward(output, y)
        data_loss = np.mean(sample_losses)
        return data_loss

class Loss_CategoricalCrossentropy(Loss):
    def forward(self, y_pred, y_true):
        samples = len(y_pred)
        y_pred_clipped = np.clip(y_pred, 1e-7, 1-1e-7)

        if len(y_true.shape) == 1: # scalar values
            correct_confidences = y_pred_clipped[range(samples), y_true]
        elif len(y_true.shape) == 2: # one-hot encoded values
            correct_confidences = np.sum(y_pred_clipped*y_true, axis=1)

        negative_log_likelihoods = -np.log(correct_confidences)
        return negative_log_likelihoods

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

loss_function = Loss_CategoricalCrossentropy()
loss = loss_function.calculate(activation2.output, y)

print("loss : ", loss)