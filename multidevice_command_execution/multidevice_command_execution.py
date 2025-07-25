import paramiko
import json
import command_to_execute
import datetime

with open('multidevice_command_execution/config.json') as file:
    devices=json.load(file)

with open('multidevice_command_execution/device_logs.txt','w') as log:

    for device in devices:
        try:
            hostname=device['name']
            ip=device['ip']
            username=device['username']
            password=device['password']
            print(f"Device name:{hostname}\nDevice ip:{ip}\nDevice username:{username}\n")

            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(ip,22,username,password)
            
            cmds=command_to_execute.command_list
            timestamp=datetime.datetime.now()
            log.write(f"{timestamp} --------------------------------------------------\n")
            log.write(f"{timestamp} {hostname} ---- IP: {ip}\n")
            for cmd in cmds:
                print(cmd)
                stdin,stdout,stderr=client.exec_command(cmd)
                timestamp=datetime.datetime.now()
                log.write(f"{timestamp} CMD: {cmd}\n")
                log.write(f"{timestamp} STDOUT:{stdout.read().decode()}\n")
                log.write(f"{timestamp} STDERR:{stderr.read().decode()}\n")
                stdout.channel.close()
                stderr.channel.close()

        except Exception as e:
            log.write(f"Exception occurred during execution!!! {e}")

        finally:
            client.close()

            