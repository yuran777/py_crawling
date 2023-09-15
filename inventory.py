import statistics
from matplotlib import pyplot as plt
import pandas as pd
import plotly.express as px

# 호스트, CPU 사용률, Memory 사용률 데이터
list_hostname = [
    # 호스트 이름 목록
]

list_cpu = [
]

list_cpu_usage = [
    # 호스트별 CPU 사용률 데이터
]

list_memory = [
]
list_memory_usage = [
    # 호스트별 Memory 사용률 데이터
]

# 호스트 이름과 카테고리 매핑 정보
hostname_to_category = {
    # 호스트 이름에 해당하는 카테고리 매핑 정보
}

# 평균 CPU 및 Memory 사용률 계산
avg_cpu = statistics.mean(list_cpu_usage)
avg_memory = statistics.mean(list_memory_usage)

# CPU 및 Memory 사용률에 따라 호스트 분류
above_avg_hostnames = []
below_avg_hostnames = []

for i in range(len(list_hostname)):
    if list_cpu_usage[i] > avg_cpu and list_memory_usage[i] > avg_memory:
        above_avg_hostnames.append(list_hostname[i])
    else:
        below_avg_hostnames.append(list_hostname[i])

# Scatter plot 그리기
n = min(len(list_cpu_usage), len(list_memory_usage))
colors = ['red' if list_cpu_usage[i] > avg_cpu and list_memory_usage[i] > avg_memory
          else 'blue' if list_cpu_usage[i] <= avg_cpu and list_memory_usage[i] <= avg_memory
          else 'orange' for i in range(n)]

marker_sizes = [cpu * memory for cpu, memory in zip(list_cpu_usage, list_memory_usage)]

plt.scatter(list_cpu_usage, list_memory_usage, s=marker_sizes, c=colors, alpha=0.6)

# 각 데이터 포인트에 호스트 이름 추가
for i, hostname in enumerate(list_hostname):
    plt.annotate(hostname, (list_cpu_usage[i], list_memory_usage[i]), fontsize=6)

# 조건을 충족하는 호스트에만 호스트 이름 추가
for i, hostname in enumerate(list_hostname):
    if hostname in above_avg_hostnames:
        plt.annotate(hostname,
                     (list_cpu_usage[i], list_memory_usage[i]),
                     fontsize=7,
                     verticalalignment='center')

# CPU 및 Memory 사용률 평균에 대한 가로 및 세로 선 추가
plt.axhline(y=avg_memory, color='orange', linestyle='--', label=f'평균 Memory: {avg_memory:.2f} %')
plt.axvline(x=avg_cpu, color='green', linestyle='--', label=f'평균 CPU: {avg_cpu:.2f} %')

plt.xlabel("CPU 사용률 (%)", fontsize=15)
plt.ylabel("Memory 사용률 (%)", fontsize=15)

plt.grid(True)
plt.legend()
plt.show()

# Plotly를 사용하여 카테고리별로 그래프 그리기
data = {
    'Host': list_hostname,
    'Category': [hostname_to_category.get(hostname, 'Unknown') for hostname in list_hostname]
}

df = pd.DataFrame(data)

df['CPU Usage'] = list_cpu_usage
df['Memory Usage'] = list_memory_usage

fig = px.scatter(
    df,
    x='CPU Usage',
    y='Memory Usage',
    color='Category',
    size='CPU Usage * Memory Usage',
    hover_name='Host',
    title='호스트 카테고리별 CPU 및 Memory 사용률',
)

fig.show()
