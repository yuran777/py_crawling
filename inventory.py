import statistics
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'AppleGothic'
sns.set(font="AppleGothic",
rc={"axes.unicode_minus":False}, style='white')

# List of hostnames
list_hostname = [
   
]

# List of CPU usage percentages
list_cpu = [
   
]
# Insert CPU Usage
list_cpu_usage = [
    
]

# List of memory usage percentages
list_memory_usage = [
  
]

list_memory = [

]

# 호스트 이름과 카테고리 매핑 정보
hostname_to_category = {
 
}

category = list(set(hostname_to_category.values()))

point_sizes = [cpu * memory for cpu, memory in zip(list_cpu, list_memory)]
# Create a DataFrame from the lists
df = pd.DataFrame({
    'Host': list_hostname,
    'CPU Usage (%)': list_cpu_usage,
    'Memory Usage (%)': list_memory_usage,
    'Category': [hostname_to_category.get(host) for host in list_hostname],  # Assign 'Other' if no category found
    'Point Size': point_sizes
})

# Calculate average CPU and Memory usage
avg_cpu = statistics.mean(list_cpu_usage)
avg_memory = statistics.mean(list_memory_usage)

# Create scatter plot with size and color mapping
plt.figure(figsize=(100, 8))
sns.scatterplot(x='CPU Usage (%)', y='Memory Usage (%)', size='Point Size', sizes=(80, 300), hue='Category', data=df)

# Add horizontal and vertical lines for average CPU and Memory
plt.axhline(y=avg_memory, color='orange', linestyle='--', label=f'Average Memory: {avg_memory:.2f} %')
plt.axvline(x=avg_cpu, color='green', linestyle='--', label=f'Average CPU: {avg_cpu:.2f} %')

plt.xlabel("CPU Usage (%)", fontsize=15)
plt.ylabel("Memory Usage (%)", fontsize=15)

plt.grid(True)
plt.legend()
plt.show()
