##open file in the same location
#f = open("test.py", "r")
#print(f.read())

##open file in diff location
#f = open("C:\Users\Anisa Dian Islami\OneDrive - Sari Melati Kencana\Documents\Anisa-Pizza Hut", "r")
#print(f.read())

##delete
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")