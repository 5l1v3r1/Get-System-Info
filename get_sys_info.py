#improvement would be to attempt to accomplish everything with the default modules. Importing may pose issues in production environments.
import platform
import os
import sys
import shutil
import psutil
import datetime


# First, identify the system. Goal is to reduce OS identification to 3 values: 'Linux,' 'Windows' & 'OS X'
def get_platform():
    platforms = {
        'linux1': 'Linux',
        'linux2': 'Linux',
        'linux': 'Linux',
        'darwin': 'OS X',
        'win32': 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform

    return platforms[sys.platform]


# system basics.
# Arguments for Mac and Linux systems interoperated well, had to break out a few things to Windows only

class mac_nix_sys_basics():  # must be different than windows
    try:
        os = os.name
        platform = platform.release()
        # mac_host = os.uname()
        host = os.uname()[1]  # alternate if above does not work
        # mac_arch = os.uname()
        arch = os.uname()[4]  # alternate if above does not work
    except:
        pass


class win_sys_basics():  # must be different than mac
    try:
        win_hostname = platform.node()
        win_platform = platform.system()  # ID as Windows
        win_release = platform.uname()[2]  # release
        win_version = platform.uname()[3]  # version
        win_arch = platform.architecture()[0]  # arch
        win_proc = platform.processor()  # processor
        win_cpu = os.cpu_count()  # CPUs
    except:
        pass


# Disk space arguments all worked on each platform
class disk_space():  # future test, may combine with Win???
    try:
        disk_space_total = shutil.disk_usage("/")[0]
        total_to_TBs = round(disk_space_total / 1000000000000, 2)
        total_to_GBs = round(disk_space_total / 1000000000, 2)
        disk_space_used = shutil.disk_usage("/")[1]
        used_to_TBs = round(disk_space_used / 1000000000000, 2)
        used_to_GBs = round(disk_space_used / 1000000000, 2)
        disk_space_free = shutil.disk_usage("/")[2]
        free_to_TBs = round(disk_space_free / 1000000000000, 2)
        free_to_GBs = round(disk_space_free / 1000000000, 2)
        percentage_free = round(disk_space_free / disk_space_total * 100)
    except:
        pass



# memory & CPU arguments all worked on each platform
class mem_cpu():  # future test, may combine with Win???
    try:
        cores = psutil.cpu_count()
        cpu_percent = psutil.cpu_percent()
        memory_percent = psutil.virtual_memory()[2]
        memory_total = psutil.virtual_memory()[0]
        total_mem_GBs = round(memory_total / 1000000000, 2)
        disk_percent = psutil.disk_usage('/')[3]
        boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
        running_since = boot_time.strftime("%A %d. %B %Y")
    except:
        pass

# output setup - defining a timestamp to insert
tstamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")  # 03-11-2019 07:33:34  (24H)

# Audit routines
def osx_audit():
    try:
        print("Operating system identified as: ", get_platform())
        print('>>> Running OS X audit')
        print('~' * 40)
        print('~' * 40)
        print('SYSTEM REPORT')
        print('~' * 40)
        print("Operating system identified as: ", get_platform())
        print("platform.system: ", platform.system())
        print("os.name: ", mac_nix_sys_basics.os)
        print("platform.release: ", mac_nix_sys_basics.platform)
        print("Host name (os.uname):", os.uname()[1]) #issue with Class variable, used argumernt instead
        print("Arch (os.uname):", os.uname()[4]) #issue with Class variable, used argumernt instead
        print('~' * 40)
        print("Disk Space: ", disk_space.total_to_TBs, "TBs")
        print("Allocated Space: ", disk_space.used_to_TBs, "TBs")
        print("Free Space: ", disk_space.free_to_TBs, "TBs")
        print("Disk Space: ", disk_space.total_to_GBs, "GBs")
        print("Allocated Space: ", disk_space.used_to_GBs, "GBs")
        print("Free Space: ", disk_space.free_to_GBs, "GBs")
        print(disk_space.percentage_free, "% of the disk is free space")
        print('~' * 40)
        print("CPU Cores: ", mem_cpu.cores)
        print("Total Memory: ", mem_cpu.total_mem_GBs, "GBs")
        print("Memory Usage: ", mem_cpu.memory_percent, "%")
        print("Boot Time: ", mem_cpu.boot_time)
        print('~' * 40)
        print('~' * 40)
        print(get_platform() + ' audit completed on ' + tstamp)
    except:
        pass


def linux_audit():
    print("Operating system identified as: ", get_platform())
    print('>>> Running linux audit')
    print('~' * 40)
    print('~' * 40)
    print('SYSTEM REPORT')
    print('~' * 40)
    print("Operating system identified as: ", get_platform())
    print("platform.system: ", platform.system())
    print("os.name: ", mac_nix_sys_basics.os)
    print("platform.release: ", mac_nix_sys_basics.platform)
    print("Host name (os.uname):", os.uname()[1]) #issue with Class variable, used argumernt instead
    print("Arch (os.uname):", os.uname()[4]) #issue with Class variable, used argumernt instead
    print('~' * 40)
    print("Disk Space: ", disk_space.total_to_TBs, "TBs")
    print("Allocated Space: ", disk_space.used_to_TBs, "TBs")
    print("Free Space: ", disk_space.free_to_TBs, "TBs")
    print("Disk Space: ", disk_space.total_to_GBs, "GBs")
    print("Allocated Space: ", disk_space.used_to_GBs, "GBs")
    print("Free Space: ", disk_space.free_to_GBs, "GBs")
    print(disk_space.percentage_free, "% of the disk is free space")
    print('~' * 40)
    print("CPU Cores: ", mem_cpu.cores)
    print("Total Memory: ", mem_cpu.total_mem_GBs, "GBs")
    print("Memory Usage: ", mem_cpu.memory_percent, "%")
    print("Boot Time: ", mem_cpu.boot_time)
    print('~' * 40)
    print('~' * 40)
    print(get_platform() + ' audit completed on ' + tstamp)


def windows_audit():
    try:
        print("Operating system identified as: ", get_platform())
        print('>>> Running windows audit')
        print('~' * 40)
        print('~' * 40)
        print('SYSTEM REPORT')
        print('~' * 40)
        print("Operating system identified as: ", get_platform())
        print("platform: ", win_sys_basics.win_platform)
        print("Version: ", win_sys_basics.win_version)
        print("Release: ", win_sys_basics.win_release)
        print("Host name:", win_sys_basics.win_hostname)
        print("Arch:", win_sys_basics.win_arch)
        print('~' * 40)
        print("Disk Space: ", disk_space.total_to_TBs, "TBs")
        print("Allocated Space: ", disk_space.used_to_TBs, "TBs")
        print("Free Space: ", disk_space.free_to_TBs, "TBs")
        print("Disk Space: ", disk_space.total_to_GBs, "GBs")
        print("Allocated Space: ", disk_space.used_to_GBs, "GBs")
        print("Free Space: ", disk_space.free_to_GBs, "GBs")
        print(disk_space.percentage_free, "% of the disk is free space")
        print('~' * 40)
        print("CPU Cores: ", mem_cpu.cores)
        print("Total Memory: ", mem_cpu.total_mem_GBs, "GBs")
        print("Memory Usage: ", mem_cpu.memory_percent, "%")
        print("Boot Time: ", mem_cpu.boot_time)
        print("Running since: ", windows_mem_cpu.running_since)
        print('~' * 40)
        print('~' * 40)
        print(get_platform() + ' audit completed on ' + tstamp)
    except:
        pass

# main code to run Audit first then output. Goal was to show results on screen as well as save as file
def audit():
    if get_platform() == "OS X":
        osx_audit()
    elif get_platform() == "Windows":
        windows_audit()
    elif get_platform() == "Linux":
        linux_audit()
    else:
        print('Operating system not recognized, audit failed')


def output():
    if get_platform() == "OS X":
        output_file = ('sys_audit_' + platform.node() + '_.txt')
        stdout_backup = sys.stdout
        with open(output_file, 'a') as f:
            sys.stdout = f
            osx_audit()
        sys.stdout = stdout_backup
    elif get_platform() == "Windows":
        output_file = ('sys_audit_' + platform.node() + '_.txt')
        stdout_backup = sys.stdout
        with open(output_file, 'a') as f:
            sys.stdout = f
            windows_audit()
        sys.stdout = stdout_backup
    elif get_platform() == "Linux":
        output_file = ('sys_audit_' + platform.node() + '_.txt')
        stdout_backup = sys.stdout
        with open(output_file, 'a') as f:
            sys.stdout = f
            linux_audit()
        sys.stdout = stdout_backup
    else:
        print('Could not create output file')


# MAIN CODE
audit()  # runs aydit and displays on screen
output()  # writes audit results to file

