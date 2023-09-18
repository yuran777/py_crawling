import statistics
import matplotlib.pyplot as plt
import numpy as np

# List of hostnames
list_hostname = [

]

# List of CPU usage percentages
list_cpu = [

]
# Insert CPU Usage
list_cpu_usage = [

]

avg_cpu = statistics.mean(list_cpu)
avg_cpu_usage = statistics.mean(list_cpu_usage)

below_avg_cpu_count = 0
below_avg_cpu_list = []

for i in range(len(list_cpu_usage)):
    if list_cpu_usage[i] <= avg_cpu:
        below_avg_cpu_count += 1
        below_avg_cpu_list.append((list_hostname[i], list_cpu_usage[i]))

above_avg_cpu_count = 0
above_avg_cpu_list = []

for i in range(len(list_cpu_usage)):
    if list_cpu_usage[i] > avg_cpu:
        above_avg_cpu_count += 1
        above_avg_cpu_list.append((list_hostname[i], list_cpu_usage[i]))

# 결과 출력
print(f"평균 CPU 사용률 이하인 CPU 개수: {below_avg_cpu_count}")
# print("평균 CPU 사용률 이하인 CPU 내역:")
# for hostname, cpu_usage in below_avg_cpu_list:
#     print(f"호스트명: {hostname}, CPU 사용률: {cpu_usage} %")

print("---------------------------------------------------")

print(f"평균 CPU 사용률 이상인 CPU 개수: {above_avg_cpu_count}")
# print("평균 CPU 사용률 이상인 CPU 내역:")
# for hostname, cpu_usage in above_avg_cpu_list:
#     print(f"호스트명: {hostname}, CPU 사용률: {cpu_usage}")
print("---------------------------------------------------")


#Insert Memory Usage
list_memory_usage = [

]
list_memory = [

]
avg_memory = statistics.mean(list_memory)
avg_memory_usge = statistics.mean(list_memory_usage)


# Define a dictionary to map hostnames to categories
# Continue adding hostname-category mappings
hostname_to_category = {

}

# # Example usage:
# print(hostname_to_category["mobdev"])  # This will print "GIS"
# print(hostname_to_category["ars_asa01"])  # This will print "이지원"


#Insert Host Name
avg_memory = statistics.mean(list_memory_usage)

below_avg_memory_count = 0
below_avg_memory_list = []

for i in range(len(list_memory_usage)):
    if list_memory_usage[i] <= avg_memory:
        below_avg_memory_count += 1
        below_avg_memory_list.append((list_hostname[i], list_cpu_usage[i]))

# 결과 출력
print(f"평균 Memory 사용률 이하인 Memory의 Host 개수: {below_avg_memory_count}")
# print("평균 Memory 사용률 이하인 Memory의 Host 내역:")
# for hostname, memory_usage in below_avg_memory_list:
#     print(f"호스트명: {hostname}, Memory 사용률: {memory_usage}")

above_avg_hostnames = []

for i in range(len(list_hostname)):
    if list_cpu_usage[i] > avg_cpu and list_memory_usage[i] > avg_memory:
        above_avg_hostnames.append(list_hostname[i])


above_avg_count = len(above_avg_hostnames)

print(f"CPU 및 Memory 사용률이 평균 이상인 Host 개수: {above_avg_count}")

# 결과 출력
# print("CPU 및 Memory 사용률이 평균 이상인 호스트:")
# for hostname in above_avg_hostnames:
#     print(hostname)


below_avg_hostnames = []

for i in range(len(list_hostname)):
    if list_cpu_usage[i] <= avg_cpu and list_memory_usage[i] <= avg_memory:
        below_avg_hostnames.append(list_hostname[i])


below_avg_count = len(below_avg_hostnames)

print(f"CPU 및 Memory 사용률이 평균 이하인 Host 개수: {below_avg_count}")

# print(len(list_cpu_usage)) # 103
# print(len(list_memory_usage)) # 103

## Ensure both lists have the same length

# min_length = min(len(list_cpu_usage), len(list_memory_usage))
# list_cpu_usage = list_cpu_usage[:min_length]
# list_memory_usage = list_memory_usage[:min_length]

marker_sizes = [cpu * memory for cpu, memory in zip(list_cpu, list_memory)]
n = 103

colors = ['red' if list_cpu_usage[i] > avg_cpu and list_memory_usage[i] > avg_memory
          else 'blue' if list_cpu_usage[i] <= avg_cpu and list_memory_usage[i] <= avg_memory
else 'orange' for i in range(n)]


plt.scatter(list_cpu_usage, list_memory_usage, s=marker_sizes, c=colors, alpha=0.6)

# Create a list to store hostnames that meet the condition
selected_hostnames = []

# Iterate through the data and identify hostnames that meet the condition
for i in range(len(list_hostname)):
    if list_cpu_usage[i] > avg_cpu and list_memory_usage[i] > avg_memory:
        selected_hostnames.append(list_hostname[i])

# Label each point with its corresponding hostname
# for i, hostname in enumerate(list_hostname):
#     plt.annotate(hostname, (list_cpu_usage[i], list_memory_usage[i]), fontsize=6)
#
# # Label each point with its corresponding hostname if it meets the condition
# for i, hostname in enumerate(list_hostname):
#     if hostname in selected_hostnames:
#         plt.annotate(hostname,
#                      (list_cpu_usage[i], list_memory_usage[i]),
#                      fontsize=7,
#                      verticalalignment='center',
#         )


plt.axhline(y=avg_memory, color='orange', linestyle='--', label=f'Avg Memory: {avg_memory:.2f} %')
plt.axvline(x=avg_cpu, color='green', linestyle='--', label=f'Avg CPU: {avg_cpu:.2f} %')

plt.xlabel("CPU Usage (%)", fontsize=15)
plt.ylabel("Memory Usage (%)", fontsize=15)

plt.grid(True)
plt.legend()
plt.show()
