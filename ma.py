from tkinter import*
import tkinter.messagebox as messagebox
import mysql.connector as mysql

def save():
    name=txt1.get()
    phone=txt2.get()
    if name=='' or phone=='':
         messagebox.showinfo("Insert Status","Please fill all the fields")
    else:
        conn=mysql.connect(host='localhost',user='root',passwd='',database='anshida')
        cursor=conn.cursor()
        cursor.execute("insert into student values('%s','%s')"%(name,phone))
        conn.commit()
        txt1.delete(0,END)
        txt2.delete(0,END)
        messagebox.showinfo("Insert Status","Inserted Successfully")
def Delete():
    name=txt1.get()
    if name=='':
        messagebox.showinfo("Insert Status","Please enter name") 
def  show():
    name=txt1.get() 
    if name=='' :
               messagebox.showinfo("details","please enter name")    
    else:
        conn=mysql.connect(host='localhost',user='root',passwd='',database='anshida')
        cursor=conn.cursor()
        cursor.execute("delete from student where name ='%s'"%name)
        rows=cursor.fetchall()
        for row in rows:
             labe=Label(root,text=row[0]+"\t"+row)
             labe.place(x=20,y=200)
                        
        conn.commit()
        txt1.delete(0,END)
        messagebox.showinfo("Insert Status","Delete Successfully")

def edit():
    name=txt1.get()
    phone=txt2.get()
    if  name=='' or phone=='':
         messagebox.showinfo("Insert Status","Please fill all the fields")
    else:
        conn=mysql.connect(host='localhost',user='root',passwd='',database='anshida')
        cursor=conn.cursor()
        cursor.execute("update student set phone='%s' where name='%s'"%(phone,name))
        conn.commit()
        txt1.delete(0,END)
        txt2.delete(0,END)
        messagebox.showinfo("Insert Status","Update Successfully")
def clear():
      txt1.delete(0,END)
      txt2.delete(0,END)
      messagebox.showinfo("Insert Status","clear Successfully")
root=Tk ()
root.geometry ("400x400")
root.resizable (False,False)
root.configure (background="orange")
root.attributes("-alpha",0.9)
root.attributes("-topmost",True)
lbl1=Label(text="name:").place(x=25,y=80)
lbl1=Label(text="phone number:").place(x=25,y=110)
txt1=Entry()
txt1.place(x=120,y=80)
txt2=Entry()
txt2.place(x=120,y=110)
btn1=Button(text="save",command=save)
btn1.place(x=100,y=140)
btn2=Button(text="delete",command=Delete)
btn2.place(x=140,y=140)
btn3=Button(text="show",command=show)
btn3.place(x=190,y=140)
btn4=Button(text="edit", command=edit)
btn4.place(x=235,y=140)
btn5=Button(text="clear",command=clear)
btn5.place(x=270,y=140)
root.mainloop()