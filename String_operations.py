import re
#String Operations: Strip, Split, Slice, Regex

#strip
line = "   Interface Gi0/1 is up     \n"
print(line.strip())

print("*"*10)

#split
output = "Filesystem      Size  Used Avail Use% Mounted on\n/dev/sda1        50G   25G   25G  50% /"
lines = output.split('\n')
headers = lines[0].split()
values = lines[1].split()
print(f"Mount point: {values[-1]}, Usage: {values[-2]}")

print("*"*10)

#split 2
line = " 18:09:36 up 5 days,  3:42,  2 users,  load average: 0.08, 0.09, 0.08"
parts = line.split(" up ")
print(parts)
uptime_section = parts[1].split(",")[0]  
print(uptime_section)

print("*"*10)

#slicing
interface = "GigabitEthernet0/1"
print(interface[0:15])
print(interface[15:18])

print("*"*10)

#regex 1
line = "CPU usage: user 12.5%, system 7.3%, idle 80.2%"
pattern=r'\d+\.\d+'
print(re.findall(pattern,line))

print("*"*10)

#regex 2
log_line = "Device connected with IP: 192.168.10.254 on port 22"
pattern=r'\d+\.\d+\.\d+\.\d+'
print(re.findall(pattern,log_line))

print("*"*10)