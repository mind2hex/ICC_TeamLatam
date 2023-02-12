#!/usr/bin/python3

import sys
import socket
import time
import re


numbers = []
numbers.append("""   _
  / |
  | |
  | |
  |_|""")
numbers.append("""  ____
 |___ \\
   __) |
  / __/
 |_____|""")
numbers.append("""  _____
 |___ /
   |_ \\
  ___) |
 |____/""")
numbers.append("""  _  _
 | || |
 | || |_
 |__   _|
    |_|""")
numbers.append("""  ____
 | ___|
 |___ \\
  ___) |
 |____/""")
numbers.append("""   __
  / /_
 | '_ \\
 | (_) |
  \___/""")
numbers.append("""  _____
 |___  |
    / /
   / /
  /_/""")
numbers.append("""   ___
  ( _ )
  / _ \\
 | (_) |
  \\___/""")
numbers.append("""   ___
  / _ \\
 | (_) |
  \\__, |
    /_/""")
numbers.append("""   ___
  / _ \\
 | | | |
 | |_| |
  \\___/""")



TARGET="172.16.0.10"
PORT=11171

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((TARGET, PORT))

myfile = open("log.txt", 'w')

while True:
    info = ""
    temp = ""
    while "[*] Answer:" not in info:
        temp = mysock.recv(1024).decode()
        info += temp
        print(temp)
        myfile.write(temp)

        if "HTB" in temp:
            mysock.close()
            exit(0)
            

    challenge = info.split("_,.-'~'-.,__,.-'~'-.,__,.-BE QUICK IN INTERACTIONS-'~'-.,__,.-'~'-.,__,.-'~'-.,_")[1].split("[*] Answer:")[0].split("\n\n")

    aux = ""
    for num in challenge:
        if len(num) == 0:
            continue
        else:
            if num in numbers:
                if numbers.index(num) + 1 == 10:
                    aux += "0"
                else:
                    aux += str(numbers.index(num) + 1)

    aux += "\n"
    mysock.send(aux.encode())
