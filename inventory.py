import statistics
import matplotlib.pyplot as plt
import numpy as np

# Your list of hostnames
list_hostname = [
    # ... (your hostnames here)
]

# Your CPU usage data
list_cpu = [
    # ... (your CPU usage data here)
]

# Your memory usage data
list_memory = [
    # ... (your memory usage data here)
]

# Calculate the average CPU and memory usage
avg_cpu = statistics.mean(list_cpu)
avg_memory = statistics.mean(list_memory)

# Ensure both lists have the same length
n = min(len(list_cpu), len(list_memory))

# Set a single scalar value for the size of scatter points
s = min(len(list_cpu), len(list_memory))

colors = np.random.rand(n)

# Create the scatter plot
plt.scatter(list_cpu, list_memory, s=s, c=colors, alpha=0.5, cmap='viridis')

# Label each point with its corresponding hostname
for i, hostname in enumerate(list_hostname):
    plt.annotate(hostname, (list_cpu[i], list_memory[i]), fontsize=8)

# Set labels and title
plt.xlabel("CPU Usage")
plt.ylabel("Memory Usage")
plt.title("CPU vs Memory Usage")

# Display the grid
plt.grid(True)

# Show the plot
plt.show()
