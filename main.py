import pyfirmata
from time import*
import pyttsx3 as pt
import speech_recognition as sr
import socket
from tkinter import*
from tkinter import messagebox as msg
from tkinter import simpledialog as sd
top=Tk()
top.title("Abhineet Raj - Automation wizard Sample")
top.geometry("500x500")
l1=Label(text="Instructions:-",font=30)
l2=Label(text="1> Make sure you are connected to the internet\n\n2> You have connected your arduino to this device\n\n3>You have uploaded firmata software in arduino\n\n 		File -> Examples -> Firmata -> StandardFirmata",font=25)
l = Label(text="Arduino Speech Controls with Eric", font=40)
l3=Label(text="Setting up things...",font=35)
l4=Label(text="Error setting up - restart the app",font=40)
l5= Label(text="Successfully completed",font=30)
def check():
	l3.place(x=2000,y=2000)
	kh=[]
	k=""
	for i in range(1,6):
		try:
			ard=Arduino("COM"+str(i))
		except:
			kh.append(i)
	if (6 in kh):
		k="Arduino board is not connected with computer"
	kh=None
	##Arduino connectivity
	if ("127.0.0.1" in socket.gethostbyname(socket.gethostname())):
		k=k+"\nError - no internet connection"
	else:
		k=k
	if(len(k)>1):
		pt.speak("Error occurred")
		msg.showerror("Eric",k)
		l4.place(x=100,y=200)
	else:
		l5.place(x=100,y=200)
		btn3.place(x=100,y=250)
		ard.digital[2].mode=OUTPUT
		ard.digital[2].write(0)
def main():
	pt.speak("the software has been started speak something")
	gh = sr.Recognizer()
	with sr.Microphone() as source:
		lw=Label(text="Say something",font=40)
		lw.place(x=0,y=0)
		e = gh.record(source, duration=5)
		sdkf=gh.recognize_google(e)
		lw.place(x=2000,y=2000)
	if("on" in sdkf):
		ard.digital[2].write(1)
	elif("off" in sdkf):
		ard.digital[2].write(0)
	else:
		f=""
def inst():
	l1.place(x=50,y=100)
	top.geometry("700x500")
	l2.place(x=60,y=150)
	btn.place(x=100,y=350)
	l.place(x=2000,y=2000)
	w.place(x=2000,y=2000)
def sp():
	pt.speak("Hello , I am Eric and i will help you in arduino automation")
	l1.place(x=2000,y=2000)
	l2.place(x=2000,y=2000)
	btn.place(x=2000,y=2000)
	l3.place(x=100,y=200)
	check()
btn = Button(command = sp,text="Let's Continue ->",relief="groove", activeforeground="white", activebackground="black", font=36)
w=Button(command = inst,text="Let's Continue ->",relief="groove", activeforeground="white", activebackground="black", font=36)
btn3=Button(command = main,text="Speak",relief="groove", activeforeground="white", activebackground="black", font=36)
w.place(x=150,y=200)
l.place(x=120,y=100)
top.mainloop()
