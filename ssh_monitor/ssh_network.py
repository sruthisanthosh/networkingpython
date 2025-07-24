import paramiko;
import datetime;
import config;

ip=config.ip;
user=config.user;
password=config.password;

client = paramiko.SSHClient();
client.load_system_host_keys();
client.set_missing_host_key_policy(paramiko.AutoAddPolicy());
with open('ssh_monitor/monitor_device_logs.txt','w') as log:
    try:
        client.connect(ip,22,user,password);

        stdin, stdout, stderr = client.exec_command('uptime');

        
        log.write(f"{datetime.datetime.now()} STDOUT: {ip} {stdout.read().decode()}");
        log.write(f"{datetime.datetime.now()} STDERR: {ip} {stderr.read().decode()}");


    except Exception as e:
        log.write(f"Exception occured while connecting to the ssh server: {e}");

client.close();