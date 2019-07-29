#Author Gagan Batri
#date - 30-07-2019
#description : creat file -> write data with different ip->read data from file-> find valid ips->creat new files with valid ips. 

import re
valid_ip = []
is_valid_ip = True
with open('ip_extract.txt','w+') as f:
    f.write("My ip is 400.65.179.203, sever ip is 10.65.34.56, \nremote ip is 100.234.55.4, and 0.4.34.222, \n remote1 ip is 234.456.77.866")

with open('ip_extract.txt') as f:
    fout = f.read()

res = re.findall(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b',fout)
print("following ip's found;")
print(f"{res}\n")
print("verifying valid ip's\n")
for i in res:
    ip_ = i.split('.')
    for j in range(4):
        if int(ip_[j]) > 255:
            is_valid_ip = False
            break
        else :
            is_valid_ip = True
    if is_valid_ip:
        valid_ip.append(i)
print("found following valid ip's;")
print(f"{valid_ip} \n")
with open('valid_ip.txt','w') as f:
    for i in range(len(valid_ip)) :
        #print("writing {} ip in file".format(valid_ip[i] ))
        f.write("ip{} : {}\n".format(i+1,valid_ip[i]))

print("valid ip written to file valid_ip.txt")