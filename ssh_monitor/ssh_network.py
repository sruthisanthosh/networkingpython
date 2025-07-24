import paramiko;
import datetime;
import config;

ip=config.ip;
user=config.user;
password=config.password;

client = paramiko.SSHClient();
client.load_system_host_keys();
client.set_missing_host_key_policy(paramiko.AutoAddPolicy());
client.connect(ip,22,user,password);

stdin, stdout, stderr = client.exec_command('uptime');

with open('monitor_device_logs.txt','w') as log:
    log.write(f"{datetime.datetime.now()} {ip} {stdout.read().decode()} {stderr.read().decode()}");

client.close();


