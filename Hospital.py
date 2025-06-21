from tkinter import *
from tkinter import ttk
import random
import time
import datetime
import mysql.connector
from tkinter import messagebox



class Hospital:
    def  __init__(self,root):
        self.root=root
        self.root.config(background="#fc0384")
        self.root.title("Amma Hospital Records")
        self.root.geometry("1540x800+0+0")

        self.Tabletnames=StringVar()
        self.Referanceno=StringVar()
        self.Dose=StringVar()
        self.Nooftablets=StringVar()
        self.Bloodpressure=StringVar()
        self.Milligrams=StringVar()
        self.Pharmacycompany=StringVar()






        label=Label(self.root,bd=20,
            relief=RIDGE,
            text="HOSPITAL MANAGEMENT SYSTEM",
            fg="red",bg="white",
            font=("times nnew roma",50,"bold"))
        label.pack(side=TOP,fill=X)
#===============DATA FRAMES==========================================
        DataFrame=Frame(self.root,bd=20,
                relief=RIDGE,
                bg="#fc0384")
        DataFrame.place(x=0,y=120,width=1530,height=400)
        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,
                                font=("times new  roman",12,"bold"),
                                text="patient info")

        DataFrameLeft.place(x=0,y=4,width=990,height=350)
        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,
                                font=("times new  roman",12,"bold"),
                                text="prescriptio")

        DataFrameRight.place(x=985,y=5,width=350,height=350)
        #====================BUTTON FRAMES====================================
        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=520,width=1370,height=70)
        #====================DETAILS FRAMES====================================
        DetailsFrame=Frame(bd=20,relief=RIDGE)
        DetailsFrame.place(x=0,y=590,width=1370,height=190)
        #====================LEFT DATAFRAME====================================
        lblTablletName=Label(DataFrameLeft,text="Tablet Names",font=("times new  roman",12,"bold"),padx=2,pady=6)
        lblTablletName.grid(row=0,column=0,sticky=W)
        comNametablet=ttk.Combobox(DataFrameLeft,textvariable=self.Tabletnames,font=("times new  roman",12,"bold"),width=33)
        comNametablet["values"]=("dolo365","nice","corona","adderall")
        comNametablet.grid(row=0,column=1)
        #==================2===================================================
        lblref=Label(DataFrameLeft,font=("arial",12,"bold"),text="Referannce No",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        textref=Entry(DataFrameLeft,textvariable=self.Referanceno,font=("arial",13,"bold"),width=35)
        textref.grid(row=1,column=1)
        #================3=====================================================
        lbldose=Label(DataFrameLeft,font=("arial",12,"bold"),text="Dose",padx=2)
        lbldose.grid(row=2,column=0,sticky=W)
        textdose=Entry(DataFrameLeft,textvariable=self.Dose,font=("arial",13,"bold"),width=35)
        textdose.grid(row=2,column=1)

        lblNoOfTablets= Label(DataFrameLeft,font=("arial",12,"bold"),text="No Of Tablets",padx=2)
        lblNoOfTablets.grid(row=3,column=0,sticky=W)
        textNoOfTablets=Entry(DataFrameLeft,textvariable=self.Nooftablets,font=("arial",13,"bold"),width=35)
        textNoOfTablets.grid(row=3,column=1)

        lblBP= Label(DataFrameLeft,font=("arial",12,"bold"),text="Blood Pressure",padx=2)
        lblBP.grid(row=0,column=2,sticky=W)
        textBP=Entry(DataFrameLeft,textvariable=self.Bloodpressure,font=("arial",13,"bold"),width=35)
        textBP.grid(row=0,column=3)

        lblMG= Label(DataFrameLeft,font=("arial",12,"bold"),text="Milli Grams",padx=2)
        lblMG.grid(row=1,column=2,sticky=W)
        textMG=Entry(DataFrameLeft,textvariable=self.Milligrams,font=("arial",13,"bold"),width=35)
        textMG.grid(row=1,column=3)

        lblPC= Label(DataFrameLeft,font=("arial",12,"bold"),text="Pharmacy Company",padx=2)
        lblPC.grid(row=2,column=2,sticky=W)
        textPC=Entry(DataFrameLeft,textvariable=self.Pharmacycompany,font=("arial",13,"bold"),width=35)
        textPC.grid(row=2,column=3)
        #===============RIGHT TABEL====================================

        self.txtPrescription=Text(DataFrameRight,font=("free hand",12,"bold"),width=45,height=16,pady=6,padx=2)
        self.txtPrescription.grid(row=0,column=0)
        #===============BUTTON=========================================

        btnPrescription=Button(Buttonframe,command=self.iprescription,state='normal',text="Prescription",fg="white",bg="green",font=("Arial",12,"bold"),
                               width=23,height=1,padx=2,pady=6)
        btnPrescription.grid(row=0,column=0)


        btnUpdate=Button(Buttonframe,command=self.update_data,text="update",bg="green",fg="white",font=("arial",12,"bold"),
                               width=23,height=1,padx=2,pady=6)
        btnUpdate.grid(row=0,column=1)


        btnDelete=Button(Buttonframe,command=self.idelete,text="Delete",bg="green",foreground="white",font=("arial",12,"bold"),
                               width=23,height=1,padx=2,pady=6)
        btnDelete.grid(row=0,column=2)


        btnExit=Button(Buttonframe,text="Exit",bg="green",fg="white",font=("arial",12,"bold"),
                               width=23,height=1,padx=2,pady=6)
        btnExit.grid(row=0,column=3)

        btnPrescriptionDate=Button(Buttonframe,text="PrescriptionDate",bg="green",fg="white",font=("arial",12,"bold"),
                               width=23,height=1,padx=2,pady=6,command=self.iPrescriptionData)
        btnPrescriptionDate.grid(row=0,column=4)

        btnClear=Button(Buttonframe,command=self.clear,text="Clear",bg="green",fg="white",font=("arial",12,"bold"),
                               width=23,height=1,padx=2,pady=6)
        btnClear.grid(row=0,column=5)
#=========================TABLE=======================================
#=========================SCROLBAR====================================
        scroll_x=ttk.Scrollbar(DetailsFrame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(DetailsFrame,orient=VERTICAL)

        self.hospital_table=ttk.Treeview(
            DetailsFrame,
            columns=("tabletnames","referanceno","dose","nooftablets",
                      "bloodpressure","milligrams","pharmacycompany"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        self.hospital_table.heading("tabletnames",text="Tablet Names")
        self.hospital_table.heading("referanceno",text="Referance No")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No Of Tablets")
        self.hospital_table.heading("bloodpressure",text="Blood Pressure")
        self.hospital_table.heading("milligrams",text="Milli Grams")
        self.hospital_table.heading("pharmacycompany",text="Pharmacy Company")

        self.hospital_table["show"]="headings"
        self.hospital_table.pack(fill=BOTH,expand=1)

        self.hospital_table.column("tabletnames",width=100)
        self.hospital_table.column("referanceno",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("bloodpressure",width=100)
        self.hospital_table.column("milligrams",width=100)
        self.hospital_table.column("pharmacycompany",width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    
#===============================functions===================
# ======================Function to Insert Data ============================
    def iPrescriptionData(self):
        if self.Tabletnames.get() == "" or self.Referanceno.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            conn = mysql.connector.connect(
                host="127.0.0.1", username="SQL", password="sql@12345", database="mydatas")
            my_cursor = conn.cursor()
            my_cursor.execute("INSERT INTO hospital (Tabletnames, Referanceno, Dose, Nooftablets, Bloodpressure, Milligrams, Pharmacycompany) VALUES (%s,%s,%s,%s,%s,%s,%s)", (
                self.Tabletnames.get(),
                self.Referanceno.get(),
                self.Dose.get(),
                self.Nooftablets.get(),
                self.Bloodpressure.get(),
                self.Milligrams.get(),
                self.Pharmacycompany.get()
            ))
            conn.commit()
            conn.close()
            self.fetch_data() 
            self.clear()
            messagebox.showinfo("Success", "Record has been inserted")
    #=====================UPDATE  FUNCTION==============================================
    def update_data(self):

        conn = mysql.connector.connect(
                host="127.0.0.1", username="SQL", password="sql@12345", database="mydatas")
        my_cursor = conn.cursor()
        my_cursor.execute("update hospital  set  Tabletnames=%s,Dose=%s,Nooftablets=%s,Bloodpressure=%s,Milligrams=%s,Pharmacycompany=%s where Referanceno=%s",(
            self.Tabletnames.get(),
            self.Dose.get(),
            self.Nooftablets.get(),
            self.Bloodpressure.get(),
            self.Milligrams.get(),
            self.Pharmacycompany.get(),
            self.Referanceno.get(),
                 ))
        conn.commit()
        conn.close()
        self.fetch_data()  
        messagebox.showinfo("Success", "Record  updated")

    # ======================Function to Fetch Data from DB ============================
    def fetch_data(self):
        conn = mysql.connector.connect(
            host="127.0.0.1", username="SQL", password="sql@12345", database="mydatas")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM hospital")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("", END, values=i)
        conn.commit()
        conn.close()
    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()  
        content=self.hospital_table.item(cursor_row) 
        row=content["values"]
        self.Tabletnames.set(row[0])
        self.Referanceno.set(row[1])
        self.Dose.set(row[2])
        self.Nooftablets.set(row[3])
        self.Bloodpressure.set(row[4])
        self.Milligrams.set(row[5])
        self.Pharmacycompany.set(row[6])
#=======================PRESCRIPTION FUNCTION==================================================
    def iprescription(self):
        self.txtPrescription.insert(END,"Name Of Tablets:\t\t"+self.Tabletnames.get()+"\n")
        self.txtPrescription.insert(END,"Referance No:\t\t"+self.Referanceno.get()+"\n")
        self.txtPrescription.insert(END,"Dose:\t\t"+self.Dose.get()+"\n")
        self.txtPrescription.insert(END,"No Of Tablets:\t\t"+self.Nooftablets.get()+"\n")
        self.txtPrescription.insert(END,"Bloodpressure:\t\t"+self.Bloodpressure.get()+"\n")
        self.txtPrescription.insert(END,"Milligrams:\t\t"+self.Milligrams.get()+"\n")
        self.txtPrescription.insert(END,"Pharmacy Company:\t\t"+self.Pharmacycompany.get()+"\n")
 #=====================DELETE FUNCTION==========================================================       
    def idelete(self):
        conn = mysql.connector.connect(
            host="127.0.0.1", username="SQL", password="sql@12345", database="mydatas")
        my_cursor = conn.cursor()
        query="delete from hospital where Referanceno=%s"
        value = (self.Referanceno.get(),)  

        my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete","patient record deleted successfully")
 #============================CLEAR FUNCTION==============================
    def clear(self):
        self.Tabletnames.set("")
        self.Referanceno.set("")
        self.Dose.set("")
        self.Nooftablets.set("")
        self.Bloodpressure.set("")
        self.Milligrams.set("")
        self.Pharmacycompany.set("")
        self.txtPrescription.delete("1.0", END)

root=Tk()
object=Hospital(root)
root.mainloop()



