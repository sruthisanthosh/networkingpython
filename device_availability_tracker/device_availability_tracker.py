import paramiko,datetime
import subprocess, json, time

with open('device_availability_tracker/config.json') as file:
    device_details = json.load(file)


with open('device_availability_tracker/device_ping_logs.json','w') as log:
    devices_result=[]
    start_time=datetime.datetime.now()
    while(datetime.datetime.now()-start_time < datetime.timedelta(seconds=15)):
        for device in device_details:
            ip=device['ip']
            print(ip)
            result=subprocess.run(["ping","-c","1",ip])
            timestamp=datetime.datetime.now()

            if (result.returncode == 0):
                status="Reachable" 
            else:
                status="Unreachable"

            device_out={"Hostname":device['name'],"IP":device['ip'],"Status":status,"Timestamp":f"{timestamp}"}

            devices_result.append(device_out)
            time.sleep(5)

    json.dump(devices_result,log,indent=2)