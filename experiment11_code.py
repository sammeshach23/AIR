import numpy as np
import matplotlib.pyplot as plt

def calculate_torques_and_forces(l1, l2, theta1, theta2, Fx, Fy):
    dx1 = l1 * np.cos(theta1)
    dy1 = l1 * np.sin(theta1)
    dx2 = dx1 + l2 * np.cos(theta1 + theta2)
    dy2 = dy1 + l2 * np.sin(theta1 + theta2)
    
    tau2 = Fx * l2 * np.cos(theta1 + theta2) + Fy * l2 * np.sin(theta1 + theta2)
    
    tau1 = (Fx * l1 * np.cos(theta1) + Fy * l1 * np.sin(theta1) + 
            Fx * l2 * np.cos(theta1 + theta2) + Fy * l2 * np.sin(theta1 + theta2))
    
    F1 = tau1 / l1
    F2 = tau2 / l2
    
    return tau1, tau2, F1, F2

l1 = 1.0
l2 = 1.0

theta1_deg = float(input("Enter joint 1 angle (in degrees): "))
theta2_deg = float(input("Enter joint 2 angle (in degrees): "))
Fx = float(input("Enter the force in the x-direction at the end-effector: "))
Fy = float(input("Enter the force in the y-direction at the end-effector: "))

theta1 = np.radians(theta1_deg)
theta2 = np.radians(theta2_deg)

tau1, tau2, F1, F2 = calculate_torques_and_forces(l1, l2, theta1, theta2, Fx, Fy)

print(f"Torque at Joint 1 (τ1): {tau1:.2f} Nm")
print(f"Torque at Joint 2 (τ2): {tau2:.2f} Nm")
print(f"Force at Joint 1 (F1): {F1:.2f} N")
print(f"Force at Joint 2 (F2): {F2:.2f} N")

theta1_range = np.linspace(-np.pi/2, np.pi/2, 100)
theta2_range = np.linspace(-np.pi/2, np.pi/2, 100)

tau1_values = []
tau2_values = []
F1_values = []
F2_values = []

for t1 in theta1_range:
    for t2 in theta2_range:
        tau1_temp, tau2_temp, F1_temp, F2_temp = calculate_torques_and_forces(l1, l2, t1, t2, Fx, Fy)
        tau1_values.append(tau1_temp)
        tau2_values.append(tau2_temp)
        F1_values.append(F1_temp)
        F2_values.append(F2_temp)

plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.plot(theta1_range, tau1_values[:len(theta1_range)], label=r'$\tau_1$ (Torque at Joint 1)')
plt.xlabel(r'$\theta_1$ (degrees)')
plt.ylabel('Torque (Nm)')
plt.title('Torque at Joint 1 vs Joint Angle')
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(theta2_range, tau2_values[:len(theta2_range)], label=r'$\tau_2$ (Torque at Joint 2)')
plt.xlabel(r'$\theta_2$ (degrees)')
plt.ylabel('Torque (Nm)')
plt.title('Torque at Joint 2 vs Joint Angle')
plt.legend()

plt.subplot(2, 2, 3)
plt.plot(theta1_range, F1_values[:len(theta1_range)], label=r'$F_1$ (Force on Link 1)')
plt.xlabel(r'$\theta_1$ (degrees)')
plt.ylabel('Force (N)')
plt.title('Force on Link 1 vs Joint Angle')
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(theta2_range, F2_values[:len(theta2_range)], label=r'$F_2$ (Force on Link 2)')
plt.xlabel(r'$\theta_2$ (degrees)')
plt.ylabel('Force (N)')
plt.title('Force on Link 2 vs Joint Angle')
plt.legend()

plt.tight_layout()
plt.show()
