# Small micropython neural net implementation with ulab
# Based on https://olivierlenoir.gitlab.io/MicroPython-NeuralNetwork/MicroPythonNeuralNetwork.pdf

from ulab import numpy as np
from math import exp
from random import random
from json import load, dump


def short(a):
    return round(a, 3)


def amap(arr, func):
    """Map function to all elements of the matrix"""
    return np.array([list(map(func, m)) for m in arr])


def one_hot(cls, n):
    ret = np.zeros(n)
    ret[int(cls)] = 1.0
    return ret


def nn_weights(nn):
    print("Rounded weights")
    for i, w in enumerate(nn.weights):
        print("W{}".format(i), amap(w, short))


class DFF(object):
    """Neural Network Deep Feed Forward (DFF)"""

    def __init__(self, layers=(1, 1), weights=None, func="sigmoid"):
        self.layers = layers
        self.func = func
        self.actfunc = getattr(DFF, func)
        self.actfunc_deriv = lambda a: getattr(DFF, func)(a, deriv=True)
        if weights:
            self.weights = weights
        else:
            self.weights = [
                self.randmat(*s) for s in zip(self.layers[:-1], self.layers[1:])
            ]

    @staticmethod
    def randmat(m, n, positive_only=False):
        """Random matrix m rows by n cols"""
        if not positive_only:
            # range is -1, 1
            return np.array([[random() * 2 - 1 for _ in range(n)] for _ in range(m)])
        else:
            return np.array([[random() for _ in range(n)] for _ in range(m)])

    @staticmethod
    def sigmoid(a, deriv=False):
        """Activation function, Sigmoid"""
        if deriv:
            return a * (1 - a)
        return 1 / (1 + exp(-a))

    @staticmethod
    def relu(a, deriv=False):
        """Activation function, Rectified Linear Unit (ReLU)"""
        # print(a, deriv)
        if deriv:
            return 1.0 if a > 0 else 0.0
        return a if a > 0 else 0.0

    @staticmethod
    def tanh(a, deriv=False):
        """Activation function, tanh"""
        if deriv:
            return 1.0 - np.tanh(a) ** 2
        return np.tanh(a)

    def predict(self, a):
        """Predict input: a"""
        for w in self.weights:
            a = amap(np.dot(a, w), self.actfunc)
        return a

    def train(self, a, s, lrate=1):
        """Feed a, forward error based on s and learning rate lrate"""
        # Gradient weights
        gweights = []
        # Layers
        layers = [a]
        # Feed
        for w in self.weights:
            layers.append(amap(np.dot(layers[-1], w), self.actfunc))
        # Forward
        hl = layers.pop()
        e = (s - hl) * amap(hl, self.actfunc_deriv)
        for w in self.weights[::-1]:
            hl = layers.pop()
            gweights.append(np.dot(hl.transpose(), e))
            e = np.dot(e, w.transpose()) * amap(hl, self.actfunc_deriv)
        # Update weights
        for i, w in enumerate(self.weights):
            self.weights[i] += gweights.pop() * lrate

    def load(self, dff_file="network.json"):
        """Read data from json DFF file"""
        with open(dff_file) as f:
            parm = load(f)
        parm["weights"] = [np.array(w) for w in parm["weights"]]
        self.__init__(**parm)

    def dump(self, dff_file="network.json"):
        """Write data in json DFF file"""
        parameter = {
            "layers": self.layers,
            "weights": [w.mat for w in self.weights],
            "func": self.func,
        }
        with open(dff_file, "w") as f:
            dump(parameter, f)
