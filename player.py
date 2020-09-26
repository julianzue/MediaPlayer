#!/usr/bin/python3

import os
from colorama import Fore, init
import vlc
import time

init()


if not "directory.txt" in os.listdir(os.getcwd()):
	addfile = open("directory.txt", "w")
	directory = input("[+] Enter default directory: ")
	addfile.write(directory)
	addfile.close()


def show():
	green = Fore.LIGHTGREEN_EX
	blue  = Fore.LIGHTBLUE_EX
	yellow = Fore.LIGHTYELLOW_EX
	red = Fore.LIGHTRED_EX
	reset = Fore.RESET

	file = open("directory.txt", "r")
	dire = file.readline()
	file.close()

	#os.system("clear")

	song = False

	while True:

		os.system("clear")
		print("")
		print("[i] " + dire)

		if song:
			print("[i] Playing: " + yellow +  file.strip("/") + reset)
		else:
			print("[i] Playing: " + red + "None" + reset)

		print("")
		
		count = 0
		files = []
		
		for item in os.listdir(dire):
			if count < 10:
				count_out = "00"+str(count)
			elif count < 100:
				count_out = "0"+str(count)
			else:
				count_out = str(count)
			
			if "." in item:
				if ".mp3" in item:
					print(count_out + " | " + green + item + reset)

			else:
				print(count_out + " | " + blue + item + reset)
				
			files.append(item+"/")
			count += 1
				
		
		print("")
		x = input("[+] > ")
		print("")
		
		if x == "exit":
			quit()
			
		elif x == "back":
			splitted = dire.split("/")
			length = len(splitted)
			dire = ""

			for string in splitted[:length-2]:
				dire += string+"/"
				
			print("[i] " + dire)

		elif x == "clear":
			os.system("clear")

		elif x == "reload":
			show()

		elif x == "help":
			print("[i] Enter Number to change directory or playing file.")
			print("[i] Enter 'back' to jump back 1 directory.")
			print("[i] Enter 'exit' to quit the program")

			time.sleep(3)

			show()
			
		else:
			if ".mp3" in files[int(x)]:

				file = ""
				
				file += files[int(x)]
				file.strip("/")

				player = vlc.MediaPlayer(dire + "/" + file)
				player.play()

				song = True			

			else:
				print("DIR | " + files[int(x)])
				dire += files[int(x)]
				print("[i] " + dire)
				
		print("")

show()