import pandas as pd
import matplotlib.pyplot as plt

# Load data
csv_file_path = 'output.csv'
data = pd.read_csv(csv_file_path)

# Prepare data
# Process the UserId field to extract only the user name before the parentheses
data['UserId'] = data['UserId'].apply(lambda x: x.split('(')[0])
data['SubmitTime'] = pd.to_datetime(data['SubmitTime'], errors='coerce')
data['EndTime'] = pd.to_datetime(data['EndTime'], errors='coerce')
data['StartTime'] = pd.to_datetime(data['StartTime'], errors='coerce')
data['Duration'] = (data['EndTime'] - data['StartTime']).dt.total_seconds() / 60  # Duração em minutos


# Submissions per user
submission_counts = data['UserId'].value_counts()
plt.figure(figsize=(10, 6))
submission_counts.plot(kind='bar', color='blue')
plt.title('Submissions per user')
plt.xlabel('User')
plt.ylabel('Number of Jobs Submitted')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('imgs/submissions_by_user.png')
plt.show()

# Job states
job_states = data['JobState'].value_counts()
plt.figure(figsize=(10, 6))
job_states.plot(kind='pie', autopct='%1.1f%%')
plt.title('Job states')
plt.ylabel('')
plt.tight_layout()
plt.savefig('imgs/job_states_distribution.png')
plt.show()

# Histogram of Job States
plt.figure(figsize=(10, 6))
data['JobState'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Job states')
plt.xlabel('Job state')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('imgs/job_states_histogram.png')
plt.show()


# Number of resources allocated per job (example with memory)
data['Mem'] = data['Tres'].apply(lambda x: int(x.split(',')[1].split('=')[1].replace('G', '').replace('M', '')) if 'mem' in x else 0)
plt.figure(figsize=(10, 6))
data['Mem'].plot(kind='hist', bins=20, color='green')
plt.title('Memory Allocated by Job')
plt.xlabel('Memory (G)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('imgs/memory_allocation_histogram.png')
plt.show()

# Duration of jobs
print("Duration of jobs (minutes):")
print(data['Duration'].describe())
plt.figure(figsize=(10, 6))
data['Duration'].plot(kind='hist', bins=30, color='purple')
plt.title('Distribuição da Duration of jobs')
plt.xlabel('Duration (Minutes)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('imgs/job_duration_histogram.png')
plt.show()


# Gráfico de Barras do Contador de Nodes
plt.figure(figsize=(10, 6))
data['NodeCnt'].value_counts().sort_index().plot(kind='bar', color='green')
plt.title('Job Distribution by Nodes')
plt.xlabel('Number of Nodes')
plt.ylabel('Number of Jobs')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('imgs/node_count_bar_chart.png')
plt.show()

# Submission Timeline Chart
plt.figure(figsize=(12, 7))
data['SubmitTime'].dt.floor('d').value_counts().sort_index().plot(kind='line', marker='o', linestyle='-')
plt.title('Jobs Submitted Over Time')
plt.xlabel('Submission Date')
plt.ylabel('Number of Jobs')
plt.grid(True)
plt.tight_layout()
plt.savefig('imgs/submission_time_line_chart.png')
plt.show()
