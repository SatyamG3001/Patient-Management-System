from tkinter import *
from tkinter import filedialog
import tkinter as tk
from tkinter.messagebox import askyesno
import sqlite3

top = Tk()
top.title("Patient Management System")
top.geometry("400x400")
top.config(bg='yellow')



 
def destroy():
           top.destroy()
def upload(event):
    print("ready to upload")
    
    top = Tk()  
    top.title("upload details")
    top.geometry("400x400")
    top.config(bg='green')
    def upload_photo(event):
        
        top.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files",".jpg"),("all files",".*")))
        
        print(top.filename)  
    def submit():
            conn = sqlite3.connect('address_book.db')
            c=conn.cursor()
            c.execute("INSERT INTO addresses VALUES (:f_name,:a_date,:doctor,:disease,:ward_no,:med_his,:file)",
              {
                    'f_name' :e1.get(),
                    'a_date' :e2.get(),
                    'doctor' :e3.get(),
                    'disease':e4.get(),
                    'ward_no':e5.get(),
                    'med_his':e6.get(),
                    'file':top.filename
                  
              })
            conn.commit()
            conn.close()
    
    def clear1():
        e1.delete(first=0,last=22)
        e2.delete(first=0,last=22)
        e3.delete(first=0,last=22)
        e4.delete(first=0,last=22)
        e5.delete(first=0,last=22)
        e6.delete(first=0,last=22)

    def destroy():
           top.destroy()
   
    photo1 = Button(top, text = "upload photo",activebackground = "pink", activeforeground = "blue")
    photo1.pack()
    photo1.bind('<Button-1>',upload_photo)
    #creating label  
    uname = Label(top, text = "Full name").place(x = 30,y = 50)  
  
    #creating label  
    Admit_date = Label(top, text = "Admit date").place(x = 30, y = 90)
    Doctor = Label(top, text = "Doctor").place(x = 30, y = 130)  
    disease  = Label(top, text = "disease").place(x = 30, y = 170)
    ward_no = Label(top, text = "ward no.").place(x = 30, y = 210)
    medical_history  = Label(top, text = "Medical history").place(x = 30, y = 250)
      
    
    e1 = Entry(top,width=20)
    e2 = Entry(top,  width = 20)
    e3 = Entry(top, width = 20)
    e4 = Entry(top, width = 20)
    e5 = Entry(top, width = 20)
    e6 = Entry(top, width = 20)
    e1.place(x=130,y=50)   
    e2.place(x=130,y=90)
    e3.place(x=130,y=130)
    e4.place(x=130,y=170)
    e5.place(x=130,y=210)
    e6.place(x=130,y=250)
    sbmitbtn = Button(top,text="Submit",activebackground="pink",activeforeground="blue",command=submit).place(x=110,y=300)
  
    clear = Button(top, text = "clear",activebackground = "yellow", activeforeground = "blue",command=clear1).place(x=190,y=300)  
    quit1 = Button(top, text = "Quit",activebackground = "yellow", activeforeground = "blue",command=destroy).place(x=260,y=300)
    
    top.mainloop()
    
     

    
def view(event):
    top = Tk()  
  
    top.geometry("400x400")   
    print("ready to view")
    
    top.title('view details')
    query_label=''
    q1 = Entry(top,width=20)
    q1.place(x=120,y=10)
   
    def query():
            conn = sqlite3.connect('address_book.db')
            c=conn.cursor() 

            c.execute("SELECT *, oid FROM addresses")
            records = c.fetchall()

           
            print_records =''
            n=int (q1.get()) -1
            for record in records[n]:
                    print_records += str(record) + "\n" + "\n"


     
            query_label=Label(top,text=print_records,width=20)
            query_label.place(x=120,y=65)       
                    

            conn.commit()
            conn.close()
    def clean():
            q1.delete(first=0,last=22)
            top.destroy()
    reg_no = Label(top, text = "Patient no.").place(x = 10, y = 10) 
    query_btn = Button(top,text='show records',command=query).place(x=250,y=10)
    uname = Label(top, text = "Full name").place(x = 30,y = 65)  
  
    #creating label  
    Admit_date = Label(top, text = "Admit date").place(x = 30, y = 95)
    Doctor = Label(top, text = "Doctor").place(x = 30, y = 125)  
    disease  = Label(top, text = "disease").place(x = 30, y = 155)
    ward_no = Label(top, text = "ward no.").place(x = 30, y = 185)
    medical_history  = Label(top, text = "Medical history").place(x = 30, y = 215)
      
    clear = Button(top,text='exit',command=clean).place(x=350,y=10)
    top.mainloop()

uname = Label(top, text = "Home Page",relief=SUNKEN,height=2).place(x=180,y=10)
widget = Button(None,text='upload',width=20,highlightcolor="blue")
widget1 = Button(None,text='view',width=20)
widget.place(x=140,y=100)
widget1.place(x=140,y=150)

widget.bind('<Button-1>', upload)
widget1.bind('<Button-1>',view)
quit1 = Button(top, text = "Quit",activebackground = "yellow", activeforeground = "blue",command=destroy).place(x=200,y=300)

widget.mainloop()
widget1.mainloop()
top.mainloop()
