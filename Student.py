from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
class Student:
    def __init__(self,root):
        self.root=root 
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("times new roman",25,"bold"),bg="powderblue",fg="black")
        title.pack(side=TOP,fill=X)
        subtitle=Label(self.root,text="Government High School Bailhongal",bd=5,relief=GROOVE,font=("times new roman",15,"bold"),bg="lime",fg="red")
        subtitle.pack(side=TOP,fill=X)

        self.Sl_no_var=StringVar()
        self.Record_no_var=StringVar()
        self.name_var=StringVar()
        self.sats_var=StringVar()
        self.father_var=StringVar()
        self.gender_var=StringVar()
        self.mother_var=StringVar()
        self.dob_var=StringVar()
        self.caste_cate_var=StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="silver")
        Manage_Frame.place(x=20,y=100,width=450,height=593)

        m_title=Label(Manage_Frame,text="Manage Students",bg="silver",fg="black",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=15)


        lbl_sl=Label(Manage_Frame,text="Sl.no",bg="silver",fg="black",font=("times new roman",15,"bold"))
        lbl_sl.grid(row=1,column=0,pady=5,padx=20,sticky="w")
        txt_sl=Entry(Manage_Frame,textvariable=self.Sl_no_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_sl.grid(row=1,column=1,pady=5,padx=20,sticky="w")

        lbl_record=Label(Manage_Frame,text="Record_no",bg="silver",fg="black",font=("times new roman",15,"bold"))
        lbl_record.grid(row=2,column=0,pady=5,padx=20,sticky="w")
        txt_record=Entry(Manage_Frame,textvariable=self.Record_no_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_record.grid(row=2,column=1,pady=5,padx=20,sticky="w")

        lbl_Name=Label(Manage_Frame,text="Name",bg="silver",fg="black",font=("times new roman",15,"bold"))
        lbl_Name.grid(row=3,column=0,pady=5,padx=20,sticky="w")
        txt_Name=Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Name.grid(row=3,column=1,pady=5,padx=20,sticky="w")

        lbl_Sats=Label(Manage_Frame,text="Sats no",bg="silver",fg="black",font=("times new roman",15,"bold"))
        lbl_Sats.grid(row=4,column=0,pady=5,padx=20,sticky="w")
        txt_Sats=Entry(Manage_Frame,textvariable=self.sats_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Sats.grid(row=4,column=1,pady=5,padx=20,sticky="w")


        lbl_Father=Label(Manage_Frame,text="Father Name",bg="silver",fg="black",font=("times new roman",15,"bold"))
        lbl_Father.grid(row=7,column=0,pady=5,padx=20,sticky="w")
        txt_Father=Entry(Manage_Frame,textvariable=self.father_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Father.grid(row=7,column=1,pady=5,padx=20,sticky="w")

        lbl_Gender=Label(Manage_Frame,text="Gender",bg="silver",fg="black",font=("times new roman",15,"bold"))
        lbl_Gender.grid(row=5,column=0,pady=5,padx=20,sticky="w")
        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman",13,"bold"),state="readonly")
        combo_gender["values"]=["male","female"]
        combo_gender.grid(row=5,column=1,padx=20,pady=5,sticky="w")

        lbl_Mother=Label(Manage_Frame,text="Mother Name",bg="silver",fg="black",font=("times new roman",15,"bold"))
        lbl_Mother.grid(row=8,column=0,pady=5,padx=20,sticky="w")
        txt_Mother=Entry(Manage_Frame,textvariable=self.mother_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Mother.grid(row=8,column=1,pady=5,padx=20,sticky="w")

        lbl_Dob=Label(Manage_Frame,text="DOB",bg="silver",fg="black",font=("times new roman",15,"bold"))
        lbl_Dob.grid(row=6,column=0,pady=5,padx=20,sticky="w")
        txt_Dob=Entry(Manage_Frame,textvariable=self.dob_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Dob.grid(row=6,column=1,pady=5,padx=20,sticky="w")

        lbl_Add=Label(Manage_Frame,text="Birthplace",bg="silver",fg="black",font=("times new roman",15,"bold"))
        lbl_Add.grid(row=10,column=0,pady=5,padx=20,sticky="w")
        self.txt_Add=Text(Manage_Frame,width=18,height=2,font=("",15))
        self.txt_Add.grid(row=10,column=1,pady=5,padx=20,sticky="w")

        lbl_cast=Label(Manage_Frame,text="Caste/Category",bg="silver",fg="black",font=("times new roman",15,"bold"))
        lbl_cast.grid(row=9,column=0,pady=5,padx=20,sticky="w")
        txt_cast=Entry(Manage_Frame,textvariable=self.caste_cate_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_cast.grid(row=9,column=1,pady=5,padx=20,sticky="w")

       

        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="silver")
        btn_Frame.place(x=15,y=550,width=420,height=35)

        Addbtn=Button(btn_Frame,text="Add",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=2)
        Updatebtn=Button(btn_Frame,text="Update",width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=2)
        Deletebtn=Button(btn_Frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=2)
        Clearbtn=Button(btn_Frame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=2)



        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="silver")
        Detail_Frame.place(x=500,y=100,width=800,height=593)


        lbl_Search=Label(Detail_Frame,text="Search By",bg="silver",fg="black",font=("times new roman",20,"bold"))
        lbl_Search.grid(row=0,column=0,pady=8,padx=20,sticky="w")
        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state="readonly")
        combo_search["values"]=["Record_no","Name","Sats_no"]
        combo_search.grid(row=0,column=1,padx=20,pady=8,sticky="w")
        txt_Search=Entry(Detail_Frame,textvariable=self.search_txt,width=15,font=("times new roman",14,"bold"),bd=5,relief=GROOVE)
        txt_Search.grid(row=0,column=2,pady=8,padx=20,sticky="w")

        searchbtn=Button(Detail_Frame,text="Search",width=10,pady=5,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(Detail_Frame,text="Show All",width=10,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)



        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="silver")
        Table_Frame.place(x=10,y=70,width=760,height=500)
        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame,columns=("Sl_no","Record_no","name","sats","gender","dob","father","mother","birthplace","castecate"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("Sl_no",text="Sl_no")
        self.Student_table.heading("Record_no",text="Record_no")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("sats",text="SATS no")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("dob",text="D.O.B")
        self.Student_table.heading("father",text="Father name")
        self.Student_table.heading("mother",text="Mother name")
        self.Student_table.heading("birthplace",text="Birthplace")
        self.Student_table.heading("castecate",text="Caste/Category")
        self.Student_table["show"]="headings"
        self.Student_table.column("Sl_no",width=50)
        self.Student_table.column("Record_no",width=100)
        self.Student_table.column("name",width=150)
        self.Student_table.column("sats",width=100)
        self.Student_table.column("gender",width=100)
        self.Student_table.column("dob",width=100)
        self.Student_table.column("father",width=100)
        self.Student_table.column("mother",width=100)
        self.Student_table.column("birthplace",width=100)
        self.Student_table.column("castecate",width=150)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()
    def add_students(self):
        if self.Record_no_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error","All fields are required!!!")
        else:    
            con=pymysql.connect(host="localhost",user="root",password="",database="stm1")
            cur=con.cursor()
            cur.execute("Insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.Sl_no_var.get(),
                                                                        self.Record_no_var.get(),
                                                                        self.name_var.get(),
                                                                        self.sats_var.get(),
                                                                        self.gender_var.get(),
                                                                        self.dob_var.get(),
                                                                        self.father_var.get(),
                                                                        self.mother_var.get(),
                                                                        self.caste_cate_var.get(),
                                                                        self.txt_Add.get('1.0',END)
                                                                        ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record has been inserted")                                                                

    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm1")
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()        
    def clear(self):
        self.Record_no_var.set("")
        self.Sl_no_var.set("")
        self.name_var.set("")
        self.sats_var.set("")
        self.gender_var.set("")
        self.father_var.set("")
        self.mother_var.set("") 
        self.dob_var.set("")
        self.caste_cate_var.set("") 
        self.txt_Add.delete("1.0",END)
    

    def get_cursor(self,ev):
        cursor_row=self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents['values']
        self.Sl_no_var.set(row[0])
        self.Record_no_var.set(row[1])
        self.name_var.set(row[2])
        self.sats_var.set(row[3])
        self.gender_var.set(row[4])
        self.dob_var.set(row[5])
        self.father_var.set(row[6]) 
        self.mother_var.set(row[7])
        self.caste_cate_var.set(row[8]) 
        self.txt_Add.delete("1.0",END)
        self.txt_Add.insert(END,row[9])

    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm1")
        cur=con.cursor()
        cur.execute("Update students set Record_no=%s,name=%s,sats_no=%s,gender=%s,dob=%s,father=%s,mother=%s,castecate=%s,birthplace=%s  where Sl_no=%s",(
                                                                                                                                                           self.Record_no_var.get(),
                                                                                                                                                           self.name_var.get(),
                                                                                                                                                           self.sats_var.get(),
                                                                                                                                                           self.gender_var.get(),
                                                                                                                                                           self.dob_var.get(),
                                                                                                                                                           self.father_var.get(),
                                                                                                                                                           self.mother_var.get(),
                                                                                                                                                           self.caste_cate_var.get(),
                                                                                                                                                           self.txt_Add.get('1.0',END),
                                                                                                                                                           self.Sl_no_var.get()
                                                                                                                                                           ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
   
    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm1")
        cur=con.cursor()
        cur.execute("delete from students where Record_no=%s",self.Record_no_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
   
    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm1")
        cur=con.cursor()
        cur.execute("select * from students where"+str(self.search_by.get())+" LIKE "+ "'%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()   
      


root=Tk()
ob=Student(root)
root.mainloop()