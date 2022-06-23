import os
import subprocess
import re
import concurrent.futures



os.system("touch ip_campus.txt")
def ip_threading(i):
    for x in range(100):
        for floor in range(20):
            ip = subprocess.getoutput(f"ping -c 1 20.20.{i}.{x}")
            try:
                print(re.findall(r"\d{2}.\d{3}.\d{1,}.\d{1,}",ip)[0])
            except IndexError:
                pass
            if "64 bytes from" in ip:
                ip = re.findall(r"\d{2}.\d{3}.\d{1,}.\d{1,}",ip)[0]
                os.system(f"echo {ip} >> ip_campus.txt")
                print(f"FOUND {ip}")
    return False

with concurrent.futures.ThreadPoolExecutor() as exe:
    # counter = 20
    for counter in range(0,40):
        exe.submit(ip_threading,counter)
        counter += 1
        if counter == 255:
            break
            
        
