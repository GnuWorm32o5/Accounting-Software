from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from PIL import Image, ImageTk #pip install pillow


class supplierClass:
    def __init__(self, root, back_command=None):
        self.root = root
        self.create_table()
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        x = (screen_w // 2) - (1350 // 2)
        y = (screen_h // 2) - (700 // 2)
        self.root.geometry(f"1350x700+{x}+{y}")
        self.root.after(100, self.root.deiconify)
        self.root.title("Dobavljaci")
        self.root.config(bg="")
        self.root.resizable(False, False)
        self.root.focus_force()
        #============================================================


        # All_variables=============================================
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        self.var_sup_id = StringVar()
        self.var_name= StringVar()
        self.var_num = StringVar()
        self.var_adress = StringVar()
        self.var_pay = StringVar()
        self.var_email = StringVar()
        self.var_duguje = StringVar()
        self.var_potrazuje = StringVar()



        btn_nazad = Button(self.root, text="Nazad",command=back_command, font=("Segoe UI", 10), cursor="hand2", bd=2, relief=GROOVE)
        btn_nazad.place(x=350, y=60, width=100, height=50, anchor=NE)

        #Pretraga======================================================================================
        SearchFrame = LabelFrame(self.root, text="Pretraga dobavljača", bg="white", font=("Segoe UI", 20, ""),  bd=2, relief=RIDGE)
        SearchFrame.place(x=400, y=20, width=600, height=100)

        #Opcije=========================================================================================
        cmb_search = ttk.Combobox(SearchFrame, textvariable = self.var_searchby ,values = ("Ime"), state="readonly", justify=CENTER, font=("Segoe UI",12))
        cmb_search.place(x=10,y=5, width=180)
        cmb_search.current(0)

        txt_search = Entry(SearchFrame,textvariable = self.var_searchtxt, font=("Segoe UI", 12), bg="lightyellow")
        txt_search.place(x=230,y=5)

        btn_search = Button(SearchFrame, text="Pretraga",command = self.search, font=("Segoie UI", 10), cursor="hand2", bd=2, relief=GROOVE)
        btn_search.place(x=450, y=3, width=100 , height=30)

        # Naslov=====================================================================================================

        title=Label(self.root,text="Podaci dobavljača",bg = "#0f4d7d", fg = "white", font=("Segoe UI", 20, ""))
        title.place(x=170, y=150, height=50, width=1000)

        #Sadrzaj======================================================================================================
        #Labeli
        lbl_empid = Label(self.root,text="Dobavljač ID#",bg = "white", font=("Segoe UI", 12, ""))
        lbl_empid.place(x=100, y=230)

        lbl_empid = Label(self.root, text="Ime", bg="white", font=("Segoe UI", 12, ""))
        lbl_empid.place(x=420, y=230)

        lbl_num = Label(self.root, text="Kontakt broj", bg="white", font=("Segoe UI", 12, ""))
        lbl_num.place(x=700, y=230)

        lbl_adress = Label(self.root, text="Adresa", bg="white", font=("Segoe UI", 12, ""))
        lbl_adress.place(x=100, y=290)

        lbl_pay = Label(self.root, text="Stanje", bg="white", font=("Segoe UI", 12, ""))
        lbl_pay.place(x=420, y=290)

        lbl_email = Label(self.root, text="Email", bg="white", font=("Segoe UI", 12, ""))
        lbl_email.place(x=700, y=290)


        #Kockepored

        txt_emp_id=Entry(self.root, textvariable=self.var_sup_id, font=("Segoe UI", 12), bg="white")
        txt_emp_id.place(x=220, y=230, width=120)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("Segoe UI", 12), bg="white")
        txt_name.place(x=500, y=230, width=120)

        txt_num = Entry(self.root, textvariable=self.var_num, font=("Segoe UI", 12), bg="white")
        txt_num.place(x=850, y=230, width=120)

        txt_adress = Entry(self.root, textvariable=self.var_adress, font=("Segoe UI", 12), bg="white")
        txt_adress.place(x=220, y=290, width=120)

        txt_pay = Entry(self.root, textvariable=self.var_pay, font=("Segoe UI", 12), bg="white")
        txt_pay.place(x=500, y=290, width=120)

        txt_email = Entry(self.root, textvariable=self.var_email, font=("Segoe UI", 12), bg="white")
        txt_email.place(x=850, y=290, width=120)

        # Dugmad ===================================================================================================

        btn_save = Button(self.root,text = "Sačuvati",command=self.add, font=("Segoe UI", 10, ""), bg="white",relief=GROOVE)
        btn_save.place(x=300, y=350)
        btn_update = Button(self.root, text = "Ažurirati",command=self.update, font=("Segoe UI", 10, ""), bg="white",relief=GROOVE)
        btn_update.place(x=500, y=350)
        btn_delete = Button(self.root, text= "Izbrisati",command=self.delete, font=("Segoe UI", 10, ""), bg="white",relief=GROOVE)
        btn_delete.place(x=700, y=350)
        btn_clear = Button(self.root, text = "Očistiti",command=self.clear, font = ("Segoe UI", 10, ""), bg="white",relief=GROOVE)
        btn_clear.place(x=900, y=350)


        #Tabela podataka zaposlenih ==============================================================================
        emp_frame = Frame(self.root, bd=3, bg="white")
        emp_frame.place(x=0, rely=1, relwidth=1, height=300, anchor="sw")

        scrolly = Scrollbar(emp_frame,orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.SupplierTable = ttk.Treeview(emp_frame, columns=("emp_id", "name", "contact", "email", "adress", "pay", "duguje", "potrazuje"), show="headings", yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.SupplierTable.xview)
        scrolly.config(command=self.SupplierTable.yview)


        self.SupplierTable.heading("emp_id", text="Dobavljač ID#")
        self.SupplierTable.column("emp_id", width=80)

        self.SupplierTable.heading("name", text="Ime")
        self.SupplierTable.column("name", width=80)

        self.SupplierTable.heading("contact", text="Kontakt")
        self.SupplierTable.column("contact", width=90)

        self.SupplierTable.heading("email", text="Email")
        self.SupplierTable.column("email", width=120)

        self.SupplierTable.heading("adress", text="Adresa")
        self.SupplierTable.column("adress", width=100)

        self.SupplierTable.heading("pay", text="Iznos")
        self.SupplierTable.column("pay", width=70)

        self.SupplierTable.heading("duguje", text="Duguje")
        self.SupplierTable.column("duguje", width=70)

        self.SupplierTable.heading("potrazuje", text="Potrazuje")
        self.SupplierTable.column("potrazuje", width=70)

        self.SupplierTable.pack(fill=BOTH, expand=1)
        self.SupplierTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()

    #     Kreira tabelu za svaki slucaj ==========================================================================

    def create_table(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS supplier (
            eid INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            contact TEXT,
            email TEXT,
            adress TEXT,
            pay REAL,
            duguje REAL,
            potrazuje REAL
        )""")
        # cur.execute("ALTER TABLE supplier RENAME COLUMN pass TO passwd")
        con.commit()
        con.close()

    def add(self):
        con = sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            if self.var_sup_id.get()== "":
                messagebox.showerror("Greška","ID dobavljača mora biti unet.", parent=self.root)
            else:
                cur.execute("Select * from supplier where eid=?", (self.var_sup_id.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Greška","ID dobavljača je već dodeljen nekom zaposlenom, molim izmenite ili dodelite drugi broj.", parent=self.root)
                else:
                    cur.execute("""INSERT INTO supplier 
                        (eid, name, contact, email, adress, pay) 
                        VALUES (?,?,?,?,?,?)""",
                                (
                                    self.var_sup_id.get(),
                                    self.var_name.get(),
                                    self.var_num.get(),
                                    self.var_email.get(),
                                    self.var_adress.get(),
                                    self.var_pay.get()
                                )
                                )
                    con.commit()
                    messagebox.showinfo("Uspeh", "Dobavljač uspešno dodat!", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Greška", f"Greška iz razloga : {str(ex)}", parent=self.root)
        finally:
            con.close()


    def show(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            cur.execute("Select * from supplier")
            rows=cur.fetchall()
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for row in rows:
                self.SupplierTable.insert('', END, values=row)

        except Exception as ex:
             messagebox.showerror("Greška",f"Greška iz razloga : {str(ex)}", parent=self.root)
        finally:
            con.close()

#olaksavanje-update-dugmeta
    def get_data(self,ev):
        f=self.SupplierTable.focus()
        content=(self.SupplierTable.item(f))
        row=content['values']
        print(row)
        self.var_sup_id.set(row[0])
        self.var_name.set(row[1])
        self.var_num.set(row[2])
        self.var_email.set(row[3])
        self.var_adress.set(row[4])
        self.var_pay.set(row[5])

    def update(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        try:
            if self.var_sup_id.get() == "":
                messagebox.showerror("Greška", "ID Dobavljača mora biti unet.", parent=self.root)
            else:
                cur.execute("Select * from supplier where eid=?", (self.var_sup_id.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Greška",
                                         "Greška u ID dobavljača.", parent=self.root)
                else:
                    cur.execute("""UPDATE supplier SET 
                        (eid=?, name=?, contact=?, email=?, adress=?, pay=?) 
                        VALUES (?,?,?,?,?,?)""",
                                (
                                    self.var_sup_id.get(),
                                    self.var_name.get(),
                                    self.var_num.get(),
                                    self.var_email.get(),
                                    self.var_adress.get(),
                                    self.var_pay.get()
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
            if self.var_sup_id.get() == "":
                messagebox.showerror("Greška", "ID Dobavljača mora biti unet.", parent=self.root)
            else:
                cur.execute("Select * from supplier where eid=?", (self.var_sup_id.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Greška",
                                         "Greška u ID zaposlenog.", parent=self.root)
                else:
                    op=messagebox.askyesno("Potvrda","Da li stvarno želite da obrišete unos?", parent=self.root)
                    if op == True:
                        cur.execute("DELETE FROM supplier WHERE eid=?", (self.var_sup_id.get(),))
                        con.commit()
                        messagebox.showinfo("Brisanje", "Uspešno izbrisana stavka.", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Greška", f"Greška iz razloga : {str(ex)}", parent=self.root)
        finally:
            con.close()

    def clear(self):
        self.var_sup_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_adress.set("")
        self.var_pay.set("")

    def search(self):

        search_map = {
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
                cur.execute(f"SELECT * FROM supplier WHERE {column} LIKE ?", (f"%{self.var_searchtxt.get()}%",))
                rows=cur.fetchall()
                self.SupplierTable.delete(*self.SupplierTable.get_children())
                if len(rows) != 0:
                    for row in rows:
                        self.SupplierTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Greška", "Nije pronađen zapis.", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Greška", f"Greška iz razloga : {str(ex)}", parent=self.root)
        finally:
            con.close()




if __name__=="__main__":
    root=Tk()
    obj=supplierClass(root)
    root.mainloop()