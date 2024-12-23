from cgitb import text
import tkinter as tk
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import datetime
import os
from tabulate import tabulate
import mysql.connector
#modules imported to for the software

def main():
    win=Tk()
    win=Tk()
    app=Login_Window(win)
    app=loggedin_Window(win)
    app=tk(win)
    win.mainloop()
#main windows assigned

#frontened of of loginn window
class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1000x700+300+40")
        self.root.resizable(False,False)
        
       #====Background Image
        img3=Image.open(r"image\image1.jpg")
        img3=img3.resize((1360,768),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1310,height=768)

        frame2=Frame(self.root,bg="gray")
        frame2.place(x=295,y=160,width=410,height=500)

        frame1=Frame(self.root,bg="black")
        frame1.place(x=300,y=165,width=400,height=490)
        
        frame=Frame(self.root,bg="gray")
        frame.place(x=305,y=170,width=390,height=480)
        
        img1=Image.open(r"image\image 99.jpg")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="gray",borderwidth=0)
        lblimg1.place(x=450,y=180,width=100,height=100)

        #heading
        get_str=Label(frame,text="Only for Authorized Peoples",font=("MS Serif",12,"bold"),fg="dark blue",bg="gray")
        get_str.place(x=90,y=120)

        #label
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="black",bg="gray")
        username.place(x=65,y=156)
        
        self.txtuser=StringVar()
        self.txtpass=StringVar()
        
        self.txtuser=ttk.Entry(frame,textvariable=self.txtuser,font=("times new roman",15,"bold"))
        self.txtuser.place(x=30,y=186,width=270)
        
        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="gray")
        password.place(x=65,y=226)
        
        self.txtpass=ttk.Entry(frame,textvariable=self.txtpass,font=("times new roman",15,"bold"),show="*")
        self.txtpass.place(x=30,y=256,width=270)
        
        #===icon images===
        img2=Image.open(r"image\image2.jpg")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=340,y=326,width=25,height=25)
        
        img3=Image.open(r"image\image3.jpg")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=340,y=398,width=25,height=25)
        
        #button
        loginbtn=Button(frame,text="Login",cursor="hand2",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="dark blue")
        loginbtn.place(x=195,y=303,width=160)
        
        registerbtn=Button(frame,text="Not Registered? Register",cursor="hand2",command=self.register_window,font=("times new roman",12,"bold"),borderwidth=0,fg="dark blue",bg="gray",activeforeground="black",activebackground="gray")
        registerbtn.place(x=11,y=367,width=175)

        registerbtn=Button(frame,text="Forgot Password?",cursor="hand2",command=self.forgot_password_window,font=("times new roman",12,"bold"),borderwidth=0,fg="dark blue",bg="gray",activeforeground="black",activebackground="gray")
        registerbtn.place(x=16,y=397,width=160)
      
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
#==================fucntion assigned for login window===========     
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All field required",parent=self.root)
        #elif self.txtuser.get()=="admin" and self.txtpass.get()=="admin":
        #    self.new_window=Toplevel(self.root)
        #    self.app=Face_Attendance_System(self.new_window)
        #elif self.txtuser.get()=="teacher" and self.txtpass.get()=="teacher":
        #    self.new_window=Toplevel(self.root)
        #    self.app=Attendance(self.new_window)
        else:
            conn=mysql.connector.Connect(host="127.0.0.1",user="root",password="@2001vaity",database="pythongui")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register1 where email=%s and password=%s",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get()                 
                                                                                ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid userame & Password",parent=self.root)
            else:
                open_main=messagebox.askyesno("YesNo","Student Login")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=loggedin_Window(self.new_window)
                else:
                    if not open_main:
                        self.new_window=Toplevel(self.root)
                        self.app=Login_Window(self.new_window)
                    return
            conn.commit()
            conn.close()
           
    def clear(self):
        self.txtuser.set("")
        self.txtpass.set("")
    
    #========reset Password======
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.Connect(host="127.0.0.1",user="root",password="@2001vaity",database="pythongui")
            my_cursor=conn.cursor()
            query=("select * from register1 where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct security question",parent=self.root2)
            else:
                query=("update register1 set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)
       
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Your password has been reset Succesfully",parent=self.root2)
                self.root2.destroy()
        
    #=====forget password=======
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email address to reset password")
        else:
            conn=mysql.connector.Connect(host="127.0.0.1",user="root",password="@2001vaity",database="pythongui")
            my_cursor=conn.cursor()
            query=("select * from register1 where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            if row==None:
                messagebox.showerror("My Error","Please enter the valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root.title("Forget Password")
                self.root2.geometry("340x450+610+170")
                
                l=Label(self.root2,text="Forget Password",font=("times new roman",15,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)
                
                security=Label(self.root2,text="Select Security Question",font=("times new roamn",15,"bold"),bg="white")
                security.place(x=50,y=80)
        
                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roamn",15,"bold"),state="readonly",justify=CENTER)
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Seurity No.","Your Pet Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)
        
                security_A=Label(self.root2,text="Security Answer",font=("times new roamn",15,"bold"),bg="white")
                security_A.place(x=50,y=150)
        
                self.txt_security=ttk.Entry(self.root2,font=("times new roamn",15,"bold"))
                self.txt_security.place(x=50,y=180,width=250)
                
                
                new_password=Label(self.root2,text="New Password",font=("times new roamn",15,"bold"),bg="white")
                new_password.place(x=50,y=220)
        
                self.txt_newpass=ttk.Entry(self.root2,font=("times new roamn",15,"bold"))
                self.txt_newpass.place(x=50,y=250,width=250)
                
                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roamn",15,"bold"),fg="white",bg="green")
                btn.place(x=50,y=290)
                
                
 
           
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1000x700+300+40")

        #====variables=====
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_check=IntVar()
        
        #====Background Image
        img=Image.open(r"image\image1.jpg")
        img=img.resize((1400,768),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=-50,y=0,width=1500,height=768)
        
        #=====main frame====
        frame2=Frame(self.root,bg="gray")
        frame2.place(x=140,y=90,width=720,height=570)

        frame1=Frame(self.root,bg="black")
        frame1.place(x=145,y=95,width=710,height=560)

        frame=Frame(self.root,bg="gray")
        frame.place(x=150,y=100,width=700,height=550)
        
        register_lbl=Label(frame,text="REGISTER HERE",font=("MS Serif",25,"bold"),fg="Black",bg="gray")
        register_lbl.place(x=20,y=20)
        
        #====label and entry===
        fname=Label(frame,text="First Name",font=("times new roamn",15,"bold"),bg="gray")
        fname.place(x=50,y=100)
        
        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roamn",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)
        
        l_name=Label(frame,text="Last Name",font=("times new roamn",15,"bold"),bg="gray")
        l_name.place(x=370,y=100)
        
        self.txt_l_name=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roamn",15,"bold"))
        self.txt_l_name.place(x=370,y=130,width=250)
        #row 2
        contact=Label(frame,text="Contact No",font=("times new roamn",15,"bold"),bg="gray")
        contact.place(x=50,y=170)
        
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roamn",15,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)
        
        email=Label(frame,text="Email",font=("times new roamn",15,"bold"),bg="gray")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roamn",15,"bold"))
        self.txt_email.place(x=370,y=200,width=250)
        
        #row3
        security=Label(frame,text="Select Security Question",font=("times new roamn",15,"bold"),bg="gray")
        security.place(x=50,y=240)
        
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roamn",15,"bold"),state="readonly",justify=CENTER)
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Security No.","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)
        
        security_A=Label(frame,text="Security Answer",font=("times new roamn",15,"bold"),bg="gray")
        security_A.place(x=370,y=240)
        
        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roamn",15,"bold"))
        self.txt_security.place(x=370,y=270,width=250)
        
        #row 4
        pswd=Label(frame,text="Password",font=("times new roamn",15,"bold"),bg="gray")
        pswd.place(x=50,y=310)
        
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roamn",15,"bold"))
        self.txt_pswd.place(x=50,y=340,width=250)
        
        confirm=Label(frame,text="Password",font=("times new roamn",15,"bold"),bg="gray")
        confirm.place(x=370,y=310)
        
        self.txt_confirm=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roamn",15,"bold"))
        self.txt_confirm.place(x=370,y=340,width=250)
        
        #=======checkbuttons===
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditon",font=("times new roamn",12,"bold"),bg="gray",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)
        
        #===buttons==
        img1=Image.open(r"image\image33.jpg")
        img1=img1.resize((200,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=50,y=450,width=200)
        
        img2=Image.open(r"image\image22.jpg")
        img2=img2.resize((200,50),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img2)
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2")
        b1.place(x=480,y=450,width=200)
    
    #=======function declaration
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & confirm Password must be same",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree our Terms & Condition",parent=self.root)
        else:
            conn=mysql.connector.Connect(host="127.0.0.1",user="root",password="@2001vaity",database="pythongui")
            my_cursor=conn.cursor()
            query=("select * from register1 where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist please try another email",parent=self.root)
            else:
                my_cursor.execute("insert into register1 values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()
                                                                             ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Succesfuly",parent=self.root)

    def return_login(self):
         self.root.destroy()   
class loggedin_Window():

    def __init__(self,root):
        self.root=root
        self.root.title("Logged in")
        self.root.geometry("1000x700+300+40")

        frame=Frame(self.root,bg="#E0EEEE")
        frame.place(x=0,y=0,width=1535,height=780)

        heading=Label(frame,text="SQL Database",font=("MS Serif",25,"bold"),fg="Black",bg="#E0EEEE")
        heading.place(x=450,y=80) 

        manualbtn=Button(frame,text="Manual Attendance Generator",cursor="hand2",command=self.manual_attendance_window,font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#36648B",bg="#E0EEEE",activeforeground="blue",activebackground="#E0EEEE")
        manualbtn.place(x=0,y=60,width=260)

        attenbtn=Button(frame,text="Show Attendance",cursor="hand2",command=self.attendance,font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#36648B",bg="#E0EEEE",activeforeground="blue",activebackground="#E0EEEE")
        attenbtn.place(x=0,y=20,width=260)   
    
    def manual_attendance_window(self):
        self.new_window=Toplevel(self.root)
        self.app=manual_attendance(self.new_window)
    
    def attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=attened(self.new_window)
class attened():
    
    def __init__(self,root):
            self.root=root
            os.system("trial3.py")      

class manual_attendance():
    
        def __init__(self,root):
            self.root=root
            self.root.title("Manual Attendance Window")
            self.root.geometry("340x450+610+170")
            self.root.resizable(False,False)

            frame1=Frame(self.root,bg="#008080")
            frame1.place(x=0,y=0,width=390,height=480)

            frame=Frame(self.root,bg="#E0EEEE")
            frame.place(x=5,y=5,width=329,height=438)

            get_str=Label(frame,text="Attendance",font=("MS Serif",20,"bold"),fg="black",bg="#E0EEEE")
            get_str.place(x=95,y=0)
            
            #==========user lable=================
            userid=Label(frame,text="UserID",font=("times new roman",15,"bold"),fg="black",bg="#E0EEEE")
            userid.place(x=7,y=66)
            
            #==============assinged variables================
            self.var_user=StringVar()
            self.var_date=StringVar()
            self.var_clock_in_time=StringVar()
            self.var_clock_out_time=StringVar()
            
            #=============user input==============
            self.txtuser=ttk.Entry(frame,textvariable=self.var_user,font=("times new roman",15,"bold"))
            self.txtuser.place(x=7,y=96,width=270)

            #===========date label and input==============
            date=Label(frame,text="Date",font=("times new roman",15,"bold"),fg="black",bg="#E0EEEE")
            date.place(x=7,y=126)

            self.txtuser=ttk.Entry(frame,textvariable=self.var_date,font=("time new roman",15,"bold"))
            self.txtuser.place(x=7,y=156,width=270)
            
            #===========time label and input=================
            subject=Label(frame,text="Clock In Time",font=("times new roman",15,"bold"),fg="black",bg="#E0EEEE")
            subject.place(x=7,y=188)

            self.txtuser=ttk.Entry(frame,textvariable=self.var_clock_in_time,font=("times new roman",15,"bold"))
            self.txtuser.place(x=7,y=218,width=270)
            
            #=============time label and input==============
            dtinput=Label(frame,text="Clock out Time",font=("times new roman",15,"bold"),fg="black",bg="#E0EEEE")
            dtinput.place(x=7,y=248)

            self.txtuser=ttk.Entry(frame,textvariable=self.var_clock_out_time,font=("times new roman",15,"bold"))
            self.txtuser.place(x=7,y=278,width=270)
            
            #==========current date and time output===============
            d = Label(root, text=f"{datetime.datetime.now():%a, %b/%d/%Y }", fg="black", bg="#E0EEEE", font=("times new roman", 12)).place(x=7,y=312)
            t = Label(root, text=f"{datetime.datetime.now():%H:%M:%S}", fg="black", bg="#E0EEEE", font=("times new roman", 12)).place(x=7,y=342)

            savedatabtn=Button(frame,text="Save Data",cursor="hand2",command=self.save_code,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="cyan",bg="black",activeforeground="black",activebackground="cyan")
            savedatabtn.place(x=180,y=370,width=140) 

            

        def save_code(self):
            if self.var_user.get()=="" or self.var_date.get()=="Select":
               messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                conn=mysql.connector.Connect(host="127.0.0.1", user="root", password="@2001vaity", database="pythongui")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into attend values(%s,%s,%s,%s)",(
                                                                                self.var_user.get(),
                                                                                self.var_date.get(),
                                                                                self.var_clock_in_time.get(),
                                                                                self.var_clock_out_time.get()
                                                                            ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Attendance taken Successfully",parent=self.root)

                



        
if __name__=="__main__":
    root=Tk()
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    app=Login_Window(root)
    root.mainloop()



# Code to show attendance data

import tkinter as tk
from tkinter.font import BOLD
from turtle import width
from tabulate import tabulate
import mysql.connector

mydb = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                passwd="@2001vaity",
                database="pythongui"
              )

mycursor = mydb.cursor()
mycursor.execute("SELECT user, clock_in_time, clock_out_time FROM attend")
myresult = mycursor.fetchall()

output = (tabulate(myresult, headers=['USER', 'CLOCK IN TIME', 'CLOCK OUT TIME'], tablefmt='psql'))
root = tk.Tk()
root.resizable(False,False)

# Create a tk.Text instance
myText = tk.Text(bg="light gray",fg="black",width="100",height="30")
myText.place(x=0,y=0)
myText.pack()

# Use the insert function to push whatever the output it to the screen
for thing in output:
    myText.insert(tk.END, f'{thing}')

root.mainloop()














# VSCode code to show biometric Attendance data

from operator import index
from tkinter import *
import serial
import serial.tools.list_ports
import functools

ports = serial.tools.list_ports.comports()
serialObj = serial.Serial()

root = Tk()
root.config(bg="gray")

def initComPort(index):
    currentPort = str(ports[index])
    comPortVar = str(currentPort.split(' ')[0])
    print(comPortVar)
    serialObj.port = comPortVar
    serialObj.baudrate = 9600
    serialObj.open()
for onePort in ports:
    comButton = Button(root, text=onePort, font=('Calibri','13'), height=1, width=45, command = functools.partial(initComPort, index = ports.index(onePort)))
    comButton.grid(row=ports.index(onePort),column=0)  

dataCanvas = Canvas(root, width=600, height=400, bg="white")
dataCanvas.grid(row=0,column=1,rowspan=100)

vsb = Scrollbar(root, orient='vertical',command = dataCanvas.yview)
vsb.grid(row=0,column=2, rowspan=100,sticky='ns')

dataCanvas.config(yscrollcommand = vsb.set)

dataFrame = Frame(dataCanvas, bg="white")
dataCanvas.create_window((10,0),window=dataFrame,anchor='nw')

def checkSerialPort():
    if serialObj.isopen() and serialObj.in_waiting:
        recentPacket = serialObj.readline()
        recentPacketString = recentPacket.decode('utf').rstring('\n')
        Label(dataFrame,text = recentPacketString, font = ('calibri','13'),bg='white').pack()

while True:
    root.update()
    checkSerialPort()
