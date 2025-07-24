import subprocess;
import datetime;
import time;

with open('monitor_network/ip_list.txt') as file:
    ip_list = [ line.strip() for line in file ];

with open('monitor_network/monitor_logs','w') as log:
    end_time = datetime.datetime.now() + datetime.timedelta(minutes=1);
    
    while(datetime.datetime.now() < end_time):
        for ip in ip_list:
            result = subprocess.run(['ping','-c','1',ip],stdout=subprocess.DEVNULL, stderr = subprocess.DEVNULL);
            log.write(f"{datetime.datetime.now()} Status of {ip} is {result.returncode} \n");
            time.sleep(5);
                  