#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
description: 
author: yyli
created date: 2024/10/17
"""
# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""  
description:   
author: yyli  
created date: 2024/10/16  
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
    bridge[-1] = end  # This will be overridden later in the plotting, but we keep it here for the simulation

    for i in range(1, n_steps):
        increment = np.sqrt(t[i] - t[i - 1]) * np.random.normal()
        bridge[i] = bridge[i - 1] + increment

        # Normalize so that the bridge has the correct endpoint in expectation (though we will override it visually)
    # This step is actually not necessary for our purpose since we are only interested in the visual convergence
    # but it's kept here for completeness and correctness in a standard Brownian Bridge setting
    # bridge -= bridge[-1] * t + end * t  # Uncomment this line if you want the bridge to end exactly at 'end' on average

    # Return the unnormalized bridge for visualization purposes (we will adjust the endpoint in the plot)
    return bridge


# Parameters
n_points = 100  # Number of starting points
n_steps = 1  # Number of steps in the Brownian Bridge simulation
fixed_end = 0  # The common endpoint for all Brownian Bridges

# Generate start points from N(0, 1)
start_points = np.random.normal(0, 1, n_points)

# Simulate Brownian Bridges
bridges = [brownian_bridge(start, fixed_end, n_steps) for start in start_points]

# Plot the results
plt.figure(figsize=(10, 10))
for bridge in bridges:
    # Shift the bridge so that it ends at the fixed_end point visually
    # We do this by replacing the last element of the bridge array with the fixed_end value
    bridge[-1] = fixed_end
    plt.plot(bridge, alpha=0.5, color='b')




if __name__ == "__main__":
    # Plot the common endpoint
    plt.scatter([n_steps] * n_points, [fixed_end] * n_points, c='r', s=10, label='Common Endpoint')

    # Optionally plot the start points (though they are off the chart due to scaling)
    # plt.scatter(np.zeros_like(start_points), start_points, c='g', label='Start Points')

    plt.title('Brownian Bridges Converging to a Common Endpoint')
    plt.xlabel('Steps')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.show()
