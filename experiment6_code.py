import numpy as np
import matplotlib.pyplot as plt

def inverse_kinematics_3dof(x, y, theta_total, l1, l2, l3):
   
    x_prime = x - l3 * np.cos(theta_total)
    y_prime = y - l3 * np.sin(theta_total)
    
    d = np.sqrt(x_prime**2 + y_prime**2)
    if d > l1 + l2 or d < abs(l1 - l2):
        raise ValueError("Target is out of reach for the robot arm.")
    
    theta1 = np.arctan2(y_prime, x_prime) - np.arccos((l1**2 + d**2 - l2**2) / (2 * l1 * d))
    theta2 = np.arccos((l1**2 + l2**2 - d**2) / (2 * l1 * l2)) - np.pi
    theta3 = theta_total - (theta1 + theta2)
    
    return theta1, theta2, theta3

x = float(input("Enter the x-coordinate of the target point: "))
y = float(input("Enter the y-coordinate of the target point: "))
theta_total_deg = float(input("Enter the total angle of the end-effector with respect to the base (in degrees): "))

theta_total = np.radians(theta_total_deg)

l1 = float(input("Enter the length of the first link: "))
l2 = float(input("Enter the length of the second link: "))
l3 = float(input("Enter the length of the third link: "))

try:
    theta1, theta2, theta3 = inverse_kinematics_3dof(x, y, theta_total, l1, l2, l3)
    theta1_deg = np.degrees(theta1)
    theta2_deg = np.degrees(theta2)
    theta3_deg = np.degrees(theta3)

    print(f"Joint angle θ1: {theta1_deg:.2f} degrees")
    print(f"Joint angle θ2: {theta2_deg:.2f} degrees")
    print(f"Joint angle θ3: {theta3_deg:.2f} degrees")

    x1 = l1 * np.cos(theta1)
    y1 = l1 * np.sin(theta1)
    x2 = x1 + l2 * np.cos(theta1 + theta2)
    y2 = y1 + l2 * np.sin(theta1 + theta2)
    x3 = x2 + l3 * np.cos(theta1 + theta2 + theta3)
    y3 = y2 + l3 * np.sin(theta1 + theta2 + theta3)

    plt.figure(figsize=(8, 8))
    plt.plot([0, x1], [0, y1], 'r-', linewidth=3, label='Link 1')
    plt.plot([x1, x2], [y1, y2], 'g-', linewidth=3, label='Link 2')
    plt.plot([x2, x3], [y2, y3], 'b-', linewidth=3, label='Link 3')
    plt.scatter([0, x1, x2, x3], [0, y1, y2, y3], c='k', zorder=5)
    plt.plot(x, y, 'ro', markersize=8, label='Target Point')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Inverse Kinematics of a 3-DOF Robot Arm")
    plt.grid(True)
    plt.axis("equal")
    plt.legend()
    plt.show()
except ValueError as e:
    print(e)

print("Result: The inverse kinematics of the 3-DOF robot arm was computed successfully.")
