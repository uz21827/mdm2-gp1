import numpy as np
import matplotlib.pyplot as plt

# Constants
K0 = 0.5
CL = 2.0
k_decay = 0.03
T_infusion = 2
T_interval = 12
num_infusions = 5
Cmax_1 = 25.0
tau = num_infusions * T_interval + num_infusions * T_infusion  # Total time

# Time values from 0 to tau in small time steps for smoother plotting
time_values = np.arange(0, tau + 0.1, 0.1)

# Calculate concentrations based on the time intervals
concentrations = []

for t in time_values:
    infusion_index = int(t // (T_infusion + T_interval))
    
    # Linear increase during the infusion
    if t < (infusion_index + 1) * T_infusion:
        concentrations.append((K0 / CL) * (t - infusion_index * T_infusion) / T_infusion)
    # Exponential decay between infusions
    else:
        concentrations.append(Cmax_1 * np.exp(-k_decay * (t - (infusion_index + 1) * T_infusion - infusion_index * T_interval)))

# Plotting the graph
plt.plot(time_values, concentrations)

# Adding labels and title
plt.xlabel('Time (hours)')
plt.ylabel('Cp (mg/L)')
plt.title('IV Infusion - Multiple Linear Infusions and Exponential Decay')

# Display the plot
plt.grid(True)
plt.show()
