import numpy as np
import matplotlib.pyplot as plt

def forward_kinematics_3dof(theta1, theta2, theta3, l1, l2, l3):
    x1 = l1 * np.cos(theta1)
    y1 = l1 * np.sin(theta1)

    x2 = x1 + l2 * np.cos(theta1 + theta2)
    y2 = y1 + l2 * np.sin(theta1 + theta2)

    x3 = x2 + l3 * np.cos(theta1 + theta2 + theta3)
    y3 = y2 + l3 * np.sin(theta1 + theta2 + theta3)

    return x3, y3, [(0, 0), (x1, y1), (x2, y2), (x3, y3)]

theta1_deg = float(input("Enter the angle of the first joint (in degrees): "))
theta2_deg = float(input("Enter the angle of the second joint (in degrees): "))
theta3_deg = float(input("Enter the angle of the third joint (in degrees): "))

l1 = float(input("Enter the length of the first link: "))
l2 = float(input("Enter the length of the second link: "))
l3 = float(input("Enter the length of the third link: "))

theta1 = np.radians(theta1_deg)
theta2 = np.radians(theta2_deg)
theta3 = np.radians(theta3_deg)

x, y, points = forward_kinematics_3dof(theta1, theta2, theta3, l1, l2, l3)

print(f"End-effector position: ({x:.2f}, {y:.2f})")

plt.figure(figsize=(8, 8))
plt.plot([p[0] for p in points], [p[1] for p in points], 'r-', linewidth=3, label="Robot Arm")
plt.scatter([p[0] for p in points], [p[1] for p in points], c='b', zorder=5)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("3-DOF Forward Kinematics")
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()

print("Result: The forward kinematics of the 3-DOF robot arm was computed successfully.")
