from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from PIL import Image, ImageTk #pip install pillow


class supplierClass:
    def __init__(self, root, back_command=None):
        self.root = root
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        x = (screen_w // 2) - (1350 // 2)
        y = (screen_h // 2) - (700 // 2)
        self.root.geometry(f"1350x700+{x}+{y}")
        self.root.after(100, self.root.deiconify)
        self.root.title("Dobavljac")
        self.root.config(bg="white")
        self.root.resizable(False, False)
        self.root.focus_force()
        #============================================================
        # All_variables=============================================
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        self.var_dz = StringVar()
        self.var_di = StringVar()
        self.var_name= StringVar()
        self.var_lname = StringVar()
        self.var_num = StringVar()
        self.var_user = StringVar()
        self.var_pass = StringVar()
        self.var_email = StringVar()
        self.var_adress = StringVar()
        self.var_pay = StringVar()
        self.var_usertype = StringVar()
        self.var_emp_id = StringVar()

        btn_nazad = Button(self.root, text="Nazad",command=back_command, font=("Segoe UI", 10), cursor="hand2", bd=2, relief=GROOVE)
        btn_nazad.place(x=350, y=60, width=100, height=50, anchor=NE)

        #Pretraga======================================================================================
        SearchFrame = LabelFrame(self.root, text="Pretraga zaposlenih", bg="white", font=("Segoe UI", 20, ""),  bd=2, relief=RIDGE)
        SearchFrame.place(x=400, y=20, width=600, height=100)

        #Opcije=========================================================================================
        cmb_search = ttk.Combobox(SearchFrame, textvariable = self.var_searchby ,values = ("Odaberite","Zaposleni ID","Ime", "Prezime", "Email", "Kontakt"), justify=CENTER, font=("Segoe UI",12))
        cmb_search.place(x=10,y=5, width=180)
        cmb_search.current(0)

        txt_search = Entry(SearchFrame,textvariable = self.var_searchtxt, font=("Segoe UI", 12), bg="lightyellow")
        txt_search.place(x=230,y=5)

        btn_search = Button(SearchFrame, text="Pretraga",command = self.search, font=("Segoie UI", 10), cursor="hand2", bd=2, relief=GROOVE)
        btn_search.place(x=450, y=3, width=100 , height=30)



        title=Label(self.root,text="Podaci zaposlenih",bg = "#0f4d7d", fg = "white", font=("Segoe UI", 20, ""))
        title.place(x=170, y=150, height=50, width=1000)

        #Sadrzaj======================================================================================================
        #Labeli
        lbl_empid = Label(self.root,text="Zaposleni ID#",bg = "white", font=("Segoe UI", 12, ""))
        lbl_empid.place(x=200, y=230)

        lbl_dz = Label(self.root, text="Datum zap. rad. odn", bg="white", font=("Segoe UI", 12, ""))
        lbl_dz.place(x=520, y=230)

        lbl_di = Label(self.root, text="Datum ist. rad. odn.", bg="white", font=("Segoe UI", 12, ""))
        lbl_di.place(x=900, y=230)

        lbl_name = Label(self.root, text="Ime", bg="white", font=("Segoe UI", 12, ""))
        lbl_name.place(x=200, y=290)

        lbl_lname = Label(self.root, text="Prezime", bg="white", font=("Segoe UI", 12, ""))
        lbl_lname.place(x=520, y=290)

        lbl_num = Label(self.root, text="Kontakt broj", bg="white", font=("Segoe UI", 12, ""))
        lbl_num.place(x=900, y=290)

        lbl_user = Label(self.root, text="Kor. Ime", bg="white", font=("Segoe UI", 12, ""))
        lbl_user.place(x=200, y=350)

        lbl_pass = Label(self.root, text="Šifra", bg="white", font=("Segoe UI", 12, ""))
        lbl_pass.place(x=520, y=350)

        lbl_email = Label(self.root, text="Email", bg="white", font=("Segoe UI", 12, ""))
        lbl_email.place(x=900, y=350)

        lbl_adress = Label(self.root, text="Adresa", bg="white", font=("Segoe UI", 12, ""))
        lbl_adress.place(x=200, y=410)

        lbl_pay = Label(self.root, text="Plata", bg="white", font=("Segoe UI", 12, ""))
        lbl_pay.place(x=520, y=410)

        lbl_usertype = Label(self.root, text="Tip naloga", bg="white", font=("Segoe UI", 12, ""))
        lbl_usertype.place(x=900, y=410)

        #Kockepored

        txt_emp_id=Entry(self.root, textvariable=self.var_emp_id, font=("Segoe UI", 12), bg="white", state="readonly")
        txt_emp_id.place(x=320, y=230, width=100)

        txt_dz = Entry(self.root, textvariable=self.var_dz, font=("Segoe UI", 12), bg="white")
        txt_dz.place(x=670, y=230, width=100)

        txt_di = Entry(self.root, textvariable=self.var_di, font=("Segoe UI", 12), bg="white")
        txt_di.place(x=1050, y=230, width=100)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("Segoe UI", 12), bg="white")
        txt_name.place(x=320, y=290, width=100)

        txt_lname = Entry(self.root, textvariable=self.var_lname, font=("Segoe UI", 12), bg="white")
        txt_lname.place(x=670, y=290, width=100)

        txt_num = Entry(self.root, textvariable=self.var_num, font=("Segoe UI", 12), bg="white")
        txt_num.place(x=1050, y=290, width=100)

        txt_user = Entry(self.root, textvariable=self.var_user, font=("Segoe UI", 12), bg="white")
        txt_user.place(x=320, y=350, width=100)

        txt_pass = Entry(self.root, textvariable=self.var_pass, font=("Segoe UI", 12), bg="white")
        txt_pass.place(x=670, y=350, width=100)

        txt_email = Entry(self.root, textvariable=self.var_email, font=("Segoe UI", 12), bg="white")
        txt_email.place(x=1050, y=350, width=100)

        txt_adress = Entry(self.root, textvariable=self.var_adress, font=("Segoe UI", 12), bg="white")
        txt_adress.place(x=320, y=410, width=100)

        txt_pay = Entry(self.root, textvariable=self.var_pay, font=("Segoe UI", 12), bg="white")
        txt_pay.place(x=670, y=410, width=100)

        cmb_usertype = ttk.Combobox(self.root, textvariable=self.var_usertype, state="readonly", values =  ("Odaberite","Admin", "User"), font=("Segoe UI", 12))
        cmb_usertype.current(0)
        cmb_usertype.place(x=1050, y=410, width=100)

        btn_save = Button(self.root,text = "Sačuvati",command=self.add, font=("Segoe UI", 10, ""), bg="white",relief=GROOVE)
        btn_save.place(x=300, y=450)
        btn_update = Button(self.root, text = "Ažurirati",command=self.update, font=("Segoe UI", 10, ""), bg="white",relief=GROOVE)
        btn_update.place(x=500, y=450)
        btn_delete = Button(self.root, text= "Izbrisati",command=self.delete, font=("Segoe UI", 10, ""), bg="white",relief=GROOVE)
        btn_delete.place(x=700, y=450)
        btn_clear = Button(self.root, text = "Očistiti",command=self.clear, font = ("Segoe UI", 10, ""), bg="white",relief=GROOVE)
        btn_clear.place(x=900, y=450)

        #Tabela podataka zaposlenih ==============================================================================
        emp_frame = Frame(self.root, bd=3, bg="white")
        emp_frame.place(x=0, rely=1, relwidth=1, height=200, anchor="sw")

        scrolly = Scrollbar(emp_frame,orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.EmployeeTable = ttk.Treeview(emp_frame,columns=("emp_id","dz", "di", "name", "lname", "contact", "user", "pass", "email", "adress", "pay", "usertype"), show="headings", yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)


        self.EmployeeTable.heading("emp_id", text="Zaposleni ID#")
        self.EmployeeTable.column("emp_id", width=80)

        self.EmployeeTable.heading("dz", text="Dat. Zap.")
        self.EmployeeTable.column("dz", width=80)

        self.EmployeeTable.heading("di", text="Dat. Ist.")
        self.EmployeeTable.column("di", width=80)

        self.EmployeeTable.heading("name", text="Ime")
        self.EmployeeTable.column("name", width=80)

        self.EmployeeTable.heading("lname", text="Prezime")
        self.EmployeeTable.column("lname", width=80)

        self.EmployeeTable.heading("contact", text="Kontakt")
        self.EmployeeTable.column("contact", width=90)

        self.EmployeeTable.heading("user", text="Kor. Ime")
        self.EmployeeTable.column("user", width=80)

        self.EmployeeTable.heading("pass", text="Šifra")
        self.EmployeeTable.column("pass", width=80)

        self.EmployeeTable.heading("email", text="Email")
        self.EmployeeTable.column("email", width=120)

        self.EmployeeTable.heading("adress", text="Adresa")
        self.EmployeeTable.column("adress", width=100)

        self.EmployeeTable.heading("pay", text="Plata")
        self.EmployeeTable.column("pay", width=70)

        self.EmployeeTable.heading("usertype", text="Vrsta naloga")
        self.EmployeeTable.column("usertype", width=90)

        self.EmployeeTable.pack(fill=BOTH, expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>", self.get_data)

        self.create_table()
        self.show()

    def create_table(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS employee (
            eid INTEGER PRIMARY KEY,
            dz TEXT,
            di TEXT,
            name TEXT,
            lname TEXT,
            contact TEXT,
            user TEXT,
            pass TEXT,
            email TEXT,
            adress TEXT,
            pay REAL,
            usertype TEXT
        )""")
        # cur.execute("ALTER TABLE employee RENAME COLUMN pass TO passwd")
        con.commit()
        con.close()

    def add(self):
        con = sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Greška","ID zaposlenog je već dodeljen nekom zaposlenom, molim izmenite ili dodelite drugi broj.", parent=self.root)
                else:
                    cur.execute("""INSERT INTO employee 
                        (dz, di, name, lname, contact, user, pass, email, adress, pay, usertype) 
                        VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
                                (
                                    self.var_dz.get(),
                                    self.var_di.get(),
                                    self.var_name.get(),
                                    self.var_lname.get(),
                                    self.var_num.get(),
                                    self.var_user.get(),
                                    self.var_pass.get(),
                                    self.var_email.get(),
                                    self.var_adress.get(),
                                    self.var_pay.get(),
                                    self.var_usertype.get()
                                )
                                )
                    con.commit()
                    messagebox.showinfo("Uspeh", "Zaposleni uspešno dodat!", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Greška", f"Greška iz razloga : {str(ex)}", parent=self.root)
        finally:
            con.close()


    def show(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            cur.execute("Select * from employee")
            rows=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('', END, values=row)

        except Exception as ex:
             messagebox.showerror("Greška",f"Greška iz razloga : {str(ex)}", parent=self.root)
        finally:
            con.close()

#olaksavanje-update-dugmeta
    def get_data(self,ev):
        f=self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(f))
        row=content['values']
        print(row)
        self.var_emp_id.set(row[0])
        self.var_dz.set(row[1])
        self.var_di.set(row[2])
        self.var_name.set(row[3])
        self.var_lname.set(row[4])
        self.var_num.set(row[5])
        self.var_user.set(row[6])
        self.var_pass.set(row[7])
        self.var_email.set(row[8])
        self.var_adress.set(row[9])
        self.var_pay.set(row[10])
        self.var_usertype.set(row[11])

    def update(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
                cur.execute("Select * from employee where eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Greška",
                                         "Greška u ID zaposlenog.", parent=self.root)
                else:
                    cur.execute("""UPDATE employee SET 
                    dz=?, di=?, name=?, lname=?, contact=?, user=?, pass=?, email=?, adress=?, pay=?, usertype=?
                    WHERE eid=?""", (
                                self.var_dz.get(),
                                self.var_di.get(),
                                self.var_name.get(),
                                self.var_lname.get(),
                                self.var_num.get(),
                                self.var_user.get(),
                                self.var_pass.get(),
                                self.var_email.get(),
                                self.var_adress.get(),
                                self.var_pay.get(),
                                self.var_usertype.get(),
                                self.var_emp_id.get()
                            )
                )
                    con.commit()

                    messagebox.showinfo("Uspeh", "Podatak uspešno ažuriran!", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Greška", f"Greška iz razloga : {str(ex)}", parent=self.root)
        finally:
            con.close()

    def delete(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
                cur.execute("Select * from employee where eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Greška",
                                         "Greška u ID zaposlenog.", parent=self.root)
                else:
                    op=messagebox.askyesno("Potvrda","Da li stvarno želite da obrišete unos?", parent=self.root)
                    if op == True:
                        cur.execute("DELETE FROM employee WHERE eid=?", (self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Brisanje", "Uspešno izbrisana stavka.", parent=self.root)
                        self.clear()
                        self.show()
        except Exception as ex:
            messagebox.showerror("Greška", f"Greška iz razloga : {str(ex)}", parent=self.root)
        finally:
            con.close()

    def clear(self):
        self.var_emp_id.set("")
        self.var_dz.set("")
        self.var_di.set("")
        self.var_name.set("")
        self.var_lname.set("")
        self.var_num.set("")
        self.var_user.set("")
        self.var_pass.set("")
        self.var_email.set("")
        self.var_adress.set("")
        self.var_pay.set("")
        self.var_usertype.set("Odaberite")

    def search(self):

        search_map = {
            "Zaposleni ID": "eid",
            "Ime": "name",
            "Prezime": "lname",
            "Email": "email",
            "Kontakt": "contact",
        }

        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            if self.var_searchby.get() == "Odaberite":
                messagebox.showerror("Greška", "Izaberite opciju za pretragu.", parent=self.root)
            elif self.var_searchtxt.get() == "":
                messagebox.showerror("Greška", "Polje za pretragu ne sme biti prazno.", parent=self.root)
            else:
                column = search_map.get(self.var_searchby.get())
                cur.execute(f"SELECT * FROM employee WHERE {column} LIKE ?", (f"%{self.var_searchtxt.get()}%",))
                rows=cur.fetchall()
                self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                if len(rows) != 0:
                    for row in rows:
                        self.EmployeeTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Greška", "Nije pronađen zapis.", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Greška", f"Greška iz razloga : {str(ex)}", parent=self.root)
        finally:
            con.close()




if __name__=="__main__":
    root=Tk()
    obj=(supplierClass(root))
    root.mainloop()