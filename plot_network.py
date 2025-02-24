import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("docs/network_log.csv")
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['status'] = df['status'].map({'up': 1, 'down': 0})

# Create a chart
plt.figure(figsize=(12, 6))
plt.plot(df['timestamp'], df['status'], drawstyle="steps-post", label="Uptime", color='green')
plt.xlabel("Time")
plt.ylabel("Status")
plt.title("Network Uptime History")
plt.yticks([0, 1], ["Down", "Up"])
plt.legend()
plt.grid()

# Save the chart as an image
plt.savefig("docs/network_uptime_chart.png")
