import numpy as np

# simulation
transition_matrix = np.array([
    [.99, .01, 0, 0], # current
    [.25, .7, .05, 0], # 30 - 60
    [.1, 0, .8, .1], # 60 - 90
    [.05, 0, 0, .95] # 90 +
])

# chapman-kolmogorov
print(transition_matrix)
# probability of current to 90 + after 6 months ....
P_6 = np.linalg.matrix_power(transition_matrix, 6)
print(P_6[-1, -1])
# probability of current to 90 + after two years (24 months) ....
P_24 = np.linalg.matrix_power(transition_matrix, 24)
print(P_24[-1, -1])

# find convergence
P_100 = np.linalg.matrix_power(transition_matrix, 100)
print(P_100[-1, -1])
P_1000 = np.linalg.matrix_power(transition_matrix, 1000)
print(P_1000[-1, -1])
P_10000 = np.linalg.matrix_power(transition_matrix, 10000)
print(P_10000[-1, -1])

# pi(t) = pi(0)P^t
initial = np.array([.4, .4, .1, .1])
P_24_initial = initial.T @ np.linalg.matrix_power(transition_matrix, 24)
print(P_24_initial)
print(P_24_initial[-1])

initial_2 = np.array([.4, .2, .1, .3])
P_24_initial_2 = initial_2 @ np.linalg.matrix_power(transition_matrix, 24)
print(P_24_initial_2[-1])

# Baum-Welch Algo, Expectation maximization (EM)
# E-step: use forward-backward to calculate expected state occupancies
# M-step: update model parameters (transitions, emissions) to maximized likelihood
    # coming up with latent states that maximize the 
    # liklihood of observing the series of data from those states
# iterate until convergence




