from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk, messagebox
import sqlite3

class productClass:
    def __init__(self,root, on_close=None):
        self.on_close = on_close
        self.root = root
        # self.create_db()
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        x = (screen_w // 2) - (1350 // 2)
        y = (screen_h // 2) - (700 // 2)
        self.root.geometry(f"1350x700+{x}+{y}")
        self.root.after(100, self.root.deiconify)
        self.root.title("Kategorija")
        self.root.config(bg="white")  # dark navy blue #1e2a3a
        self.root.resizable(False, False)
        # self.root.state("zoomed")
        self.root.bind("<Escape>", lambda e: self.on_close() if self.on_close else self.root.destroy())

        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()


        self.var_category = StringVar()
        self.var_product = StringVar()
        self.var_supplier = StringVar()
        self.var_name = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_status = StringVar()


        # ========BackButton================================================================================================

        btn_back = Button(self.root,
                          command=lambda: self.on_close() if self.on_close else self.root.destroy(),
                          font=("Segoe UI", 12), bg="white", relief="groove", text="◄ Nazad")
        btn_back.place(x=15, y=50)

        # =========Title===================================================================================================

        title = Label(self.root, text="Upravljanje proizvodima", font=("Segoe UI", 15), bg="lightblue")
        title.place(x=200, y=50, width=1000)


        #==============Box====================================================================================================
        product_frame = Frame(self.root, bd=3, relief="groove", bg="white")
        product_frame.place(x=10,y=200,width=650,height=450)

        # scrolly = Scrollbar(product_frame, orient="vertical")
        # scrollx = Scrollbar(product_frame, orient="horizontal")

        # =========Title2===================================================================================================

        title = Label(product_frame, text="Proizvodi", font=("Segoe UI", 15), bg="lightblue")
        title.pack(side=TOP, fill=X)

        #======Labels======================================================================================================

        lbl_category = Label(product_frame,text="Kategorija", font=("Segoe UI", 15), bg="white")
        lbl_category.place(x=30,y=50)

        lbl_supplier = Label(product_frame,text="Dobavljač", font=("Segoe UI", 15), bg="white")
        lbl_supplier.place(x=30,y=110)

        lbl_product = Label(product_frame,text="Proizvod", font=("Segoe UI", 15), bg="white")
        lbl_product.place(x=30,y=170)

        lbl_price = Label(product_frame,text="Cena", font=("Segoe UI", 15), bg="white")
        lbl_price.place(x=30,y=230)

        lbl_qty = Label(product_frame,text="Količina", font=("Segoe UI", 15), bg="white")
        lbl_qty.place(x=30,y=290)

        lbl_status = Label(product_frame,text="Stanje", font=("Segoe UI", 15), bg="white")
        lbl_status.place(x=30,y=350)

        #====Fields==================================================================================================================
        cmb_cat = ttk.Combobox(product_frame, textvariable=self.var_category, values=("Odabrati","Kategorija","Dobavljač"), state="readonly")
        cmb_cat.place(x=250,y=55)
        cmb_cat.current(0)

        cmb_supplier = ttk.Combobox(product_frame, textvariable=self.var_supplier, values=("Odabrati","Kategorija","Dobavljač"), state="readonly")
        cmb_supplier.place(x=250, y=110)
        cmb_supplier.current(0)

        txt_product = Entry(product_frame, textvariable=self.var_product, font=("Segoe UI", 12), bg="white")
        txt_product.place(x=250, y=170)

        txt_price = Entry(product_frame, textvariable=self.var_price, font=("Segoe UI", 12), bg="white")
        txt_price.place(x=250, y=230)

        txt_qty = Entry(product_frame, textvariable=self.var_qty, font=("Segoe UI", 12), bg="white")
        txt_qty.place(x=250, y=290)

        cmb_status = ttk.Combobox(product_frame, textvariable=self.var_status, values=("Odabrati","Na stanju","Nema"), state="readonly")
        cmb_status.place(x=250, y=350)
        cmb_status.current(0)

        # =========Buttons================================================================================================

        btn_save=Button(product_frame, font=("Segoe UI", 12), bg="white", relief="groove", text="Sačuvati")
        btn_save.place(x=100, y=400)

        btn_update = Button(product_frame, font=("Segoe UI", 12), bg="white", relief="groove", text="Ažurirati")
        btn_update.place(x=200, y=400)

        btn_delete = Button(product_frame,  font=("Segoe UI", 12), bg="white", relief="groove", text="Obrisati")
        btn_delete.place(x=300, y=400)

        btn_clear = Button(product_frame, font=("Segoe UI", 12), bg="white", relief="groove", text="Očistiti polja")
        btn_clear.place(x=400, y=400)

        # ========Search Frame================================================================================================
        SearchFrame = LabelFrame(self.root, text="Pretraga", bg="white", font=("Segoe UI", 12))
        SearchFrame.place(x=250, y=90, width=880, height=80)

        # ======Options================================================================================================
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby,
                                  values=("Odabrati", "Kategorija", "Dobavljač", "Name"), state="readonly", justify="center",
                                  font=("Segoe UI", 15))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=("Segoe UI", 15), bg="white").place(
            x=300, y=10, width=300)
        btn_search = Button(SearchFrame, text="Pretraga", font=("Segoe UI", 15), bg="white")
        btn_search.place(x=650, y=8, width=200, height=30)


        #=======Frame=======================================================================================================
        p_frame = Frame(self.root, bd=3, relief="groove")
        p_frame.place(x=10, y=500, width=600,height=390)

        scrolly = Scrollbar(p_frame, orient="vertical")
        scrollx = Scrollbar(p_frame, orient="horizontal")

        self.ProductTable = ttk.Treeview(
            p_frame,
            columns=("pid", "category", "supplier", "name", "price", "qty","status"),
            show="headings"
        )
        scrolly.config(command=self.ProductTable.yview)
        scrollx.config(command=self.ProductTable.xview)

        self.ProductTable.config(yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        self.ProductTable.heading("pid", text="ID", anchor=CENTER)
        self.ProductTable.heading("category", text="Kategorija", anchor=CENTER)
        self.ProductTable.heading("supplier", text="Dobavljač", anchor=CENTER)
        self.ProductTable.heading("name", text="Naziv", anchor=CENTER)
        self.ProductTable.heading("price", text="Cena", anchor=CENTER)
        self.ProductTable.heading("qty", text="Količina", anchor=CENTER)
        self.ProductTable.heading("status", text="Stanje", anchor=CENTER)

        self.ProductTable.column("pid", width=15)
        self.ProductTable.column("category", width=100)
        self.ProductTable.column("supplier", width=100)
        self.ProductTable.column("name", width=100)
        self.ProductTable.column("price", width=100)
        self.ProductTable.column("qty", width=100)
        self.ProductTable.column("status", width=100)

        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.pack(side=BOTTOM, fill=X)
        self.ProductTable.pack(fill=BOTH, expand=1)

        # self.ProductTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()

        #=====Func====================================================================================================================

    def create_db(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS product (
                       pid INTEGER PRIMARY KEY AUTOINCREMENT,
                       category TEXT,
                       supplier TEXT,
                       product TEXT,
                       price TEXT,
                       qty TEXT,
                       status TEXT
                    )""")
        con.commit()
        con.close()

    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_category.get() == "":
                messagebox.showerror("Greška", "ID Zaposlenog mora biti unet!", parent=self.root)
            else:
                cur.execute("Select  * from employee where eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Greška", "Broj je prethodno dodeljen postojećem zaposlenom.",
                                         parent=self.root)
                else:
                    cur.execute(
                        "Insert into employee (eid, name, email, gender, contact, dob, doj, password, utype, adress, salary) values(?,?,?,?,?,?,?,?,?,?,?)",
                        (
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
            cur.execute("Select * from product")
            rows = cur.fetchall()
            self.ProductTable.delete(*self.ProductTable.get_children())
            for row in rows:
                self.ProductTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Greška", f"Greška iz razloga: {str(ex)}", parent=self.root)
        finally:
            con.close()

    def get_data(self, event):
        f = self.EmployeeTable.focus()
        content = self.EmployeeTable.item(f)
        row = content['values']
        if not row:  # ✅ guard against empty click
            return
        # remove print(row) before shipping
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
                           password=?,
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
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Greška", "ID zaposlenog mora biti unet!", parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Greška", "Nevažeći ID zaposlenog.", parent=self.root)
                else:
                    op = messagebox.askyesno("Potvrda", "Da li stvarno  želite da obrišete zaposlenog?",
                                             parent=self.root)
                    if op == True:
                        cur.execute("delete from employee where eid=?", (self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Brisanje", "Podaci uspešno obrisani.")
                        self.clear()
                        self.show()
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
    obj=(productClass(root))
    root.mainloop()