import numpy as np

inputs = [2.0, -4.7, 3.2, 2.2, 9.8]

weights = [
    [3.1, 2.1, 8.7, 1.1, 2.0],
    [1.1, 2.1, 1.7, 1.1, 2.0]
]

biases = [3, 2]

output = np.dot(weights, inputs) + biases
print(output)

# np.dot(weights, inputs) = [
    # np.dot(weights[0] + inputs) + bias[0]
    # np.dot(weights[1] + inputs) + bias[1]
    # ]