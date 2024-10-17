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


def draw_brown_lines():
    # 参数设置
    T = 1.0  # 总时间
    N = 1000  # 时间步数
    num_trajectories = 10  # 布朗运动轨迹数量
    mu = 0.0  # 漂移项（对于标准布朗运动，mu=0）
    sigma = 1.0  # 波动率（扩散系数）
    dt = T / N  # 时间步长

    # 初始化存储轨迹的数组
    trajectories = np.zeros((num_trajectories, N + 1))

    # 生成随机噪声
    noise = np.random.normal(0, np.sqrt(dt), (num_trajectories, N))

    # 使用Euler-Maruyama方法模拟布朗运动
    for i in range(num_trajectories):
        trajectories[i, 0] = 0.0  # 初始位置
        for j in range(1, N + 1):
            trajectories[i, j] = trajectories[i, j - 1] + mu * dt + sigma * noise[i, j - 1]

    # 绘制布朗运动轨迹
    plt.figure(figsize=(10, 6))
    for i in range(num_trajectories):
        plt.plot(np.linspace(0, T, N + 1), trajectories[i, :], lw=1.5, alpha=0.6)
    plt.xlabel('Time')
    plt.ylabel('Position')
    plt.title('Simulated Brownian Motion Trajectories')
    plt.grid(True)

    # Ensure the output directory exists
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

        # Save the plot to a file
    output_file = os.path.join(output_dir, 'brownian_lines.png')
    plt.savefig(output_file)

    # Optionally, you can also show the plot on the screen
    plt.show()

    # Close the plot to free up resources (if you didn't call plt.show())
    plt.close()


if __name__ == "__main__":
    draw_brown_lines()
