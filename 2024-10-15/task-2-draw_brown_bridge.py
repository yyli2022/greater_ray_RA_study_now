#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
description: 
author: yyli
created date: 2024/10/16
"""
import os

import matplotlib.pyplot as plt
import numpy as np


def brownian_bridge(T, y, sigma, N):
    """
    Generate a Brownian Bridge with given parameters.

    Parameters:
    T (float): Time horizon.
    y (float): Terminal value of the Brownian Bridge.
    sigma (float): Diffusion coefficient.
    N (int): Number of time steps.

    Returns:
    t (numpy.ndarray): Time points.
    B_t (numpy.ndarray): Values of the Brownian Bridge at time points t.
    """
    # Time points
    t = np.linspace(0, T, N)
    dt = t[1] - t[0]

    # Initial conditions
    B_t = np.zeros(N)
    dW = np.random.normal(0, np.sqrt(dt), N - 1)  # Increments of the Wiener process

    # Iterative computation of the Brownian Bridge
    for i in range(1, N):
        drift = - y / T * t[i] * dt
        B_t[i] = B_t[i - 1] + sigma * dW[i - 1] + drift

        # Set the terminal value exactly to y
    B_t[-1] = y

    return t, B_t


def draw_active():
    # Parameters
    T = 1.0  # Time horizon
    y = 1.0  # Terminal value
    sigma = 1.0  # Diffusion coefficient
    N = 1000  # Number of time steps

    # Generate Brownian Bridge
    t, B_t = brownian_bridge(T, y, sigma, N)

    # Plot the Brownian Bridge
    plt.plot(t, B_t, label='Brownian Bridge')
    plt.xlabel('Time $ t $')
    plt.ylabel('Value $ B_t $')
    plt.title('Brownian Bridge Simulation')
    plt.legend()
    plt.grid(True)

    # Ensure the output directory exists
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

        # Save the plot to a file
    output_file = os.path.join(output_dir, 'brownian_bridge.png')
    plt.savefig(output_file)

    # Optionally, you can also show the plot on the screen
    plt.show()

    # Close the plot to free up resources (if you didn't call plt.show())
    plt.close()


if __name__ == "__main__":
    draw_active()
