#!/usr/bin/python3
import time
import webbrowser
print("""++++++++++++++++Menu++++++++++++++++++
         1.Facebook Profiles
         2.Others
         3.Linux Groups""")
menu=int(input("Press 1 or 2: "))
file1=open("fb.txt")
file2=open("other.txt")
file3=open("linuxgrp")
d={1:file1,2:file2,3:file3}  #Its a dictionary
for i in d[menu]:    #d[menu] means calling value by dictionary key
    webbrowser.open(i,new=2)  #new=2 means open new tab
    time.sleep(20)            #delay 30 second
print("Finish!")
input()   #wait for user !!!
