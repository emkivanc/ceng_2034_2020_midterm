import os
import requests
import sys
import time
import threading

cpu_core = os.cpu_count()

def gsc(url):
        query = requests.head(url)
        status_code = str(query.status_code)
        if(status_code[0]=="2"):
          print(url + " | Server status: " + status_code + " - SUCCES")
        elif(status_code[0]=="4"):
          print(url + " | Server status: " + status_code + " - FAIL")
        elif(status_code[0]=="5"):
          print(url + " | Server status: " + status_code + " - FAIL")

link = ['https://api.github.com', 'http://bilgisayar.mu.edu.tr/',
'https://www.python.org/', 'http://akrepnalan.com/ceng2034', 'https://github.com/caesarsalad/wow']

os.system("clear")
print("\n Hi user, welcome to script. \n")
print("General Information")
print("------------------------------------------------------------")
print("Operating System Type: ", os.name, "\n")
print("Your destination: ", os.getcwd(), "\n")
print("CPU (Core) Count: ", str(os.cpu_count()), "\n")
print("------------------------------------------------------------")
print("\n Please enter the command number to execute the script: \n"
      " 1 : Print Process ID (PID). \n"
      " 2 : Print Load Average if the OS is Linux (POSIX). \n"
      " 3 : Print 5 minute Load Average value. \n"
      " 4 : Print URL valid codes (With Threads). \n"
      " 0 : Exit the script.")
print("------------------------------------------------------------")
while(True):
  loadavg5 = os.getloadavg()
  command = input("Please enter the command number: ")

  #We multiply the cpu_core with two because we have multithread processor.
  if(cpu_core*2 - loadavg5[1] < 1):
    print("System was overloaded.")
    print("Exiting from the script.")
    sys.exit()
  
  if(command==None or command=="" or command==" "):
    print("Unvalid command number was sended.")

  if(command=="1"):
    print("Process ID(PID): "+str(os.getpid()))
  
  if(command=="2"):
    if(str(os.name)=="posix"):
      print("Load Average Values: "+str(os.getloadavg()))
    else:
      print("You can't see this values, you should use Linux (POSIX)")
  
  if(command=="3"):
    print("5 Minute Load Average Value: "+str(loadavg5[1]))

  if(command=="4"):
    time0 = time.time()

    th_1 = threading.Thread(target=gsc, args=(link[0],))
    th_2 = threading.Thread(target=gsc, args=(link[1],))
    th_3 = threading.Thread(target=gsc, args=(link[2],))
    th_4 = threading.Thread(target=gsc, args=(link[3],))
    th_5 = threading.Thread(target=gsc, args=(link[4],))
    th_1.start()
    th_2.start()
    th_3.start()
    th_4.start()
    th_5.start()
    th_1.join()
    th_2.join()
    th_3.join()
    th_4.join()
    th_5.join()

    time1 = time.time()

    print("\n" + "Completed in: " + str(time1 - time0) + " seconds." +"\n")

  if(command=="0"):
    print("Exiting from the script.")
    sys.exit()

  else:
    print("Unvalid command number was sended.")