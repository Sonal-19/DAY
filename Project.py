from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector 
from tkinter import messagebox


class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title('Employee Management System')

        lbl_title=Label(self.root,text='EMPLOYEE MANAGEMENT SYSTEM',font=('times new roman',32,'bold'),fg='crimson',bg='white')
        lbl_title.place(x=0,y=0,width=1530,height=50)

        #Variables
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_designation=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_married=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_idproofcomb=StringVar()
        self.var_idproof=StringVar()
        self.var_gender=StringVar()
        self.var_phone=StringVar()
        self.var_country=StringVar()
        self.var_salary=StringVar()

        #img logo
        img_logo=Image.open('empimages/logo1.jpg')
        img_logo=img_logo.resize((70,70),Image.Resampling.LANCZOS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=330,y=0,width=50,height=50)
         
        #frame
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=50,width=1523,height=140)

        
        #empimg1
        img_1=Image.open('empimages/empimg7.png')
        img_1=img_1.resize((540,140),Image.Resampling.LANCZOS)
        self.photo1=ImageTk.PhotoImage(img_1)

        self.img_1=Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=540,height=140)

        #empimg2
        img_2=Image.open('empimages/empimg6.png')
        img_2=img_2.resize((540,140),Image.Resampling.LANCZOS)
        self.photo2=ImageTk.PhotoImage(img_2)

        self.img_2=Label(img_frame,image=self.photo2)
        self.img_2.place(x=540,y=0,width=540,height=140)

        #empimg3
        img_3=Image.open('empimages/empimg5.png')
        img_3=img_3.resize((540,140),Image.Resampling.LANCZOS)
        self.photo3=ImageTk.PhotoImage(img_3)

        self.img_3=Label(img_frame,image=self.photo3)
        self.img_3.place(x=1000,y=0,width=540,height=140)

        #main frame
        main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        main_frame.place(x=0,y=192,width=1526,height=596)

        #upper frame
        upper_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text='Employee Information',font=('times new roman',13,'bold'),fg='red',bg='white')
        upper_frame.place(x=10,y=10,width=1495,height=220)
    
        #Labels and Entry fields
        #Department
        lbl_dep=Label(upper_frame,text="Department",font=("arial",10,"bold"),bg="white")
        lbl_dep.grid(row=0,column=0,padx=2,pady=7,sticky=W)

        combo_dep=ttk.Combobox(upper_frame,textvariable=self.var_dep,font=("arial",10,"bold"),width=22,state="readonly")
        combo_dep["value"]=("Select Department","HR","Manager","Software Developer","Software Engineer")
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=7,pady=7,sticky=W)


        #Name
        lbl_Name=Label(upper_frame,text="Name:",font=("arial",10,"bold"),fg="black",bg="white")
        lbl_Name.grid(row=0,column=2,padx=2,pady=7,sticky=W)

        txt_name=ttk.Entry(upper_frame,textvariable=self.var_name,width=24,font=("arial",10,"bold"))
        txt_name.grid(row=0,column=3,padx=7,pady=7,sticky=W)

        #Designation
        lbl_Designation=Label(upper_frame,text="Designation:",font=("arial",10,"bold"),fg="black",bg="white")
        lbl_Designation.grid(row=1,column=0,padx=2,pady=7,sticky=W)

        txt_Designation=ttk.Entry(upper_frame,textvariable=self.var_designation,width=24,font=("arial",10,"bold"))
        txt_Designation.grid(row=1,column=1,padx=7,pady=7,sticky=W)

        #Email
        lbl_Email=Label(upper_frame,text="Email:",font=("arial",10,"bold"),fg="black",bg="white")
        lbl_Email.grid(row=1,column=2,padx=2,pady=7,sticky=W)

        txt_email=ttk.Entry(upper_frame,textvariable=self.var_email,width=24,font=("arial",10,"bold"))
        txt_email.grid(row=1,column=3,padx=7,pady=7,sticky=W)

        #Address
        lbl_Address=Label(upper_frame,text="Address:",font=("arial",10,"bold"),fg="black",bg="white")
        lbl_Address.grid(row=2,column=0,padx=2,pady=7,sticky=W)

        txt_address=ttk.Entry(upper_frame,textvariable=self.var_address,width=24,font=("arial",10,"bold"))
        txt_address.grid(row=2,column=1,padx=7,pady=7,sticky=W)

        #Married
        lbl_married_status=Label(upper_frame,text="Married Status:",font=("arial",10,"bold"),fg="black",bg="white")
        lbl_married_status.grid(row=2,column=2,padx=2,pady=7,sticky=W)

        com_txt_married=ttk.Combobox(upper_frame,textvariable=self.var_married,state="readonly",font=("arial",10,"bold"),width=22)
        com_txt_married['value']=("Select Option","Married","Unmarried")
        com_txt_married.current(0)
        com_txt_married.grid(row=2,column=3,padx=7,pady=7,sticky=W)

        #DOB
        lbl_dob=Label(upper_frame,text="DOB:",font=("arial",10,"bold"),fg="black",bg="white")
        lbl_dob.grid(row=3,column=0,padx=2,pady=7,sticky=W)

        txt_dob=ttk.Entry(upper_frame,textvariable=self.var_dob,width=24,font=("arial",10,"bold"))
        txt_dob.grid(row=3,column=1,padx=7,pady=7,sticky=W)

        #DOJ
        lbl_doj=Label(upper_frame,text="DOJ:",font=("arial",10,"bold"),fg="black",bg="white")
        lbl_doj.grid(row=3,column=2,padx=2,pady=7,sticky=W)

        txt_doj=ttk.Entry(upper_frame,textvariable=self.var_doj,width=24,font=("arial",10,"bold"))
        txt_doj.grid(row=3,column=3,padx=7,pady=7,sticky=W)

        #ID Proof
        com_txt_proof=ttk.Combobox(upper_frame,textvariable=self.var_idproofcomb,state="readonly",font=("arial",10,"bold"),width=16)
        com_txt_proof['value']=("Select ID Proof","PAN CARD","ADHAR CARD","DRIVING LICENCE")
        com_txt_proof.current(0)
        com_txt_proof.grid(row=4,column=0,padx=2,pady=7,sticky=W)

        txt_proof=ttk.Entry(upper_frame,textvariable=self.var_idproof,width=24,font=("arial",10,"bold"))
        txt_proof.grid(row=4,column=1,padx=7,pady=7,sticky=W)


        #Gender
        lbl_gender=Label(upper_frame,text="Gender:",font=("arial",10,"bold"),fg="black",bg="white")
        lbl_gender.grid(row=4,column=2,padx=2,pady=7,sticky=W)

        com_txt_gender=ttk.Combobox(upper_frame,textvariable=self.var_gender,state="readonly",font=("arial",10,"bold"),width=22)
        com_txt_gender['value']=("Select Gender","Male","Female")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=4,column=3,padx=7,pady=7,sticky=W)

        #phone
        lbl_phone=Label(upper_frame,text="Phone No:",font=("arial",10,"bold"),fg="black",bg="white")
        lbl_phone.grid(row=0,column=4,padx=2,pady=7,sticky=W)

        txt_phone=ttk.Entry(upper_frame,textvariable=self.var_phone,width=24,font=("arial",10,"bold"))
        txt_phone.grid(row=0,column=5,padx=7,pady=7)

        #country
        lbl_country=Label(upper_frame,text="Country:",font=("arial",10,"bold"),fg="black",bg="white")
        lbl_country.grid(row=1,column=4,padx=2,pady=7,sticky=W)

        txt_country=ttk.Entry(upper_frame,textvariable=self.var_country,width=24,font=("arial",10,"bold"))
        txt_country.grid(row=1,column=5,padx=7,pady=7)

        #CTC
        lbl_ctc=Label(upper_frame,text="Salary(CTC):",font=("arial",10,"bold"),fg="black",bg="white")
        lbl_ctc.grid(row=2,column=4,padx=2,pady=7,sticky=W)

        txt_ctc=ttk.Entry(upper_frame,textvariable=self.var_salary,width=24,font=("arial",10,"bold"))
        txt_ctc.grid(row=2,column=5,padx=7,pady=7)


        #empimg4
        img_4=Image.open('empimages/empimg11.webp')
        img_4=img_4.resize((170,180),Image.Resampling.LANCZOS)
        self.photo4=ImageTk.PhotoImage(img_4)

        self.img_4=Label(upper_frame,image=self.photo4)
        self.img_4.place(x=1000,y=5,width=170,height=180)

        #Button Frame
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=1280,y=10,width=170,height=170)

        btn_add=Button(button_frame,text="Save",command=self.add_data,font=("arial",13,"bold"),width=14,bg="deepskyblue",fg="white")
        btn_add.grid(row=0,column=0,padx=2,pady=3)

        btn_update=Button(button_frame,text="Update",command=self.update_data,font=("arial",13,"bold"),width=14,bg="deepskyblue",fg="white")
        btn_update.grid(row=1,column=0,padx=2,pady=3)

        btn_delete=Button(button_frame,text="Delete",command=self.delete_data,font=("arial",13,"bold"),width=14,bg="deepskyblue",fg="white")
        btn_delete.grid(row=2,column=0,padx=2,pady=3)

        btn_clear=Button(button_frame,text="Clear",command=self.reset_data,font=("arial",13,"bold"),width=14,bg="deepskyblue",fg="white")
        btn_clear.grid(row=3,column=0,padx=2,pady=3)


        #lower frame
        lower_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text='Employee Information Table',font=('times new roman',13,'bold'),fg='red',bg='white')
        lower_frame.place(x=10,y=245,width=1495,height=340)

        #Search frame
        self.var_com_search=StringVar()
        search_frame=LabelFrame(lower_frame,bd=2,relief=RIDGE,text='Search Employee Information',font=('times new roman',12,'bold'),fg='navy',bg='white')
        search_frame.place(x=5,y=5,width=1465,height=50)

        search_by=Label(search_frame,text="Search By:",font=("arial",10,"bold"),bg="orange",fg="white")
        search_by.grid(row=0,column=0,padx=5,sticky=W)

        #search
        self.var_com_search=StringVar()
        com_txt_search=ttk.Combobox(search_frame,textvariable=self.var_com_search,state="readonly",font=("arial",10,"bold"),width=18)
        com_txt_search['value']=("Select Option","Phone","id_proof")
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,padx=5,sticky=W) 

        self.var_search=StringVar()
        txt_search=ttk.Entry(search_frame,textvariable=self.var_search,font=("arial",10,"bold"),width=24)
        txt_search.grid(row=0,column=2,padx=5,sticky=W) 


        btn__search=Button(search_frame,text="Search",command=self.search_data,font=("arial",10,"bold"),width=14,bg="orange",fg="white")
        btn__search.grid(row=0,column=3,padx=5)


        btn_ShowAll=Button(search_frame,text="Show All",command=self.fetch_data,font=("arial",10,"bold"),width=14,bg="orange",fg="white")
        btn_ShowAll.grid(row=0,column=4,padx=5)

        # ************************* Employee Table ***************************
        # Table Frame
        table_frame=Frame(lower_frame,bd=3,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470,height=248)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee_table=ttk.Treeview(table_frame,column=("dep","name","degi","email","address","married","dob","doj","idproofcomb","idproof","gender","phone","country","salary",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading("dep",text="Department")
        self.employee_table.heading("name",text="Name")
        self.employee_table.heading("degi",text="Designation")
        self.employee_table.heading("email",text="Email")
        self.employee_table.heading("address",text="Address")
        self.employee_table.heading("married",text="Married")
        self.employee_table.heading("dob",text="DOB")
        self.employee_table.heading("doj",text="DOJ")
        self.employee_table.heading("idproofcomb",text="ID Type")
        self.employee_table.heading("idproof",text="ID Proof")
        self.employee_table.heading("gender",text="Gender")
        self.employee_table.heading("phone",text="Phone")
        self.employee_table.heading("country",text="Country")
        self.employee_table.heading("salary",text="Salary")

        self.employee_table['show']='headings'

        self.employee_table.column("dep",width=100)
        self.employee_table.column("name",width=100)
        self.employee_table.column("degi",width=100)
        self.employee_table.column("email",width=100)
        self.employee_table.column("address",width=100)
        self.employee_table.column("married",width=100)
        self.employee_table.column("dob",width=100)
        self.employee_table.column("doj",width=100)
        self.employee_table.column("idproofcomb",width=100)
        self.employee_table.column("idproof",width=100)
        self.employee_table.column("gender",width=100)
        self.employee_table.column("phone",width=100)
        self.employee_table.column("country",width=100)
        self.employee_table.column("salary",width=100)

        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()


    # ***************Function Declarations*******************

    def add_data(self):
        if self.var_dep.get()=="" or self.var_email.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='sonal@19',database='employeeform')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(self.var_dep.get(),self.var_name.get(),self.var_designation.get(),self.var_email.get(),self.var_address.get(),self.var_married.get(),self.var_dob.get(),self.var_doj.get(),self.var_idproofcomb.get(),self.var_idproof.get(),self.var_gender.get(),self.var_phone.get(),self.var_country.get(),self.var_salary.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('success','Employee has been added!',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)

    
    #Fetch Table
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='sonal@19',database='employeeform')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from employee')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("",END,values=i)
                conn.commit()
            conn.close()


    # Get Cursor
    def get_cursor(self,event=""):
        cursor_row=self.employee_table.focus()
        content=self.employee_table.item(cursor_row)
        data=content['values']

        self.var_dep.set(data[0])
        self.var_name.set(data[1])
        self.var_designation.set(data[2])
        self.var_email.set(data[3])
        self.var_address.set(data[4])
        self.var_married.set(data[5])
        self.var_dob.set(data[6])
        self.var_doj.set(data[7])
        self.var_idproofcomb.set(data[8])
        self.var_idproof.set(data[9])
        self.var_gender.set(data[10])
        self.var_phone.set(data[11])
        self.var_country.set(data[12])
        self.var_salary.set(data[13])

    
    #Update
    def update_data(self):
        if self.var_dep.get()=="" or self.var_email.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                update=messagebox.askyesno('Update','Are you sure update this employee data')
                if update>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='sonal@19',database='employeeform')
                    my_cursor=conn.cursor()
                    my_cursor.execute('Update employee set Department=%s,Name=%s,Designation=%s,Email=%s,Address=%s,Married=%s,DOB=%s,DOJ=%s,ID_Proof_Type=%s,Gender=%s,Phone=%s,Country=%s,Salary=%s where ID_Proof=%s',(self.var_dep.get(),self.var_name.get(),self.var_designation.get(),self.var_email.get(),self.var_address.get(),self.var_married.get(),self.var_dob.get(),self.var_doj.get(),self.var_idproofcomb.get(),self.var_gender.get(),self.var_phone.get(),self.var_country.get(),self.var_salary.get(),self.var_idproof.get()))

                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)  
    
    
    #Delete
    def delete_data(self):
        if self.var_idproof.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                Delete=messagebox.askyesno('Delete','Are you sure update this employee data')
                if Delete>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='sonal@19',database='employeeform')
                    my_cursor=conn.cursor()
                    sql='delete from employee where id_proof=%s'
                    value=(self.var_idproof.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showninfo('Delete','Employee Successfully DEletedted',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)  

    
    #Reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_name.set(" ")
        self.var_designation.set(" ")
        self.var_email.set(" ")
        self.var_address.set("")
        self.var_married.set("Select Option")
        self.var_dob.set(" ")
        self.var_doj.set(" ")
        self.var_idproofcomb.set("Select ID Proof")
        self.var_idproof.set(" ")
        self.var_gender.set("Select Gender")
        self.var_phone.set(" ")
        self.var_country.set(" ")
        self.var_salary.set(" ")


    #Search
    def search_data(self):
        if self.var_com_search.get()=='' or self.var_search.get()=='':
            messagebox.showerror('Error','Please Select Option')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='sonal@19',database='employeeform')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from employee where' +str(self.var_com_search.get())+" LIKE '% "+ str(self.var_search.get()+"%' "))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in rows:
                        self.employee_table.insert(" ",END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
               messagebox.showerror('Error',f'Due To:{str(es)}',parent=self.root)  


                    
if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()
