import psutil
import threading

cpu_process_list = []
rows = 0
listOfProcObjects = []

<<<<<<< HEAD
=======
main_process_list = []
hidden_process_list = []


def calc(proc):
    global main_process_list
    global hidden_process_list

    process_dict = {}

    process_dict['pid'] = proc.pid
    process_dict['name'] = proc.name()
    process_dict['user'] = proc.username()
    process_dict['cpu'] = proc.cpu_percent(interval=3)
    process_dict['memory'] = proc.memory_info().vms
    try:
        process_dict['path'] = proc.cwd()
        main_process_list.append(process_dict)
    except psutil.AccessDenied:
        process_dict['path'] = '-'
        hidden_process_list.append(process_dict)
    except (psutil.NoSuchProcess, psutil.ZombieProcess):
        pass


def get_task_list(process_list):
    t = []
    for process in process_list:
        t.append(threading.Thread(target=calc, args=(process,)))
    for item in t:
        item.start()
    for item in t:
        item.join()


def get_cpu_usage(process_list):
    t = []
    for process in process_list:
        t.append(threading.Thread(target=calc, args=(process,)))
    for item in t:
        item.start()

    for item in t:
        item.join()

>>>>>>> 58dba02b921e1a128b72e9db56c33d8e4cd02e64

def getListOfProcesses():

    global listOfProcObjects
<<<<<<< HEAD
    listOfProcObjects = []
=======
    global rows
>>>>>>> 58dba02b921e1a128b72e9db56c33d8e4cd02e64
    # Iterate over the list
    process_list = list(psutil.process_iter())
    get_cpu_usage(process_list)
    process_count = 0

    print(cpu_process_list)
    for proc in process_list:
        pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
        try:
            # Fetch process details as dict
            pinfo['vms'] = proc.memory_info().vms
            #(pinfo['vms'])
            pinfo['cpu'] = cpu_process_list[process_count]
            pinfo['path'] = proc.cwd()
        except psutil.AccessDenied:
            pinfo['path'] = '-'
        except (psutil.NoSuchProcess, psutil.ZombieProcess):
            pass
        listOfProcObjects.append(pinfo)
        process_count += 1
    # Sort list of dict by key vms i.e. memory usage
    #print(listOfProcObjects)
    #print(count)
    #print(error_count)
    #print(str(count-error_count))
    # rows = len(listOfProcObjects)
    # print(rows)
    listOfProcObjects = sorted(listOfProcObjects, key=lambda procObj: procObj['vms'], reverse=True)
    #print(listOfProcObjects)

    rows = len(listOfProcObjects)
    #print(rows)
    return listOfProcObjects

# getListOfProcesses()


processes = list(psutil.process_iter())

get_task_list(processes)

print(main_process_list)
print(len(main_process_list))
print("----------------------------")
print(hidden_process_list)
print(len( hidden_process_list))

