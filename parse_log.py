import csv

# Path to .log file
log_file_path = '/var/log/slurm/slurm_jobcomp.log'

# Path to output .csv file
csv_file_path = 'output.csv'

# List to store data
data = []

# Read the .log file
with open(log_file_path, 'r') as file:
    for line in file:
        line = line.strip()
        if line:
            entry = {}
            pairs = line.split()
            for pair in pairs:
                key, value = pair.split('=', 1)
                entry[key] = value
            data.append(entry)

# Log Tags
fieldnames = ['JobId', 'UserId', 'GroupId', 'Name', 'JobState', 'Partition', 
              'TimeLimit', 'StartTime', 'EndTime', 'NodeList', 'NodeCnt', 
              'ProcCnt', 'WorkDir', 'ReservationName', 'Tres', 'Account', 'QOS', 
              'WcKey', 'Cluster', 'SubmitTime', 'EligibleTime', 'DerivedExitCode', 'ExitCode']

# Create and write to CSV file
with open(csv_file_path, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        # Ensure all keys are present on the line, even if some are missing
        row_sanitized = {key: row.get(key, '') for key in fieldnames}
        writer.writerow(row_sanitized)

print('The log has been converted to .csv')

