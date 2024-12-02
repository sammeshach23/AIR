import numpy as np
import matplotlib.pyplot as plt

def inverse_kinematics(x, y, theta_total, l1, l2):
    d = np.sqrt(x**2 + y**2)
    if d > l1 + l2 or d < abs(l1 - l2):
        raise ValueError("Target is out of reach for the robot arm.")
    alpha = np.arctan2(y, x)
    beta = np.arccos((l1**2 + d**2 - l2**2) / (2 * l1 * d))
    theta1 = alpha - beta
    theta2 = theta_total - theta1
    return theta1, theta2

x = float(input("Enter the x-coordinate of the target point: "))
y = float(input("Enter the y-coordinate of the target point: "))
theta_total_deg = float(input("Enter the total angle of the end-effector with respect to the base (in degrees): "))

theta_total = np.radians(theta_total_deg)

l1 = 1
l2 = 1

try:
    theta1, theta2 = inverse_kinematics(x, y, theta_total, l1, l2)
    theta1_deg = np.degrees(theta1)
    theta2_deg = np.degrees(theta2)

    print(f"Joint angle θ1: {theta1_deg:.2f} degrees")
    print(f"Joint angle θ2: {theta2_deg:.2f} degrees")
    
    x1 = l1 * np.cos(theta1)
    y1 = l1 * np.sin(theta1)
    x2 = x1 + l2 * np.cos(theta_total)
    y2 = y1 + l2 * np.sin(theta_total)

    print(f"Position of joint 1: ({x1:.2f}, {y1:.2f})")
    print(f"Position of end-effector: ({x2:.2f}, {y2:.2f})")
    
    plt.figure(figsize=(6, 6))
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.minorticks_on()
    plt.plot([0, x1], [0, y1], 'r-', linewidth=3, label='Link 1')
    plt.plot([x1, x2], [y1, y2], 'g-', linewidth=3, label='Link 2')
    plt.plot(x, y, 'bo', markersize=8, label='Target Point')
    plt.scatter([0, x1, x2], [0, y1, y2], c='k', zorder=5)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Inverse Kinematics of a 2-DOF Robot Arm')
    plt.xlim([-2, 2])
    plt.ylim([-2, 2])
    plt.xticks(np.arange(-2, 2.5, 0.5))
    plt.yticks(np.arange(-2, 2.5, 0.5))
    plt.legend()
    plt.show()
except ValueError as e:
    print(e)

print("Result: Thus the Inverse Kinematics of the 2D robot arm was designed successfully.")
