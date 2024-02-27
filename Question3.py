import psutil

def monitor_applications():
    running_apps = {}
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] not in running_apps:
            running_apps[process.info['name']] = 1
        else:
            running_apps[process.info['name']] += 1

    for app, count in running_apps.items():
        if count > 2:
            print(f"More than 2 instances of {app} running. Terminating excess instances.")
            for process in psutil.process_iter():
                if process.name() == app:
                    process.terminate()

if __name__ == "_main_":
    monitor_applications()