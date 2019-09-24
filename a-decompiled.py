import os,sys,time,mechanize
def menu():
	kntl = input(" ")
	if kntl =="":
		exit()
	elif kntl =="A":
		os.system ("python ind.py")
	elif kntl =="a":
		os.system ("python ind.py")
	elif kntl =="B":
		os.system ("sh install.sh")
		exit()
	elif kntl =="b":
		os.system ("sh install.sh")
		exit()
menu()

