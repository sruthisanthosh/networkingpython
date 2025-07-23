import subprocess;

with open('network_ping_tool/ip_list.txt') as file:
    ip_list= [ line.strip() for line in file ];

print(ip_list);

for ip in ip_list:
 result = subprocess.run(['ping','-c','3',ip]);
 print("--------------");
 print(result);
 if result.returncode == 0:
    print("Ping success!!");
else:
   print("Ping unsuccessful!!!") 


#Output:
'''['8.8.8.8', '1.1.1.1', '192.0.2.1']
PING 8.8.8.8 (8.8.8.8): 56 data bytes
64 bytes from 8.8.8.8: icmp_seq=0 ttl=118 time=8.049 ms
64 bytes from 8.8.8.8: icmp_seq=1 ttl=118 time=4.792 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=118 time=3.631 ms

--- 8.8.8.8 ping statistics ---
3 packets transmitted, 3 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 3.631/5.491/8.049/1.870 ms
--------------
CompletedProcess(args=['ping', '-c', '3', '8.8.8.8'], returncode=0)
Ping success!!
PING 1.1.1.1 (1.1.1.1): 56 data bytes
64 bytes from 1.1.1.1: icmp_seq=0 ttl=54 time=3.889 ms
64 bytes from 1.1.1.1: icmp_seq=1 ttl=54 time=4.120 ms
64 bytes from 1.1.1.1: icmp_seq=2 ttl=54 time=7.816 ms

--- 1.1.1.1 ping statistics ---
3 packets transmitted, 3 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 3.889/5.275/7.816/1.799 ms
--------------
CompletedProcess(args=['ping', '-c', '3', '1.1.1.1'], returncode=0)
Ping success!!
PING 192.0.2.1 (192.0.2.1): 56 data bytes
Request timeout for icmp_seq 0
Request timeout for icmp_seq 1

--- 192.0.2.1 ping statistics ---
3 packets transmitted, 0 packets received, 100.0% packet loss
--------------
CompletedProcess(args=['ping', '-c', '3', '192.0.2.1'], returncode=2)
Ping unsuccessful!!!
'''