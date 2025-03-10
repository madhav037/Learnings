import math

softmax_outputs = [0.7, 0.1, 0.2]
target_outputs = [1, 0, 0]

loss = - (math.log(softmax_outputs[0])*target_outputs[0] +
            math.log(softmax_outputs[1])*target_outputs[1] +
            math.log(softmax_outputs[2])*target_outputs[2])

print(loss) 