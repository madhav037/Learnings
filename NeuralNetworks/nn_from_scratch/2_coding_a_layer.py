# here a layer is coded where there are 5 input and 2 output neurons

inputs = [2.0, -4.7, 3.2, 2.2, 9.8]

weights1 = [3.1, 2.1, 8.7, 1.1, 2.0]
weights2 = [1.1, 2.1, 1.7, 1.1, 2.0]

bias1 = 3
bias2 = 2

output = [
    inputs[0]*weights1[0] + inputs[1]*weights1[1] + inputs[2]*weights1[2]+ inputs[3]*weights1[3]+ inputs[4]*weights1[4] + bias1,
    inputs[0]*weights2[0] + inputs[1]*weights2[1] + inputs[2]*weights2[2]+ inputs[3]*weights2[3]+ inputs[4]*weights2[4] + bias2    
]
print("manual output : ", output)

# the len(inputs) will be equal to the length of output
# the number of baises and weights will be equal
# because each input neuron has their own weight (so 5 neurons has 5 weights)
# and each output neuron has its own bias and weight arr

# to simplify weights are 2d lists len(weights) = len(bias)
# and len(wieghts[i]) = len(inputs)

# making above code dynamic and clean
inputs = [2.0, -4.7, 3.2, 2.2, 9.8]

weights = [
    [3.1, 2.1, 8.7, 1.1, 2.0],
    [1.1, 2.1, 1.7, 1.1, 2.0]
]

biases = [3, 2]

output_layer = []
for weight, bias in zip(weights, biases):
    neuron_output = 0
    for n_input, n_weight in zip(inputs, weight):
        neuron_output += n_input*n_weight
    neuron_output += bias
    output_layer.append(neuron_output)

print("output layer : ", output_layer)