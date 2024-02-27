# import psutil

# def get_running_processes():
#     running_processes = []
#     for proc in psutil.process_iter(['pid', 'name']):
#         running_processes.append((proc.info['pid'], proc.info['name']))
#     return running_processes

# if __name__ == "_main_":
#     processes = get_running_processes()
#     for pid, name in processes:
#         print(f"Process ID: {pid}, Name: {name}")

import subprocess

result = subprocess.run(['tasklist'], capture_output=True, text=True)
print(result.stdout)