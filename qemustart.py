#!/bin/python3

import sys,os,time

try:
	folder = os.path.exists("/etc/qemustart")

	if(folder != True):
		os.system("mkdir /etc/qemustart")
	
	user_input = sys.argv
	parameter = user_input[1]
	ssh_port = user_input[2]
	
	if(parameter == "-u"):
		a = os.path.exists("/etc/qemustart/kernel-qemu-4.4.34-jessie")
		if(a == True):
			print("already installed")
			print("start: qemustart -s [ssh_port]       #Open the SSH port of the simulator")
		else:
			print("Start installation...")
			print("Please wait a few minutes")
			time.sleep(0.5)
			os.system("wget https://downloads.raspberrypi.org/raspbian/images/raspbian-2017-04-10/2017-04-10-raspbian-jessie.zip -P /etc/qemustart/")
			time.sleep(0.5)
			os.system("unzip /etc/qemustart/2017-04-10-raspbian-jessie.zip")
			time.sleep(0.5)
			os.system("wget https://github.com/dhruvvyas90/qemu-rpi-kernel/blob/master/kernel-qemu-4.4.34-jessie -P /etc/qemustart/")
			os.system("apt-get install qemu-system")
			print("")
			os.system("mv qemustart.py /etc/qemustart/")
			os.system("sudo ln -s /etc/qemustart/qemustart.py /usr/bin/qemustart")
			time.sleep(0.5)
			print("installation is complete")
		
	elif(parameter == "-s"):
		os.system("qemu-system-arm -kernel /etc/qemustart/kernel-qemu-4.4.34-jessie -cpu arm1176 -m 256 -M versatilepb -serial stdio -append 'root=/dev/sda2 rootfstype=ext4 rw' -hda /etc/qemustart/2017-04-10-raspbian-jessie.img -nic user,hostfwd=tcp::{}".format(ssh_port)+"-:22 -no-reboot")

	
except:
	print("install: ./qemustart.py -u install")
	print("start: qemustart -s [ssh_port]       #Open the SSH port of the simulator")

