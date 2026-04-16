from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk, messagebox
import sqlite3
import os

class salesClass:
    def __init__(self,root, on_close=None):
        self.root = root
        # self.create_db()
        self.on_close = on_close
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        x = (screen_w // 2) - (1350 // 2)
        y = (screen_h // 2) - (700 // 2)
        self.root.geometry(f"1350x700+{x}+{y}")
        self.root.after(100, self.root.deiconify)
        self.root.title("Prodaja")
        self.root.config(bg="white")  # dark navy blue #1e2a3a
        self.root.resizable(False, False)
        # self.root.state("zoomed")
        self.root.bind("<Escape>", lambda e: self.on_close() if self.on_close else self.root.destroy())

        self.bill_list = []
        self.var_invoice = StringVar()

        # ========BackButton================================================================================================

        btn_back = Button(self.root,command=lambda: self.on_close() if self.on_close else self.root.destroy(),
                          font=("Segoe UI", 12), bg="white", relief="groove", text="◄ Nazad")
        btn_back.place(x=15, y=50)

        # =========Title===================================================================================================

        title = Label(self.root, text="Upravljanje prodajom", font=("Segoe UI", 15), bg="lightblue")
        title.place(x=200, y=50, width=1000)

        lbl_name = Label(self.root, text="Ime računa: ", font=("Segoe UI", 12), bg="white")
        lbl_name.place(x=500, y=150)

        txt_invoice = Entry(self.root, textvariable=self.var_invoice, font=("Segoe UI", 12), bg="white")
        txt_invoice.place(x=600, y=150)

        #============Button=============================================================================================

        btn_search = Button(self.root, text="Search",command=self.search, font=("Segoe UI", 12),bg="white")
        btn_search.place(x=800, y=150, height=30)

        btn_clear = Button(self.root, text="Clear",command=self.clear, font=("Segoe UI", 12),bg="white")
        btn_clear.place(x=900, y=150, height=30)

        #=====Left Frame===============================================================================================

        sales_Frame = Frame(self.root, bd=3, relief=GROOVE)
        sales_Frame.place(x=200,y=200,width=500,height=350)

        scrolly=Scrollbar(sales_Frame,orient=VERTICAL)
        self.Sales_List = Listbox(sales_Frame, font=("Segoe UI", 12), bg="white", yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.Sales_List.yview)
        self.Sales_List.pack(fill=BOTH, expand=True)
        self.Sales_List.bind("<ButtonRelease-1>", self.get_data)

        #======RightFrame================================================================================================

        bill_Frame = Frame(self.root, bd=3, relief=GROOVE)
        bill_Frame.place(x=750, y=200, width=500, height=350)

        scrolly2 = Scrollbar(bill_Frame, orient=VERTICAL)
        self.bill_area = Text(bill_Frame, font=("Segoe UI", 12), bg="white", yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT, fill=Y)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH, expand=True)

        self.show()


    def show(self):
        del self.bill_list[:]
        self.Sales_List.delete(0, END)
        # print(os.listdir("../Accounting-Software")) bill1.txt, category.py
        for i in os.listdir("bill"):
            # print(i.split('.'),i.split('.')[-1])
            if i.split(".")[1] == "txt":
                self.Sales_List.insert(END, i)
                self.bill_list.append(i.split('.')[0])


    def get_data(self, ev):
        index_ = self.Sales_List.curselection()
        file_name = self.Sales_List.get(index_)
        self.bill_area.delete(1.0, END)
        fp=open(f"bill/{file_name}","r")
        for i in fp:
            self.bill_area.insert(END, i)
        fp.close()


    def search(self):
        if self.var_invoice.get()=="":
            messagebox.showerror("Greška", "Ime računa mora biti unet.", parent=self.root)
        else:
            if self.var_invoice.get() in self.bill_list:
                fp=open(f"bill/{self.var_invoice.get()}.txt","r")
                self.bill_area.delete(1.0, END)
                for i in fp:
                    self.bill_area.insert(END, i)
                fp.close()
            else:
                messagebox.showerror("Greška", "Neispravno ime računa.", parent=self.root)

    def clear(self):
        self.var_invoice.set("")
        self.show()
        self.bill_area.delete(1.0, END)


if __name__=="__main__":
    root=Tk()
    obj=(salesClass(root))
    root.mainloop()