import numpy as np
import matplotlib.pyplot as plt

## EQ_plot
def func(x, c):
    return (x * c * np.exp(-c * x)) / (1 + np.exp(-c * x))**2

c_value = 1.0
x = np.linspace(-5, 5, 400)

y = func(x, c_value)

plt.figure(figsize=(8, 3))
plt.plot(x, y, label=r'$x \nabla f(x)$', color='blue')

# plt.title('Plot of the Function', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('Function Value', fontsize=12)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.minorticks_on()
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['bottom'].set_color('black')
plt.gca().spines['left'].set_color('black')

plt.savefig("/data2/wujunxi/ECI/tests/plots/EQ_function_plot.pdf")



# ## c_plot
# c_values = [0.1, 0.5, 1, 1.5, 2]
# coverage_prophet = [89.8, 90.2, 90.1, 90.1, 90]
# average_width_prophet = [46.23, 49.49, 47, 45.77, 45.01]
# coverage_ar = [89.4, 89.6, 89.5, 89.6, 89.6]
# average_width_ar = [17.01, 17.62, 17.12, 17.24, 17.23]
# coverage_theta = [89.7, 89.6, 89.7, 89.5, 89.5]
# average_width_theta = [17.27, 17.57, 17.46, 17.46, 17.51]

# plt.figure(figsize=(10, 5))
# plt.plot(c_values, coverage_prophet, label='Prophet', color='blue', marker='o')
# plt.plot(c_values, coverage_ar, label='AR', color='green', marker='s')
# plt.plot(c_values, coverage_theta, label='Theta', color='red', marker='^')
# plt.xlabel('c')
# plt.ylabel('Coverage')
# plt.title('Line Graph on $c$ and Coverage')
# plt.legend()
# plt.grid(True)
# plt.savefig("/data2/wujunxi/ECI/tests/plots/c_plot_cvg.pdf")

# # plt.figure(figsize=(10, 5))
# # plt.plot(c_values, average_width_prophet, label='Prophet', color='blue', marker='o')
# # plt.plot(c_values, average_width_ar, label='AR', color='green', marker='s')
# # plt.plot(c_values, average_width_theta, label='Theta', color='red', marker='^')
# # plt.xlabel('c')
# # plt.ylabel('Average Width')
# # plt.title('Line graph on $c$ and average width')
# # plt.legend()
# # plt.grid(True)

# fig, ax1 = plt.subplots(figsize=(10, 5))

# ax1.plot(c_values, average_width_prophet, label='Prophet', color='blue', marker='o', linestyle='--')
# ax1.set_ylim(40, 50)
# ax1.set_ylabel('Average Width (40-50)', color='blue')
# ax1.tick_params(axis='y', labelcolor='blue')

# ax2 = ax1.twinx()
# ax2.plot(c_values, average_width_ar, label='AR', color='green', marker='s', linestyle='-')
# ax2.plot(c_values, average_width_theta, label='Theta', color='red', marker='^', linestyle='-')
# ax2.set_ylim(16.75, 18.75)
# ax2.set_ylabel('Average Width (16.75-18.75)', color='red')
# ax2.tick_params(axis='y', labelcolor='red')

# plt.xlabel('c')
# plt.title('Line Graph on $c$ and Average Width with Dual Y-Axes (40-50 and 16.75-18.75)')
# ax1.legend(loc='upper left')
# ax2.legend(loc='lower left')

# plt.grid(True)

# plt.savefig("/data2/wujunxi/ECI/tests/plots/c_plot_width.pdf")
