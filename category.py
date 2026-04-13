from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk, messagebox
import sqlite3

class categoryClass:
    def __init__(self,root, on_close=None):
        self.on_close = on_close
        self.root = root
        self.create_db()
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

        self.var_cat_id = StringVar()
        self.var_name = StringVar()

        # ========BackButton================================================================================================

        btn_back = Button(self.root,
                          command=lambda: self.on_close() if self.on_close else self.root.destroy(),
                          font=("Segoe UI", 12), bg="white", relief="groove", text="◄ Nazad")
        btn_back.place(x=15, y=50)

        # =========Title===================================================================================================

        title = Label(self.root, text="Upravljanje kategorijama proizvoda", font=("Segoe UI", 15), bg="lightblue")
        title.place(x=200, y=50, width=1000)

        #=======Options===================================================================================================
        lbl_name = Label(self.root, text="Unesite ime kategorije", font=("Segoe UI", 12), bg="white")
        lbl_name.place(x=200, y=200)

        txt_supplier_invoice = Entry(self.root, textvariable=self.var_name, font=("Segoe UI", 12), bg="white")
        txt_supplier_invoice.place(x=500, y=200, width=400)

        lbl_cid = Label(self.root, text="Unesite broj kategorije", font=("Segoe UI", 12), bg="white")
        lbl_cid.place(x=200, y=300)

        cid_supplier = Entry(self.root, textvariable=self.var_cat_id, font=("Segoe UI", 12), bg="white")
        cid_supplier.place(x=500, y=300, width=400)

        # =========Buttons================================================================================================

        btn_save = Button(self.root, font=("Segoe UI", 12), bg="white", relief="groove",
        command=self.add, text="Sačuvati")
        btn_save.place(x=450, y=350)

        btn_update = Button(self.root, font=("Segoe UI", 12), bg="white", relief="groove",
        command=self.update,text="Ažurirati")
        btn_update.place(x=600, y=350)

        btn_delete = Button(self.root, font=("Segoe UI", 12), bg="white", relief="groove",
        command=self.delete,text="Obrisati")
        btn_delete.place(x=750, y=350)

        btn_clear = Button(self.root, font=("Segoe UI", 12), bg="white", relief="groove",
        command=self.clear,text="Očistiti polja")
        btn_clear.place(x=900, y=350)

        #===========Field==================================================================================================


        cat_frame = Frame(self.root, bd=3, relief="groove")
        cat_frame.pack(side=BOTTOM, fill=X)

        scrolly = Scrollbar(cat_frame, orient="vertical")
        scrollx = Scrollbar(cat_frame, orient="horizontal")



        self.CategoryTable = ttk.Treeview(
            cat_frame,
            columns=("cid", "name"),
            show="headings"
        )
        scrolly.config(command=self.CategoryTable.yview)
        scrollx.config(command=self.CategoryTable.xview)

        self.CategoryTable.config(yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        self.CategoryTable.heading("cid", text="ID kategorije", anchor=CENTER)
        self.CategoryTable.heading("name", text="Ime", anchor=CENTER)

        self.CategoryTable.column("cid", width=15)
        self.CategoryTable.column("name", width=100)


        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.pack(side=BOTTOM, fill=X)
        self.CategoryTable.pack(fill=BOTH, expand=1)

        self.CategoryTable.bind("<ButtonRelease-1>", self.get_data)

        #======Funcys===================================================================================================


    def create_db(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS category
                       (
                           cid INTEGER PRIMARY KEY,
                           name TEXT
                       )""")
        con.commit()
        con.close()


    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_cat_id.get() == "":
                messagebox.showerror("Greška", "Broj kategorije mora biti unet!", parent=self.root)
            else:
                cur.execute("Select  * from category where cid=?", (self.var_cat_id.get(),))
                row=cur.fetchone()
                if row is not None:
                    messagebox.showerror("Greška", "Broj je prethodno dodeljen postojećoj kategoriji.", parent=self.root )
                else:
                    cur.execute("Insert into category (cid, name) values(?,?)",(
                                        self.var_cat_id.get(),
                                        self.var_name.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Uspeh!", "Uspešno dodata kategorija na spisak!", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Greška", f" Greška iz razloga: {str(ex)}")
        finally:
            con.close()

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("Select * from category")
            rows=cur.fetchall()
            self.CategoryTable.delete(*self.CategoryTable.get_children())
            for row in rows:
                self.CategoryTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Greška", f"Greška iz razloga: {str(ex)}", parent=self.root)
        finally:
            con.close()

    def get_data(self, event):
        f = self.CategoryTable.focus()
        content = self.CategoryTable.item(f)
        row = content['values']
        if not row:  # ✅ guard against empty click
            return
        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])

    def update(self):
        if self.var_cat_id.get() == "":
            messagebox.showerror("Greška", "Broj kategorije mora biti unet!", parent=self.root)
            return

        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM category WHERE cid=?", (self.var_cat_id.get(),))
            row = cur.fetchone()
            if row is None:
                messagebox.showerror("Greška", "Nevažeći broj kategorije.", parent=self.root)
            else:
                cur.execute(
                    """UPDATE category
                       SET name=?
                       WHERE cid = ?""",
                    (
                        self.var_name.get(),
                        self.var_cat_id.get()
                    )
                )
                con.commit()
                messagebox.showinfo("Uspeh!", "Uspešno ažurirani podaci kategorije sa spiska!", parent=self.root)
                self.clear()
        except Exception as ex:
            messagebox.showerror("Greška", f"Greška iz razloga: {str(ex)}", parent=self.root)
        finally:
            con.close()


    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_cat_id.get() == "":
                messagebox.showerror("Greška", "Broj kategorije mora biti unet!", parent=self.root)
            else:
                cur.execute("Select * from category where cid=?", (self.var_cat_id.get(),))
                row=cur.fetchone()
                if row is None:
                    messagebox.showerror("Greška", "Nevažeći broj kategorije.", parent=self.root)
                else:
                    op=messagebox.askyesno("Potvrda", "Da li stvarno  želite da obrišete podatke kategorije?", parent=self.root)
                    if op==True:
                        cur.execute("delete from category where cid=?", (self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("Brisanje","Podaci uspešno obrisani.")
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Greška", f"Greška iz razloga: {str(ex)}", parent=self.root)
        finally:
            con.close()


    def clear(self):
        self.var_cat_id.set("")
        self.var_name.set("")
        self.show()



if __name__=="__main__":
    root=Tk()
    obj=(categoryClass(root))
    root.mainloop()