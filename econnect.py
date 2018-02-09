#!/usr/bin/python
import os
os.system('clear')
menu_text = "\n=======================\n==EASY CONNECT SCRIPT==\n=======================\nPlease, choose one of the available options: \n1) Make FTP Connection (SFTP Protocol)\n2) Establish SSH Connection (SSH Protocol)\n3) Download file (SSH Protocol)\n4) Download folder (SSH Protocol)\n5) File upload (SSH Protocol)\n6) Folder upload (SSH Protocol)\n0) Quit"
print (menu_text)
selected = raw_input("\n")
menu_on = True
while (menu_on == True):
    if (selected == "1"):
        os.system('clear')
        print ("Option 1 selected, opening FTP (SFTP) connection")
        user = raw_input("Insert user name:\n")
        address = raw_input("Insert IP address of target machine:\n")
        port = raw_input("Insert connection port (22 by default)\n")
        if port == "":
            port = "22"
        command = ("sftp -oPort="+port+" "+user+"@"+address)
        print ("Waiting for the connection to establish")
        os.system(command)
        menu_on = False
    elif (selected == "2"):
        os.system('clear')
        print ("Option 2 selected, opening SSH connection")
        user = raw_input("Insert user name:\n")
        address = raw_input("Insert IP address of target machine:\n")
        port = raw_input("Insert connection port (22 by default)\n")
        if port == "":
            port = "22"
        command = ("ssh -p"+port+" "+user+"@"+address)
        print ("Waiting for the connection to establish")
        os.system(command)
        menu_on = False
    elif (selected == "3"):
        os.system('clear')
        print ("Option 3 selected, starting SSH file download")
        user = raw_input("Insert user name:\n")
        address = raw_input("Insert IP address of target machine:\n")
        port = raw_input("Insert port (22 by default)\n")
        if port == "":
            port = "22"
        host_path = raw_input("Insert file to download directory (where is the file?)\n")
        local_path = raw_input("Insert downloaded file destination directory (where you want the file to be saved?)\n")
        command = ("scp -P"+port+" "+user+"@"+address+":"+host_path+" "+local_path)
        print ("Waiting for the connection to establish...")
        os.system(command)
        menu_on = False
    elif (selected == "4"):
        os.system('clear')
        print ("Option 4 selected, starting SSH folder download")
        user = raw_input("Insert user name:\n")
        address = raw_input("Insert IP address of target machine:\n")
        port = raw_input("Insert port (22 by default)\n")
        if port == "":
            port == "22"
        host_path = raw_input("Insert file to download directory (where is the folder?)\n")
        local_path = raw_input("Insert downloaded folder destination directory (where you want the folder to be saved?)\n")
        command = ("scp -r -P"+port+" "+user+"@"+address+":"+host_path+" "+local_path)
        print ("Waiting for the connection to establish...")
        os.system(command)
        menu_on = False
    elif (selected == "5"):
        os.system('clear')
        print ("Option 5 selected, starting SSH file upload")
        user = raw_input("Insert user name:\n")
        address = raw_input("Insert IP address of target machine:\n")
        port = raw_input("Insert port (22 by default)\n")
        if port == "":
            port == "22"
        host_path = raw_input("Insert file to upload directory (where is the file in local?)\n")
        local_path = raw_input("Insert uploaded file destination directory (where you want the file to be uploaded?)\n")
        command = ("scp -P"+port+" "+host_path+" "+user+"@"+address+":"+local_path)
        print ("Waiting for the connection to establish...")
        os.system(command)
        menu_on = False
    elif (selected == "6"):
        os.system('clear')
        print ("Option 6 selected, starting SSH folder upload")
        user = raw_input("Insert user name:\n")
        address = raw_input("Insert IP address of target machine:\n")
        port = raw_input("Insert port (22 by default)\n")
        if port == "":
            port = "22"
        host_path = raw_input("Insert folder to upload directory (where is the folder in local?)\n")
        local_path = raw_input("Insert uploaded folder destination directory (where you want the folder to be uploaded?)\n")
        command = ("scp -r -P"+port+" "+host_path+" "+user+"@"+address+":"+local_path)
        print ("Waiting for the connection to establish...")
        os.system(command)
        menu_on = False
    elif (selected == "0"):
        print ("Closing script... bye")
        break
        exit
    else:
        menu_on = True
        os.system('clear')
        print ("Error, unknown value, please try again")
        print (menu_text)
        break
