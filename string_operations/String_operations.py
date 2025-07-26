import re
#String Operations: Strip, Split, Slice, Regex 
 
with open('string_operations/output_log.txt','w') as log :

    #strip
    line = "   Interface Gi0/1 is up     \n"
    log.write(f'{line.strip()}\n')

    log.write(f"{'*'*10}\n")

    #split
    output = "Filesystem      Size  Used Avail Use% Mounted on\n/dev/sda1        50G   25G   25G  50% /"
    lines = output.split('\n')
    headers = lines[0].split()
    values = lines[1].split()
    log.write(f"Mount point: {values[-1]}, Usage: {values[-2]}\n")

    log.write(f"{'*'*10}\n")

    #split 2
    line = " 18:09:36 up 5 days,  3:42,  2 users,  load average: 0.08, 0.09, 0.08"
    parts = line.split(" up ")
    uptime_section = parts[1].split(",")[0]  
    log.write(f"{uptime_section}\n")

    log.write(f"{'*'*10}\n")

    #slicing
    interface = "GigabitEthernet0/1"
    log.write(f"{interface[0:15]}\n")
    log.write(f"{interface[15:18]}\n")

    log.write(f"{'*'*10}\n")

    #regex 1
    line = "CPU usage: user 12.5%, system 7.3%, idle 80.2%"
    pattern=r'\d+\.\d+'
    result=re.findall(pattern,line)
    log.write(f"{str(result)}\n")

    log.write(f"{'*'*10}\n")

    #regex 2
    log_line = "Device connected with IP: 192.168.10.254 on port 22"
    pattern=r'\d+\.\d+\.\d+\.\d+'
    result=re.findall(pattern,log_line)
    log.write(f"{str(result)}\n")

    log.write(f"{'*'*10}\n")