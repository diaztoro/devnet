#!/usr/bin/python3

routers=[]
switches=[]
devices= ["RT1", "RT2", "RT3", "SW1", "SW2", "SW3"]
devices=devices+ ["RT4", "SW4"]
for i in devices:
        if "R" in i:
            routers.append (i)
        else: 
            switches.append (i)
print(switches)