"""
Complete this implementation of backpropagation learning for
feedforward networks.
"""

# ------------------------------------------------------------------------------

import random, string, math


def pretty(values):
    return "".join(['%.3f' % v for v in values])


# ------------------------------------------------------------------------------

class Unit:
    """
    A Unit object represents a node in a network.  It keeps track of
    the node's current activation value (between 0.0 and 1.0), as well
    as all of the connections from other units into this unit, and all
    of the connections from this unit to other units in the network.
    """

    def __init__(self, activation=0.0):
        assert 0.0 <= activation <= 1.0, 'activation out of range'
        self.activation = activation
        self.incomingConnections = []
        self.outgoingConnections = []
        self.delta = 0

    def sigmoidFunction(self, x):
        return 1 / (1 + math.exp(-x))


# ------------------------------------------------------------------------------

class Connection:
    """
    A Connection object represents a connection between two units of a
    network.  The connection strength is initialized to a small random
    value.
    """

    def __init__(self, fromUnit, toUnit):
        self.fromUnit = fromUnit
        self.toUnit = toUnit
        self.randomize()
        self.increment = 0

    def randomize(self):
        self.weight = random.uniform(-0.1, +0.1)


# ------------------------------------------------------------------------------

class Network:
    """
    A Network object represents a three-layer feedforward network with
    a given number of input, hidden, and output units.
    """

    def __init__(self, numInputs, numHiddens, numOutputs):
        # creating the units
        self.outputLayer = [Unit() for i in range(numOutputs)]
        self.hiddenLayer = [Unit() for j in range(numHiddens)]
        self.inputLayer = [Unit() for k in range(numInputs)]
        # wiring up the network
        self.allConnections = []
        self.connectLayers(self.inputLayer, self.hiddenLayer)
        self.connectLayers(self.hiddenLayer, self.outputLayer)
        # connecting the bias units
        outputBias = Unit(1.0)
        self.connectToLayer(outputBias, self.outputLayer)
        hiddenBias = Unit(1.0)
        self.connectToLayer(hiddenBias, self.hiddenLayer)
        # set the learning parameters
        self.learningRate = 0.3
        self.tolerance = 0.1

    def connect(self, fromUnit, toUnit):
        """
        This method creates a connection with a random weight from the source unit
        to the target unit and updates the respective incoming and outgoing
        connections lists of both units. The connection is also added to the list
        of all connections in the network.
        """
        c = Connection(fromUnit, toUnit)
        fromUnit.outgoingConnections.append(c)
        toUnit.incomingConnections.append(c)
        self.allConnections.append(c)

    def connectToLayer(self, unit, layer):
        """
        Create connections from a unit to all units in a layer.

        Args:
            unit (Unit): The source unit.
            layer (list[Unit]): The target layer.

        This method creates connections from the source unit to all units in the
        target layer. It calls the 'connect' method to establish connections with
        all units in the specified layer.
        """
        for otherUnit in layer:
            self.connect(unit, otherUnit)

    def connectLayers(self, fromLayer, toLayer):
        """
        This method creates connections from all units in the source layer to all
        units in the target layer. It calls the 'connectToLayer' method to establish
        connections with all units in the target layer.
        """
        for unit in fromLayer:
            self.connectToLayer(unit, toLayer)

    def initialize(self):
        """
        This method initializes the weights of all connections in the network by
        calling the 'randomize' method on each connection. It is typically used
        during the network setup to randomize initial weights.
        """
        for c in self.allConnections:
            c.randomize()
        print('weights randomized')

    def test(self):
        """
        This method prints information about the network, including the connection
        weights and the results obtained by propagating input patterns through the
        network. It is useful for debugging and monitoring the network's behavior.
        """
        print('weights =', pretty([c.weight for c in self.allConnections]))
        for pattern in self.inputs:
            output = pretty(self.propagate(pattern))
            hiddenRep = pretty([h.activation for h in self.hiddenLayer])
            print('%s -> [%s] -> output %s' % (pattern, hiddenRep, output))
        print()

    def propagate(self, pattern):
        """
        This method takes an input pattern, represented as a list of
        floating-point values, propagates the pattern through the
        network, and returns the resulting output pattern as a list of
        floating-point values.  This method should update the
        activation values of all input, hidden, and output units in
        the network as a side effect.

        It ensures that given pattern is the appropriate length and
        that the values are in the range 0-1.
        """
        if len(pattern) != len(self.inputLayer):
            raise ValueError("Pattern length doesn't match the number of input units")

            # Set input unit activations directly
        for i, value in enumerate(pattern):
            self.inputLayer[i].activation = value

            # Forward propagation
        for unit in self.hiddenLayer:
            net_input = sum(
                connection.fromUnit.activation * connection.weight for connection in unit.incomingConnections)
            unit.activation = self.sigmoidFunction(net_input)

        for unit in self.outputLayer:
            net_input = sum(
                connection.fromUnit.activation * connection.weight for connection in unit.incomingConnections)
            unit.activation = self.sigmoidFunction(net_input)

        return [unit.activation for unit in self.outputLayer]

    def sigmoidFunction(self, x):
        """
        It transforms the input value 'x' into a
        value between 0 and 1. The sigmoid function is defined as:

        f(x) = 1 / (1 + e^(-x))

        where 'e' is the base of the natural logarithm (approximately 2.71828).
        This function is used to calculate the activation of units in the network.
        """
        return 1 / (1 + math.exp(-x))

    def computeError(self, inputs, targets):
        """
        This method evaluates the network's performance on the
        patterns stored in self.inputs with answers stored in
        self.targets, returning a tuple of the form

        (correct, total, score, error)

        where total is the total number of individual values in the
        target patterns, correct is the number of these that the
        network got right (to within self.tolerance), score is the
        percentage (0-100) of correct values, and error is the total
        sum squared error across all values.
        """
        total_error = 0
        correct_count = 0
        total_count = 0

        for i in range(len(inputs)):
            pattern = inputs[i]
            target = targets[i]
            output = self.propagate(pattern)

            for j in range(len(output)):
                total_error += (target[j] - output[j]) ** 2

            total_count += len(target)
            if all(abs(target[j] - output[j]) < self.tolerance for j in range(len(output))):
                correct_count += len(target)

        score = (correct_count / total_count) * 100
        return correct_count, total_count, score, total_error

    def teachPattern(self, pattern, target):
        """
            Modifies the weights according to the back-propagation
            learning rule using the given input pattern and associated
            target pattern.

            This method should begin by forward propagating activations.
            Next it should backward propagate error as follows:
            1. Update the deltas associated with every unit in the output layer.
            2. Update the deltas associated with every unit in the hidden layer.
            3. Update the increments associated with every connection in the
               network and then use these to update all weights in the network.
            """
        # Perform forward propagation
        self.propagate(pattern)

        # Backward propagation - output layer
        for i, unit in enumerate(self.outputLayer):
            error = target[i] - unit.activation
            unit.delta = error * unit.activation * (1 - unit.activation)

        # Backward propagation - hidden layer
        for unit in self.hiddenLayer:
            error = sum(connection.weight * connection.toUnit.delta for connection in unit.outgoingConnections)
            unit.delta = unit.activation * (1 - unit.activation) * error

        # Update connection weights
        for connection in self.allConnections:
            connection.increment = self.learningRate * connection.toUnit.delta * connection.fromUnit.activation
            connection.weight += connection.increment

    def teachDataset(self):
        """
        Performs one learning sweep through the training set.  Patterns
        are randomly reordered on each sweep.
        """
        assert len(self.inputs) > 0, 'no training data'
        dataset = list(zip(self.inputs, self.targets))
        random.shuffle(dataset)
        for (pattern, target) in dataset:
            # print '   teaching %s -> %s' % (pattern, target)
            self.teachPattern(pattern, target)

    def train(self, cycles=10000):
        """
        Trains the network for the given number of training cycles
        (with a default of 10000).  This method repeatedly calls
        teachDataset, displaying the current cycle number and
        performance of the network after each call.
        """
        assert len(self.inputs) > 0, 'no training data'
        for t in range(1, cycles + 1):
            self.teachDataset()
            (correct, total, score, error) = self.computeError(self.inputs, self.targets)
            print('Epoch #%5d: TSS error %7.4f, %d/%d correct (%.1f%%)' % \
                  (t, error, correct, total, score))
            if correct == total:
                print('All patterns learned')
                break



# ------------------------------------------------------------------------------
# # XOR function

x = Network(2, 3, 1)

x.inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
x.targets = [[0], [1], [1], [0]]

x.test()
x.train()
x.test()


# ------------------------------------------------------------------------------
# auto-association

# a = Network(8, 3, 8)
#
# a.inputs = [[1, 0, 0, 0, 0, 0, 0, 0],
#             [0, 1, 0, 0, 0, 0, 0, 0],
#             [0, 0, 1, 0, 0, 0, 0, 0],
#             [0, 0, 0, 1, 0, 0, 0, 0],
#             [0, 0, 0, 0, 1, 0, 0, 0],
#             [0, 0, 0, 0, 0, 1, 0, 0],
#             [0, 0, 0, 0, 0, 0, 1, 0],
#             [0, 0, 0, 0, 0, 0, 0, 1]]
#
# a.targets = a.inputs
#
# a.test()
# a.train()
# a.test()
