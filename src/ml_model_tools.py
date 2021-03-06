#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.ticker import FormatStrFormatter, LinearLocator
from mpl_toolkits.mplot3d import Axes3D


class MLModelTools:
    """
    Tools for Machine Learning Models
    """

    def split_data(self, data, target, test_ratio=0.2):
        """
        Split data into training and test sets. Ratio defaults to 20% test
        data, i.e. 80% training data.

        Caution: if not a seed is set, a new test set is generated by each run
        which may cause problems since the ML algorithm will get to see the
        whole data set.

        Parameters
        ----------
        data : array, shape = (n_samples) or shape = (n_samples, n_features)
            Training samples X
        target : array, shape = (n_samples)
            Target values y
        test_ratio : float, optional, default 0.2
            Set ratio of wanted test data. The ratio must be a positive float
            between 0 and 1.

        Returns
        -------
        X_train : array, shape (n_samples)
            Train data
        X_test : array, shape (n_samples)
            Test data
        y_train : array, shape (n_samples)
            Train target
        y_test : array, shape (n_samples)
            Test target
        """

        shuffled_indices = np.random.permutation(data.shape[0])
        test_set_size = int(data.shape[0] * test_ratio)
        test_indices = shuffled_indices[:test_set_size]
        train_indices = shuffled_indices[test_set_size:]
        return data[train_indices], data[test_indices], target[train_indices], target[test_indices]

    def frankeFunction(self, x, y):
        """
        Franke's bivariate test function – a widely used test function in
        interpolation and fitting problems.

        Parameters
        ----------
        x : array, shape = (n_samples)
            x-coordinate values
        y : array, shape = (n_samples)
            y-coordinate values

        Returns
        -------
        2D Franke's functional values : array, shape (n_samples, n_samples)
        """

        term1 = 0.75 * np.exp(-(0.25 * (9 * x - 2)**2) -
                              0.25 * ((9 * y - 2)**2))
        term2 = 0.75 * np.exp(-((9 * x + 1)**2) / 49.0 - 0.1 * (9 * y + 1))
        term3 = 0.5 * np.exp(-(9 * x - 7)**2 / 4.0 - 0.25 * ((9 * y - 3)**2))
        term4 = -0.2 * np.exp(-(9 * x - 4)**2 - (9 * y - 7)**2)
        return term1 + term2 + term3 + term4

    def plot_Franke(self):
        """
        Plot Franke's function with x,y in [0, 1]
        """

        fig = plt.figure()
        ax = fig.gca(projection="3d")
        # Make data.
        x = np.arange(0, 1, 0.05)
        y = np.arange(0, 1, 0.05)
        x, y = np.meshgrid(x, y)

        z = self.frankeFunction(x, y)
        surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm,
                               linewidth=0, antialiased=False)
        # Customize the z axis.
        ax.set_zlim(-0.10, 1.40)
        ax.zaxis.set_major_locator(LinearLocator(10))
        ax.zaxis.set_major_formatter(FormatStrFormatter("%.02f"))
        # Add a color bar which maps values to colors.
        fig.colorbar(surf, shrink=0.5, aspect=5)
        plt.show()
