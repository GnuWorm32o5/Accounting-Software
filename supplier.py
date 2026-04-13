from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk, messagebox
import sqlite3

class supplierClass:
    def __init__(self,root, on_close=None):
        self.root = root
        self.create_db()
        self.on_close = on_close
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        x = (screen_w // 2) - (1350 // 2)
        y = (screen_h // 2) - (700 // 2)
        self.root.geometry(f"1350x700+{x}+{y}")
        self.root.after(100, self.root.deiconify)
        self.root.title("Računovodstveni softver")
        self.root.config(bg="white")  # dark navy blue #1e2a3a
        self.root.resizable(False, False)
        # self.root.state("zoomed")
        self.root.bind("<Escape>", lambda e: self.on_close() if self.on_close else self.root.destroy())

        #All Variables =========================================================================================
        self.var_search_by=StringVar()
        self.var_search_txt=StringVar()

        self.var_sup_invoice=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
        self.txt_desc = Text(self.root, font=("Segoe UI", 12), bg="white")



        #========Search Frame================================================================================================
        SearchFrame=LabelFrame(self.root,text="Pretraga fakture", bg="white", font=("Segoe UI", 12))
        SearchFrame.place(x=250,y=20,width=880,height=80)

        #======Options================================================================================================
        lbl_search=Label(SearchFrame, text="Po broju", justify="center", font=("Segoe UI", 15))
        lbl_search.place(x=10,y=10,width=180)

        txt_search = Entry(SearchFrame, textvariable=self.var_search_txt, font=("Segoe UI", 15), bg="white").place(x=300, y=10, width=300)
        btn_search = Button(SearchFrame,command=self.search, text="Pretraga", font=("Segoe UI", 15), bg="white")
        btn_search.place(x=650, y=8, width=200, height=30)

        #=========Title===================================================================================================

        title = Label(self.root,text="Podaci dobavljača", font=("Segoe UI", 15), bg="lightblue")
        title.place(x =200, y=120, width=1000)

        # ========BackButton================================================================================================

        btn_back = Button(self.root,
                          command=lambda: self.on_close() if self.on_close else self.root.destroy(),
                          font=("Segoe UI", 12), bg="white", relief="groove", text="◄ Nazad")
        btn_back.place(x=15, y=120)


        #====Content===and Fields===================================================================================================================

        lbl_supplier_invoice=Label(self.root,text="Broj fakture",font=("Segoe UI", 12), bg="white")
        lbl_supplier_invoice.place(x =200, y=200)
        txt_supplier_invoice= Entry(self.root, textvariable=self.var_sup_invoice, font=("Segoe UI", 12), bg="white")
        txt_supplier_invoice.place(x=350, y=200)

        lbl_name = Label(self.root, text="Ime", font=("Segoe UI", 12), bg="white")
        lbl_name.place(x=200, y=300)
        txt_name = Entry(self.root, textvariable=self.var_name, font=("Segoe UI", 12), bg="white")
        txt_name.place(x=350, y=300)

        lbl_contact=Label(self.root,text="Kontakt",font=("Segoe UI", 12), bg="white")
        lbl_contact.place(x =200, y=400)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("Segoe UI", 12), bg="white")
        txt_contact.place(x=350, y=400)

        lbl_desc=Label(self.root, text="Opis", font=("Segoe UI", 12), bg="white")
        lbl_desc.place(x=600, y=200)

        self.txt_desc.place(x=700, y=200, height=250, width=400)

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



        self.SupplierTable = ttk.Treeview(
            emp_frame,
            columns=("invoice","name","contact", "description"),
            show="headings"
        )
        scrolly.config(command=self.SupplierTable.yview)
        scrollx.config(command=self.SupplierTable.xview)

        self.SupplierTable.config(yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        self.SupplierTable.heading("invoice", text="Faktura", anchor=CENTER)
        self.SupplierTable.heading("name", text="Ime", anchor=CENTER)
        self.SupplierTable.heading("contact", text="Kontakt", anchor=CENTER)
        self.SupplierTable.heading("description", text="Opis", anchor=CENTER)


        self.SupplierTable.column("invoice", width=15)
        self.SupplierTable.column("name", width=100)
        self.SupplierTable.column("contact", width=100)
        self.SupplierTable.column("description", width=100)



        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.pack(side=BOTTOM, fill=X)
        self.SupplierTable.pack(fill=BOTH, expand=1)

        self.SupplierTable.bind("<ButtonRelease-1>", self.get_data)


        self.show()
        #=================================================================================================

    def create_db(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS supplier
                       (
                           invoice INTEGER PRIMARY KEY,
                           name TEXT,
                           contact TEXT,
                           description TEXT
                       )""")
        con.commit()
        con.close()

    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Greška", "Broj fakture mora biti unet!", parent=self.root)
            else:
                cur.execute("Select  * from supplier where invoice=?", (self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row is not None:
                    messagebox.showerror("Greška", "Broj je prethodno dodeljen postojećoj fakturi.", parent=self.root )
                else:
                    cur.execute("Insert into supplier (invoice, name, contact, description) values(?,?,?,?)",(
                                        self.var_sup_invoice.get(),
                                        self.var_name.get(),
                                        self.var_contact.get(),
                                        self.txt_desc.get('1.0', END).strip()

                    ))
                    con.commit()
                    messagebox.showinfo("Uspeh!", "Uspešno dodata faktura na spisak!", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Greška", f" Greška iz razloga: {str(ex)}")
        finally:
            con.close()

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("Select * from supplier")
            rows=cur.fetchall()
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for row in rows:
                self.SupplierTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Greška", f"Greška iz razloga: {str(ex)}", parent=self.root)
        finally:
            con.close()

    def get_data(self, event):
        f = self.SupplierTable.focus()
        content = self.SupplierTable.item(f)
        row = content['values']
        if not row:  # ✅ guard against empty click
            return
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.txt_desc.delete('1.0', END)
        self.txt_desc.insert(END,row[3])

    def update(self):
        if self.var_sup_invoice.get() == "":
            messagebox.showerror("Greška", "Broj fakture mora biti unet!", parent=self.root)
            return

        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
            row = cur.fetchone()
            if row is None:
                messagebox.showerror("Greška", "Nevažeći broj fakture.", parent=self.root)
            else:
                cur.execute(
                    """UPDATE supplier
                       SET name=?,
                           contact=?,
                           description=?
                       WHERE invoice = ?""",
                    (
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.txt_desc.get('1.0', END),
                        self.var_sup_invoice.get()
                    )
                )
                con.commit()
                messagebox.showinfo("Uspeh!", "Uspešno ažuriran podaci fakture sa spiska!", parent=self.root)
                self.clear()
        except Exception as ex:
            messagebox.showerror("Greška", f"Greška iz razloga: {str(ex)}", parent=self.root)
        finally:
            con.close()


    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Greška", "Broj fakture mora biti unet!", parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?", (self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row is None:
                    messagebox.showerror("Greška", "Nevažeći broj fakture.", parent=self.root)
                else:
                    op=messagebox.askyesno("Potvrda", "Da li stvarno  želite da obrišete podatke ove fakture?", parent=self.root)
                    if op==True:
                        cur.execute("delete from supplier where invoice=?", (self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Brisanje","Podaci uspešno obrisani.")
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Greška", f"Greška iz razloga: {str(ex)}", parent=self.root)
        finally:
            con.close()


    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_desc.delete('1.0', END)
        self.show()



    COLUMN_MAP = {
        "Ime": "name",
        "Broj fakture": "invoice",
        "Kontakt": "contact"
    }

    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_search_txt.get() == "":
                messagebox.showerror("Greška", "Polje za pretragu ne može biti prazno.", parent=self.root)
            else:
                search_val = f"%{self.var_search_txt.get()}%"
                cur.execute("SELECT * FROM supplier WHERE invoice LIKE ?", (search_val,))
                rows = cur.fetchall()
                if rows:
                    self.SupplierTable.delete(*self.SupplierTable.get_children())
                    for row in rows:
                        self.SupplierTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Greška", "Nije pronađena faktura.", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Greška", f"Greška iz razloga: {str(ex)}", parent=self.root)
        finally:
            con.close()






if __name__=="__main__":
    root=Tk()
    obj=supplierClass(root)
    root.mainloop()