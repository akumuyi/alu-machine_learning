#!/usr/bin/env python3
"""
Defines DeepNeuralNetwork class for binary classification
"""

import numpy as np


class DeepNeuralNetwork:
    """
    Represents a deep neural network for binary classification
    """

    def __init__(self, nx, layers):
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if type(layers) is not list or len(layers) == 0:
            raise TypeError("layers must be a list of positive integers")

        self.__L = len(layers)
        self.__cache = {}
        self.__weights = {}
        prev = nx
        for i, nodes in enumerate(layers):
            if type(nodes) is not int or nodes < 1:
                raise TypeError("layers must be a list of positive integers")
            self.__weights[f"W{i + 1}"] = (
                np.random.randn(nodes, prev) * np.sqrt(2 / prev))
            self.__weights[f"b{i + 1}"] = np.zeros((nodes, 1))
            prev = nodes

    @property
    def L(self):
        return self.__L

    @property
    def cache(self):
        return self.__cache

    @property
    def weights(self):
        return self.__weights

    def forward_prop(self, X):
        self.__cache["A0"] = X
        for l in range(1, self.L + 1):
            Wl = self.__weights[f"W{l}"]
            bl = self.__weights[f"b{l}"]
            Al_prev = self.__cache[f"A{l - 1}"]
            Zl = np.matmul(Wl, Al_prev) + bl
            Al = 1 / (1 + np.exp(-Zl))
            self.__cache[f"A{l}"] = Al
        return Al, self.__cache

    def cost(self, Y, A):
        m = Y.shape[1]
        loss = -(Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A))
        return np.sum(loss) / m

    def evaluate(self, X, Y):
        A, _ = self.forward_prop(X)
        cost = self.cost(Y, A)
        prediction = np.where(A >= 0.5, 1, 0)
        return prediction, cost

    def gradient_descent(self, Y, cache, alpha=0.05):
        m = Y.shape[1]
        weights_copy = self.__weights.copy()

        for l in reversed(range(1, self.L + 1)):
            A_curr = cache[f"A{l}"]
            A_prev = cache[f"A{l - 1}"]

            if l == self.L:
                dz = A_curr - Y
            else:
                W_next = weights_copy[f"W{l + 1}"]
                dz_next = dz
                dz = np.matmul(W_next.T, dz_next) * A_curr * (1 - A_curr)

            dW = np.matmul(dz, A_prev.T) / m
            db = np.sum(dz, axis=1, keepdims=True) / m

            self.__weights[f"W{l}"] -= alpha * dW
            self.__weights[f"b{l}"] -= alpha * db

    def train(self, X, Y, iterations=5000, alpha=0.05):
        """
        Trains the neural network

        Parameters:
            X: input data, shape (nx, m)
            Y: labels, shape (1, m)
            iterations: number of iterations to train (int)
            alpha: learning rate (float)

        Returns:
            The evaluation of the training data after training
        """
        if type(iterations) is not int:
            raise TypeError("iterations must be an integer")
        if iterations <= 0:
            raise ValueError("iterations must be a positive integer")
        if type(alpha) is not float:
            raise TypeError("alpha must be a float")
        if alpha <= 0:
            raise ValueError("alpha must be positive")

        for _ in range(iterations):
            self.forward_prop(X)
            self.gradient_descent(Y, self.__cache, alpha)

        return self.evaluate(X, Y)
