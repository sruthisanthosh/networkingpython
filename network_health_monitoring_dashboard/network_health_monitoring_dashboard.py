import paramiko
import json
import command_to_execute
import datetime

with open('network_health_monitoring_dashboard/config.json') as file:
    devices = json.load(file)

with open('network_health_monitoring_dashboard/device_health.json', 'w') as health_monitor_file:
    device_list = []

    for device in devices:
        hostname = device['name']
        ip = device['ip']
        username = device['username']
        password = device['password']
        print(f"Device: {hostname} | IP: {ip} | User: {username}")

        try:
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(ip, 22, username, password)

            command = []
            values = []
            timestamp = datetime.datetime.now()

            for cmd in command_to_execute.command_list:
                stdin, stdout, stderr = client.exec_command(cmd)
                output = stdout.read().decode().strip()
                result = []
                if cmd == "uptime":
                    parts = output.split(" up ")
                    result = parts[1].split(",")[0] 
                elif cmd == "ls -l":
                    for line in output.splitlines():
                            parts = line.split()
                            if len(parts) >= 9:
                                result.append( f"{parts[4]} {parts[5]} {parts[6]} {parts[7]} {parts[8]}\n")
                elif cmd == "date":
                    result = output[0:10]
                else:
                    result = output  

                command.append(cmd)
                values.append(result)

            device_info = dict(zip(command, values))
            device_info["hostname"] = hostname
            device_info["ip"] = ip
            device_info["timestamp"] = str(timestamp)

            device_list.append(device_info)
            stdout.channel.close()

        except Exception as e:
            print(f"Error connecting to {hostname} ({ip}): {e}")

        finally:
            client.close()

    json.dump(device_list, health_monitor_file, indent=2)
