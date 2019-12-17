import platform
import os
import sys
import shutil
import psutil
import datetime

#system basics
#class systembasics:
operating_system = os.name
system = platform.system()
platform = platform.release()
host = os.uname()[1]
arch = os.uname()[4]

#disk space
disk_space_total = shutil.disk_usage("/")[0]
total_to_TBs = round(disk_space_total/1000000000000, 2)
total_to_GBs = round(disk_space_total/1000000000, 2)
disk_space_used = shutil.disk_usage("/")[1]
used_to_TBs = round(disk_space_used/1000000000000, 2)
used_to_GBs = round(disk_space_used/1000000000, 2)
disk_space_free = shutil.disk_usage("/")[2]
free_to_TBs = round(disk_space_free/1000000000000, 2)
free_to_GBs = round(disk_space_free/1000000000, 2)
percentage_free = round(disk_space_free / disk_space_total * 100)

#memory & CPU
cores = psutil.cpu_count()
cpu_percent = psutil.cpu_percent()
memory_percent = psutil.virtual_memory()[2]
memory_total = psutil.virtual_memory()[0]
total_mem_GBs = round(memory_total/1000000000, 2)
disk_percent = psutil.disk_usage('/')[3]
boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
running_since = boot_time.strftime("%A %d. %B %Y")

#screen output
print('~' * 13)
print('SYSTEM REPORT')
print('~' * 13)
print("Operating System: ", operating_system)
print("System: ", system)
print("Platform Release: ", platform)
print("Host name: ", host)
print("Architecture: ", arch)
print('~' * 13)
print("Disk Space: ", total_to_TBs, "TBs")
print("Allocated Space: ", used_to_TBs, "TBs")
print("Free Space: ", free_to_TBs, "TBs")
print("Disk Space: ", total_to_GBs, "GBs")
print("Allocated Space: ", used_to_GBs, "GBs")
print("Free Space: ", free_to_GBs, "GBs")
print(percentage_free, "% of the disk is free space")
print("CPU Cores: ", cores)
print("Total Memory: ", total_mem_GBs, "GBs")
print("Memory Usage: ", memory_percent, "%")
print("Boot Time: ", boot_time)




#print to file



"""
total, used, free = shutil.disk_usage("/")

print("Total: %d GiB" % (total // (2**30)))
print("Used: %d GiB" % (used // (2**30)))
print("Free: %d GiB" % (free // (2**30)))

"""
