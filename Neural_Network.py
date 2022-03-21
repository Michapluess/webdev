class Neural_Network:
    def __init__(self, inputsize):
        print("createNeuralNetwork")
        self.inputsize = inputsize
        self.weights = []
        self.activations = []           #biases sind noch nicht gemacht
        self.lastlayer = inputsize
        self.countlayers = 0

    def feedForward(self, inputs):
        for layer in range(self.countlayers):
            previousactivations = inputs if layer == 0 else self.activations[layer-1]
            neurons = self.weights[layer]
            for neuron in range(len(neurons)):
                arrows = neurons[neuron]
                activation = 0
                for arrow in range(len(arrows)):
                    weight = arrows[arrow]
                    activation += weight*previousactivations[arrow]
                self.activations[layer][neuron] = activation

        print("feedForward")
        return self.activations[self.countlayers-1]



    def addLayer(self, size):
        newweights = []
        newactivations = []
        for i in range(size):
            newarrows = []
            for j in range(self.lastlayer):
                newarrows.append(0.5)
            newweights.append(newarrows)
            newactivations.append(0)
        self.weights.append(newweights)
        self.activations.append(newactivations)
        self.lastlayer = size  
        self.countlayers += 1 
        print("addLayer")

nn = Neural_Network(6)
nn.addLayer(4)
nn.addLayer(2)
nn.addLayer(3)
output = nn.feedForward([0.5, 0.5, 0.5,  0.5, 0.5, 0.5])
print(nn.weights)
print(output)