import os

shutdown = input("do you wish to shut down your conputer ? (yes or no): ")

if shutdown.lower() == "no":
 exit()
elif shutdown.lower() == "yes":
  os.system("shutdown /s /t 1")
else:
  print("invalid input")