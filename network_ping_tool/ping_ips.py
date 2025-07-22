

with open('/Users/sruthisanthosh/Documents/networkingpython/networkingpython/network_ping_tool/ip_list.txt') as file:
    ip_list= [ line.strip() for line in file ];

print(ip_list);

#Output:
#['8.8.8.8', '1.1.1.1', '192.0.2.1']
