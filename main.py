# https://pypi.org/project/psutil/
# https://scapy.net/
#https://seaborn.pydata.org/

#https://python.doctor/page-tkinter-interface-graphique-python-tutoriel
import psutil
import tkinter as tk
import time





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

	label.config(text="Download speed: " + end + "MB/s", fg = fg)
	root.after(1000, main) #wait 1 second before starting the main loop again

	recvinit = revafter #update the value of the download amount

		


if __name__ == '__main__':

	netstats = (psutil.net_io_counters())
	recvinit = netstats.bytes_recv  #initiate the value of the download amount

	root = tk.Tk()
	label = tk.Label(root, text="Download speed: N/A")
	label.pack()



	root.after(1000, main) #wait 1 second before starting the main loop
	root.mainloop()
