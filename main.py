# https://pypi.org/project/psutil/
# https://scapy.net/
#https://seaborn.pydata.org/

#https://python.doctor/page-tkinter-interface-graphique-python-tutoriel
import psutil
import tkinter as tk
import time
import os





def senddata(a):
	
	return (str(a/1024/1024))


def main() : 

	global recvinit

	netstats = (psutil.net_io_counters())
	revafter = netstats.bytes_recv
	
	end = senddata(revafter - recvinit)
	endcheck = float(end)
	if endcheck > 2:
		fg = "green"
	elif endcheck > 1:
		fg = "orange"
	else:
		fg = "red"

	speedlabel.config(text="Download speed: " + end + "MB/s", fg = fg)
	pinglabel.config(text="PING: " + str(getping("www.google.com")) + " ms")
	root.after(1000, main) #wait 1 second before starting the main loop again

	recvinit = revafter #update the value of the download amount

		
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
	
	 



if __name__ == '__main__':

	netstats = (psutil.net_io_counters())
	recvinit = netstats.bytes_recv  #initiate the value of the download amount

	root = tk.Tk()
	speedlabel = tk.Label(root, text="Download speed: N/A")
	speedlabel.pack()

	pinglabel = tk.Label(root, text="PING: ")
	pinglabel.pack()


	root.after(1000, main) #wait 1 second before starting the main loop
	root.mainloop()
