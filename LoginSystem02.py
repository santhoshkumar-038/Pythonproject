from tkinter import*
import os

def delete1():
     screen3.destroy()

def delete2():
     screen4.destroy()

def delete3():
     screen5.destroy()
def saved():
     screen8 = Toplevel(mainWindow)
     screen8.geometry('100x100')
     screen8.title("saved")
     Label(screen8,text='saved').pack()
def save():
     filename=raw_filename.get()
     notes=raw_notes.get()

     data = open(filename,'w')
     data.write(notes)
     data.close()

     saved()

def create_notes():
     
     global raw_filename
     raw_filename=StringVar()
     global raw_notes
     raw_notes=StringVar()
     
     screen7 = Toplevel(mainWindow)
     screen7.geometry('300x250')
     screen7.title('notes')
     Label(screen7,text='Enter filename').pack()
     Entry(screen7,textvariable = raw_filename).pack()
     Label(screen7,text='Enter the some notes').pack()
     Entry(screen7,textvariable = raw_notes).pack()
     Button(screen7,text='save',command=save).pack()

def view_notes1():
     filename1=raw_filename1.get()
     data = open(filename1,'r')
     data1=data.read()
     screen8 = Toplevel(mainWindow)
     screen8.geometry('400x400')
     screen8.title("notes")
     Label(screen8,text=data1).pack()
     
def viewnotes():
     global screen7
     screen7 = Toplevel(mainWindow)
     screen7.geometry('400x400')
     screen7.title("notes")
     Label(screen7,text='please use one of the filename below').pack()
     all_files = os.listdir()
     Label(screen7,text=all_files).pack()
     global raw_filename1
     raw_filename1=StringVar()
     Entry(screen7,textvariable=raw_filename1).pack()
     Button(screen7,command=view_notes1,text='OK').pack()
     
def delete_notes1():
     filename2=raw_filename2.get()
     os.remove(filename2)
     screen10 = Toplevel(mainWindow)
     screen10.geometry('400x400')
     screen10.title("notes")
     Label(screen10,text=filename2+"removed").pack()
     
def deletenotes():
     
     screen9 = Toplevel(mainWindow)
     screen9.geometry('400x400')
     screen9.title("info")
     Label(screen9,text='please use one of the filename below').pack()
     all_files = os.listdir()
     Label(screen9,text=all_files).pack()
     global raw_filename2
     raw_filename2=StringVar()
     Entry(screen9,textvariable=raw_filename2).pack()
     Button(screen9,command=delete_notes1,text='OK').pack()
   
def session():
     global screen6
     screen6 = Toplevel(mainWindow)
     screen6.geometry('400x400')
     screen6.title("dashboard")
     Label(screen6,text='welcome to the dashboard').pack()
     Button(screen6,text='createnotes',command=create_notes).pack()
     Button(screen6,text='viewnotes',command=viewnotes).pack()
     Button(screen6,text="Deletenotes",command=deletenotes).pack()
     
def login_success():
     session()

def password_not_recognised():
     global screen4
     screen4=Toplevel(mainWindow)
     screen4.geometry('300x250')
     Label(screen4,text='Password_not_recognised').pack()
     Button(screen4,text="OK",command=delete2).pack()
     
def user_not_found():
     global screen5
     screen5 = Toplevel(mainWindow)
     screen5.geometry('300x250')
     Label(screen5,text='user_not_found').pack()
     Button(screen5,text='OK',command=delete3).pack()
     
def Register_login():

     global Username_info
     global Password_info
     
     Username_info=Username.get()
     Password_info=Password.get()

     file = open(Username_info,'w')
     file.write(Username_info+'\n')
     file.write(Password_info)
     file.close()

     username_entry.delete(0,END)
     password_entry.delete(0,END)

     Label(screen1,text="Registratin success",fg='green',font=('calibri',11)).pack()
     
def Register():

     global screen1
     screen1 = Toplevel(mainWindow)
     screen1.geometry('300x250')
     screen1.title('register')

     global Username
     global Password
     global username_entry
     global password_entry
     
     Username = StringVar()
     Password = StringVar()
     
     Label(screen1,text="Username *",width='30',height='2').pack()
     username_entry = Entry(screen1,textvariable=Username)
     username_entry.pack()
     Label('').pack()
     Label(screen1,text="Password *",width='30',height='2').pack()
     password_entry = Entry(screen1,textvariable=Password)
     password_entry.pack()
     Label('').pack()
     Button(screen1,text='Register',command=Register_login).pack()

def Login_reg():
     username1 = Username_verify.get()
     password1 = Password_verify.get()

     Username_entry1.delete(0,END)
     Password_entry1.delete(0,END)

     
     list_of_files = os.listdir()
     if username1 in list_of_files:
          file1=open(username1,'r')
          verify = file1.read().splitlines()
          if password1 in verify:
               login_success()
          else:
               password_not_recognised()
               
     else:
          user_not_found()
     
def Login():

     global screen1
     screen2 = Toplevel(mainWindow)
     screen2.geometry("300x250")

     global Username_verify
     global Password_verify
     global Username_entry1
     global Password_entry1

     Username_verify=StringVar()
     Password_verify=StringVar()

     global Username_entry2
     global Password_entry2
     
     Label(screen2,text="Please enter the login details").pack()
     Label("").pack()
     Label(screen2,text="Username",width='30',height='2').pack()
     Username_entry1 = Entry(screen2,textvariable=Username_verify)
     Username_entry1.pack()
     Label(screen2,text="Password",width='30',height='2').pack()
     Password_entry1 = Entry(screen2,textvariable=Password_verify)
     Password_entry1.pack()
     Label("").pack()
     Button(screen2,text="Login",command=Login_reg).pack()
     
def main_screen():
     global mainWindow
     mainWindow=Tk()
     mainWindow.geometry("300x200")
     mainWindow.title("Login System")
     
     Label(mainWindow,text="PP-01",bg="grey",width="300",height="2").pack()
     Label(text="").pack()
     Button(mainWindow,text="Login",height='2',width='30',command=Login).pack()
     Label(text="").pack()
     Button(mainWindow,text="Register",height='2',width='30',command=Register).pack()
     
     mainWindow.mainloop()

main_screen()
