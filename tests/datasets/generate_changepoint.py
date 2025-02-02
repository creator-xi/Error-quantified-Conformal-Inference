import numpy as np
import pandas as pd

# Define parameters for the changepoint setting
n = 2000  # Total number of data points
beta_0 = np.array([2, 1, 0, 0])
beta_1 = np.array([0, -2, -1, 0])
beta_2 = np.array([0, 0, 2, 1])

# Initialize arrays for X_t and Y_t
X_t = np.random.multivariate_normal(np.zeros(4), np.eye(4), n)
epsilon_t = np.random.normal(0, 1, n)
T = np.arange(n)
T = T + 1

# Generate Y_t based on the beta values and changepoints
Y_t = np.zeros(n)

# Define changepoints: t=500 and t=1000
for t in range(n):
    if t < 500:
        Y_t[t] = np.dot(X_t[t], beta_0) + epsilon_t[t]
    elif t < 1500:
        Y_t[t] = np.dot(X_t[t], beta_1) + epsilon_t[t]
    else:
        Y_t[t] = np.dot(X_t[t], beta_2) + epsilon_t[t]

# Create a dataframe for the data
data = pd.DataFrame(np.hstack((T.reshape(-1, 1), X_t, Y_t.reshape(-1, 1))), columns=['timestamp', 'X1', 'X2', 'X3', 'X4', 'y'])

# Save to a CSV file
csv_file_path = '/data2/wujunxi/PID/tests/datasets/changepoint.csv'
data.to_csv(csv_file_path, index=False)

print(csv_file_path)
