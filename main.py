# https://pypi.org/project/psutil/
# https://scapy.net/
#https://seaborn.pydata.org/

#https://python.doctor/page-tkinter-interface-graphique-python-tutoriel
import psutil
import tkinter as tk
from tkinter import *
import time
import os
import matplotlib.pyplot as plt
import matplotlib.backends.backend_tkagg as tkagg

# GLOBAL VARIABLES
speedglobal = 0
start_time = time.time()
x = []
yspeed = []
yping = []
# END GLOBAL VARIABLES



def senddata(a):
	
	return (str(a/1024/1024))


def main() : 
	global recvinit

	netstats = (psutil.net_io_counters())
	revafter = netstats.bytes_recv
	
	speed = senddata(revafter - recvinit)

	speedcheck = float(speed)
	if speedcheck > 2: 
		fg = "green"
	elif speedcheck > 1:
		fg = "orange"
	else:
		fg = "red"

	speedlabel.config(text="Download speed: " + speed + "MB/s", fg = fg,width=40)
	pinglabel.config(text="PING: " + str(getping("www.google.com")) + " ms")
	root.after(1000, main) #wait 1 second before starting the main loop again

	recvinit = revafter #update the value of the download amount

	update_plot(x, yspeed,yping,speed) #update the plot
		

		
def getping(web):
	response = os.popen("ping -n 1 " + web).read()
	if "time=" in response: #for english computers
		index = response.index("time=") + 5
		latency = float(response[index:].split(" ")[0])
		return latency
	elif "temps=" in response: #for french computers
		index = response.index("temps=") + 6
		latency = float(response[index:].split(" ")[0])
		return latency
	return -1


def update_plot(x, yspeed,yping,speed):
	
	maxtime = 10


	x_value = int(((time.time() - start_time)) % maxtime) # % means that it will loop back to 0 after maxtime seconds
	if x_value in x : #if the value is already in the list, remove it
		yspeed.pop(x.index(x_value)) #remove the oldest value
		yping.pop(x.index(x_value)) #remove the oldest value
	else:
		x.append(x_value) #add the new value to the list






	yspeed.insert(x.index(x_value),float(speed)) #insert the new value at the right index
	yping.insert(x.index(x_value),getping("www.google.com")) #insert the new value at the right index


	ax1.clear()
	ax1.set_title("Download Speed")
	ax1.set_xlabel("Time (s)")
	ax1.set_ylabel("Speed (MB/s)")	

	ax1.bar(x, yspeed, width=0.75,align='center') #plot the speed
	ax1.set_xlim(right=maxtime)



	ax2.clear()
	ax2.set_title("Ping")
	ax2.set_xlabel("Time (s)")
	ax2.set_ylabel("Ping (ms)")	
	ax2.bar(x, yping, width=0.75,align='center') #
	ax2.set_xlim(right=maxtime) #set the x limit to maxtime seconds

	

	plt.draw() #draw the plot

	 



if __name__ == '__main__':

	global recvinit

	netstats = (psutil.net_io_counters())
	recvinit = netstats.bytes_recv  #initiate the value of the download amount


	fig, (ax1,ax2) = plt.subplots(1, 2, figsize=(10, 5))
	
	

	root = tk.Tk()
	root.title("Network Monitor v1.0")

	speedlabel = tk.Label(root, text="Download speed: N/A",width=20)
	speedlabel.grid(row=0, column=0)

	pinglabel = tk.Label(root, text="PING: ")
	pinglabel.grid(row=0, column=1)

	canvas = tkagg.FigureCanvasTkAgg(fig, master=root)
	canvas.get_tk_widget().grid(row=1, column=0, columnspan=2)
	canvas.draw()

	root.after(1000, main) #wait 1 second before starting the main loop
	root.protocol("WM_DELETE_WINDOW", root.quit)

	root.mainloop()
	
		

