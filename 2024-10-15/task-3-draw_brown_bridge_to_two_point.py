#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
description: 
author: yyli
created date: 2024/10/17
"""
import numpy as np
import matplotlib.pyplot as plt


def brownian_bridge(start, end, n_steps):
    """
    Generate a Brownian Bridge between start and end over n_steps + 1 points.
    """
    t = np.linspace(0, 1, n_steps + 1)
    bridge = np.zeros(n_steps + 1)
    bridge[0] = start
    bridge[-1] = end

    for i in range(1, n_steps):
        bridge[i] = bridge[i - 1] + np.sqrt(t[i] - t[i - 1]) * np.random.normal()

        # Normalize so that the bridge ends exactly at the specified endpoint
    bridge -= bridge[-1] * t
    bridge += end * t

    return bridge


if __name__ == '__main__':

    # Parameters
    n_points = 200
    n_steps = 100  # Number of steps in the Brownian Bridge simulation

    # Generate start points from N(0, 1)
    start_points = np.random.normal(0, 1, n_points)

    # Generate end points: first 100 from N(3, 1), last 100 from N(-3, 1)
    end_points = np.concatenate([
        np.random.normal(3, 1, n_points // 2),
        np.random.normal(-3, 1, n_points // 2)
    ])

    # Simulate Brownian Bridges
    bridges = [brownian_bridge(start, end, n_steps) for start, end in zip(start_points, end_points)]

    # Plot the results
    plt.figure(figsize=(10, 6))
    for bridge in bridges:
        plt.plot(bridge, alpha=0.5, color='b')

    plt.scatter(np.zeros_like(start_points), start_points, c='r', label='Start Points')
    plt.scatter(np.ones_like(end_points) * n_steps, end_points, c='g', label='End Points')
    plt.title('Brownian Bridges Simulation')
    plt.xlabel('Steps')
    plt.ylabel('Value')
    plt.legend()
    plt.show()
