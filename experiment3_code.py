import matplotlib.pyplot as plt
import numpy as np

def forward_kinematics(theta1, theta2, l1, l2):
    x = l1 * np.cos(theta1) + l2 * np.cos(theta1 + theta2)
    y = l1 * np.sin(theta1) + l2 * np.sin(theta1 + theta2)
    return x, y

theta1_deg = float(input("Enter the angle of the first joint (in degrees): "))
theta2_deg = float(input("Enter the angle of the second joint (in degrees): "))
l1 = float(input("Enter the length of the first link: "))
l2 = float(input("Enter the length of the second link: "))

theta1 = np.radians(theta1_deg)
theta2 = np.radians(theta2_deg)

x, y = forward_kinematics(theta1, theta2, l1, l2)

print(f"End-effector position: ({x:.2f}, {y:.2f})")

plt.figure(figsize=(6, 6))

x1 = l1 * np.cos(theta1)
y1 = l1 * np.sin(theta1)

plt.plot([0, x1], [0, y1], 'r-', linewidth=3)
plt.plot([x1, x], [y1, y], 'r-', linewidth=3)

plt.plot(0, 0, 'bo', markersize=10)
plt.plot(x1, y1, 'bo', markersize=10)
plt.plot(x, y, 'go', markersize=10)

plt.xlim([-l1 - l2, l1 + l2])
plt.ylim([-l1 - l2, l1 + l2])
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Two-Link Robot Arm")
plt.grid(True)

plt.show()

print("Result: The forward kinematics of the 2D robot arm has been designed successfully.")
