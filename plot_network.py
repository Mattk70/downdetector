import pandas as pd
import matplotlib.pyplot as plt

# Load log data
df = pd.read_csv("network_log.csv")
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Convert "up"/"down" to binary (1 = up, 0 = down)
df['status'] = df['status'].map({'up': 1, 'down': 0})

# Plot the uptime history
plt.figure(figsize=(12, 6))
plt.plot(df['timestamp'], df['status'], drawstyle="steps-post", label="Uptime (1=Up, 0=Down)", color='green')

plt.xlabel("Time")
plt.ylabel("Status")
plt.title("Network Uptime History")
plt.yticks([0, 1], ["Down", "Up"])
plt.legend()
plt.grid()

# Save the plot
plt.savefig("network_uptime_chart.png")
plt.show()
