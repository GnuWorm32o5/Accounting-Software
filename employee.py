from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk, messagebox
import sqlite3

class employeeClass:
    def __init__(self,root):
        self.root = root
        self.create_db()
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        x = (screen_w // 2) - (1350 // 2)
        y = (screen_h // 2) - (700 // 2)
        self.root.geometry(f"1350x700+{x}+{y}")
        self.root.after(100, self.root.deiconify)
        self.root.geometry(f"1350x900+{x}+{y}")
        self.root.title("Računovodstveni softver")
        self.root.config(bg="white")  # dark navy blue #1e2a3a
        self.root.resizable(False, False)
        # self.root.state("zoomed")
        self.root.bind("<Escape>", lambda e: self.root.destroy())  # gasi se na escape


        #All Variables =========================================================================================
        self.var_search_by=StringVar()
        self.var_search_txt=StringVar()

        self.var_emp_id=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_email=StringVar()
        self.var_password=StringVar()
        self.var_utype=StringVar()
        self.var_adress=StringVar()
        self.var_salary=StringVar()


        #========Search Frame================================================================================================
        SearchFrame=LabelFrame(self.root,text="Pretraga Zaposlenog", bg="white", font=("Segoe UI", 12))
        SearchFrame.place(x=250,y=20,width=880,height=80)

        #======Options================================================================================================
        cmb_search=ttk.Combobox(SearchFrame, textvariable=self.var_search_by, values=("Odabrati" , "Ime", "Kontakt", "Email"), state="readonly", justify="center", font=("Segoe UI", 15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search = Entry(SearchFrame, textvariable=self.var_search_txt, font=("Segoe UI", 15), bg="white").place(x=300, y=10, width=300)
        btn_search = Button(SearchFrame,command=self.search, text="Pretraga", font=("Segoe UI", 15), bg="white")
        btn_search.place(x=650, y=8, width=200, height=30)

        #=========Title===================================================================================================

        title = Label(self.root,text="Podaci zaposlenih", font=("Segoe UI", 15), bg="lightblue")
        title.place(x =200, y=120, width=1000)


        #====Content======================================================================================================================

        lbl_empid=Label(self.root,text="ID Zaposlenog",font=("Segoe UI", 12), bg="white")
        lbl_empid.place(x =200, y=200)

        lbl_gender=Label(self.root,text="Pol",font=("Segoe UI", 12), bg="white")
        lbl_gender.place(x =600, y=200)

        lbl_contact=Label(self.root,text="Kontakt",font=("Segoe UI", 12), bg="white")
        lbl_contact.place(x =1000, y=200)

        lbl_name=Label(self.root,text="Ime",font=("Segoe UI", 12), bg="white")
        lbl_name.place(x =200, y=300)

        lbl_doj=Label(self.root,text="Datum z.",font=("Segoe UI", 12), bg="white")
        lbl_doj.place(x =600, y=300)

        lbl_dol=Label(self.root,text="Datum i.",font=("Segoe UI", 12), bg="white")
        lbl_dol.place(x =1000, y=300)

        lbl_email=Label(self.root,text="Email",font=("Segoe UI", 12), bg="white")
        lbl_email.place(x =200, y=400)

        lbl_password=Label(self.root,text="Šifra",font=("Segoe UI", 12), bg="white")
        lbl_password.place(x =600, y=400)

        lbl_utype=Label(self.root,text="Nalog",font=("Segoe UI", 12), bg="white")
        lbl_utype.place(x =1000, y=400)

        lbl_salary = Label(self.root, text="Adresa", font=("Segoe UI", 12), bg="white")
        lbl_salary.place(x=200, y=500)

        lbl_adress=Label(self.root, text="Plata",font=("Segoe UI", 12), bg="white")
        lbl_adress.place(x =600, y=500)




        #================Fields===========================================================================================

        txt_empid=Entry(self.root, textvariable=self.var_emp_id, font=("Segoe UI", 12), bg="white")
        txt_empid.place(x=350, y=200)

        txt_gender = Entry(self.root, textvariable=self.var_gender, font=("Segoe UI", 12), bg="white")
        txt_gender.place(x=700, y=200)

        txt_contact= Entry(self.root, textvariable=self.var_contact, font=("Segoe UI", 12), bg="white")
        txt_contact.place(x=1100, y=200)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("Segoe UI", 12), bg="white")
        txt_name.place(x=350, y=300)

        txt_dob = Entry(self.root, textvariable=self.var_dob, font=("Segoe UI", 12), bg="white")
        txt_dob.place(x=700, y=300)

        txt_doj = Entry(self.root, textvariable=self.var_doj, font=("Segoe UI", 12), bg="white")
        txt_doj.place(x=1100, y=300)

        txt_email = Entry(self.root, textvariable=self.var_email, font=("Segoe UI", 12), bg="white")
        txt_email.place(x=350, y=400)

        txt_password = Entry(self.root, textvariable=self.var_password, font=("Segoe UI", 12), bg="white")
        txt_password.place(x=700, y=400)

        txt_utype = ttk.Combobox(self.root, textvariable=self.var_utype,values=("Admin","Korisnik"), state="readonly", font=("Segoe UI", 12))
        txt_utype.place(x=1100, y=400)
        txt_utype.current(1)

        txt_adress = Entry(self.root, textvariable=self.var_adress, font=("Segoe UI", 12), bg="white")
        txt_adress.place(x=350, y=500)

        txt_salary = Entry(self.root, textvariable=self.var_salary, font=( "Segoe UI", 12), bg="white")
        txt_salary.place(x=700, y=500)

        #=========Buttons================================================================================================

        btn_save=Button(self.root,command=self.add, font=("Segoe UI", 12), bg="white", relief="groove", text="Sačuvati")
        btn_save.place(x=350, y=550)

        btn_update = Button(self.root, command=self.update, font=("Segoe UI", 12), bg="white", relief="groove", text="Ažurirati")
        btn_update.place(x=600, y=550)

        btn_delete = Button(self.root, command=self.delete, font=("Segoe UI", 12), bg="white", relief="groove", text="Obrisati")
        btn_delete.place(x=850, y=550)

        btn_clear = Button(self.root,command=self.clear, font=("Segoe UI", 12), bg="white", relief="groove", text="Očistiti polja")
        btn_clear.place(x=1100, y=550)

        #=========================================================================================================

        emp_frame = Frame(self.root, bd=3, relief="groove")
        emp_frame.pack(side=BOTTOM, fill=X)

        scrolly = Scrollbar(emp_frame, orient="vertical")
        scrollx = Scrollbar(emp_frame, orient="horizontal")



        self.EmployeeTable = ttk.Treeview(
            emp_frame,
            columns=("eid", "name", "email", "gender", "contact", "dob", "doj", "pass", "utype", "adress", "salary"),
            show="headings"
        )
        scrolly.config(command=self.EmployeeTable.yview)
        scrollx.config(command=self.EmployeeTable.xview)

        self.EmployeeTable.config(yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        self.EmployeeTable.heading("eid",text="ID Zaposlenog",anchor=CENTER)
        self.EmployeeTable.heading("name", text="Ime", anchor=CENTER)
        self.EmployeeTable.heading("email", text="Email", anchor=CENTER)
        self.EmployeeTable.heading("gender", text="Pol", anchor=CENTER)
        self.EmployeeTable.heading("contact", text="Kontakt", anchor=CENTER)
        self.EmployeeTable.heading("dob", text="Dat. Za.", anchor=CENTER)
        self.EmployeeTable.heading("doj", text="Dat. Ist.", anchor=CENTER)
        self.EmployeeTable.heading("pass", text="Šifra", anchor=CENTER)
        self.EmployeeTable.heading("utype", text="Tip", anchor=CENTER)
        self.EmployeeTable.heading("adress", text="Adresa", anchor=CENTER)
        self.EmployeeTable.heading("salary", text="Plata", anchor=CENTER)

        self.EmployeeTable.column("eid", width=15)
        self.EmployeeTable.column("name", width=100)
        self.EmployeeTable.column("email", width=100)
        self.EmployeeTable.column("gender", width=100)
        self.EmployeeTable.column("contact", width=100)
        self.EmployeeTable.column("dob", width=100)
        self.EmployeeTable.column("doj", width=100)
        self.EmployeeTable.column("pass", width=100)
        self.EmployeeTable.column("utype", width=100)
        self.EmployeeTable.column("adress", width=100)
        self.EmployeeTable.column("salary", width=100)


        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.pack(side=BOTTOM, fill=X)
        self.EmployeeTable.pack(fill=BOTH, expand=1)

        self.EmployeeTable.bind("<ButtonRelease-1>", self.get_data)


        self.show()
        #=================================================================================================

    def create_db(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS employee
                       (
                           eid
                           INTEGER
                           PRIMARY
                           KEY,
                           name
                           TEXT,
                           email
                           TEXT,
                           gender
                           TEXT,
                           contact
                           TEXT,
                           dob
                           TEXT,
                           doj
                           TEXT,
                           pass
                           TEXT,
                           utype
                           TEXT,
                           adress
                           TEXT,
                           salary
                           TEXT
                       )""")
        con.commit()
        con.close()

    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Greška", "ID Zaposlenog mora biti unet!", parent=self.root)
            else:
                cur.execute("Select  * from employee where eid=?", (self.var_emp_id.get(),))
                row=cur.fetchone()
                if row is not None:
                    messagebox.showerror("Greška", "Broj je prethodno dodeljen postojećem zaposlenom.", parent=self.root )
                else:
                    cur.execute("Insert into employee (eid, name, email, gender, contact, dob, doj, pass, utype, adress, salary) values(?,?,?,?,?,?,?,?,?,?,?)",(
                                        self.var_emp_id.get(),
                                        self.var_name.get(),
                                        self.var_email.get(),
                                        self.var_gender.get(),
                                        self.var_contact.get(),
                                        self.var_dob.get(),
                                        self.var_doj.get(),
                                        self.var_password.get(),
                                        self.var_utype.get(),
                                        self.var_adress.get(),
                                        self.var_salary.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Uspeh!", "Uspešno dodat zaposleni na spisak!", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Greška", f" Greška iz razloga: {str(ex)}")
        finally:
            con.close()

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("Select * from employee")
            rows=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Greška", f"Greška iz razloga: {str(ex)}", parent=self.root)

    def get_data(self, event):
        f=self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(f))
        row=content['values']
        print(row)

        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
        self.var_dob.set(row[5])
        self.var_doj.set(row[6])
        self.var_password.set(row[7])
        self.var_utype.set(row[8])
        self.var_adress.set(row[9])
        self.var_salary.set(str(row[10]))

    def update(self):
        if self.var_emp_id.get() == "":
            messagebox.showerror("Greška", "ID Zaposlenog mora biti unet!", parent=self.root)
            return

        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM employee WHERE eid=?", (self.var_emp_id.get(),))
            row = cur.fetchone()
            if row is None:
                messagebox.showerror("Greška", "Nevažeći ID zaposlenog.", parent=self.root)
            else:
                cur.execute(
                    """UPDATE employee
                       SET name=?,
                           email=?,
                           gender=?,
                           contact=?,
                           dob=?,
                           doj=?,
                           pass=?,
                           utype=?,
                           adress=?,
                           salary=?
                       WHERE eid = ?""",
                    (
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_contact.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_password.get(),
                        self.var_utype.get(),
                        self.var_adress.get(),
                        self.var_salary.get(),
                        self.var_emp_id.get()  # eid goes LAST — it's the WHERE clause
                    )
                )
                con.commit()
                messagebox.showinfo("Uspeh!", "Uspešno ažuriran zaposleni sa spiska!", parent=self.root)
                self.show()
        except Exception as ex:
            messagebox.showerror("Greška", f"Greška iz razloga: {str(ex)}", parent=self.root)
        finally:
            con.close()


    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Greška", "ID zaposlenog mora biti unet!", parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?", (self.var_emp_id.get(),))
                row=cur.fetchone()
                if row is None:
                    messagebox.showerror("Greška", "Nevažeći ID zaposlenog.", parent=self.root)
                else:
                    op=messagebox.askyesno("Potvrda", "Da li stvarno  želite da obrišete zaposlenog?", parent=self.root)
                    if op==True:
                        cur.execute("delete from employee where eid=?", (self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Brisanje","Podaci uspešno obrisani.")
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Greška", f"Greška iz razloga: {str(ex)}", parent=self.root)
        finally:
            con.close()


    def clear(self):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_password.set("")
        self.var_utype.set("Korisnik")
        self.var_adress.set("")
        self.var_salary.set("")
        self.var_search_txt.set("")
        self.var_search_by.set("Odabrati")


    ALLOWED_COLUMNS = {"name", "email", "contact", "gender", "utype", "eid"}

    COLUMN_MAP = {
        "Ime": "name",
        "Email": "email",
        "Kontakt": "contact"
    }

    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_search_by.get() == "Odabrati":
                messagebox.showerror("Greška", "Morate odabrati opciju za pretragu.", parent=self.root)
            elif self.var_search_txt.get() == "":
                messagebox.showerror("Greška", "Polje za pretragu ne može biti prazno.", parent=self.root)
            elif self.var_search_by.get() not in self.COLUMN_MAP:
                messagebox.showerror("Greška", "Nevažeća kolona pretrage.", parent=self.root)
            else:
                col = self.COLUMN_MAP[self.var_search_by.get()]
                search_val = f"%{self.var_search_txt.get()}%"
                cur.execute(f"SELECT * FROM employee WHERE {col} LIKE ?", (search_val,))
                rows = cur.fetchall()
                if rows:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Greška", "Nije pronađen.", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Greška", f"Greška iz razloga: {str(ex)}", parent=self.root)
        finally:
            con.close()






if __name__=="__main__":
    root=Tk()
    obj=employeeClass(root)
    root.mainloop()