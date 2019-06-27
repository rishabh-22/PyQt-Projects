import psutil


def get_list_of_processes():

    list_of_processes = []

    # Iterate over the list
    for proc in psutil.process_iter():
        try:
            # Fetch process details as dict
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            pinfo['vms'] = proc.memory_info().vms
            pinfo['cpu'] = proc.cpu_percent()
            pinfo['path'] = proc.cwd()

            # Append dict to list
            list_of_processes.append(pinfo)

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    # Sort list of dict by key vms i.e. memory usage
    list_of_processes = sorted(list_of_processes, key=lambda proc_obj: proc_obj['vms'])

    return list_of_processes
